# Deploying Python Programs

Deployment of a python program depends on what type of program you are deploying. Desktop apps, web apps, ETL scripts,
API's, internal tools, etc. all have different requirements.

## Deployment Types

There are 3 main forms:

1. Standard script/venv.
2. Docker container.
3. Executable file.

---

### 🚀 Local Script / Cron Job
 
Best for **simple scripts** (ETL, backups, notifications, etc.)

* **Deploy**: copy code to server (via `git clone`, `scp`, or syncing)
* **Env**: use a virtual environment (`uv venv`, `python -m venv`, or `conda`)
* **Run**: directly with `python script.py` or via cron/systemd

👉 Example:

```bash
cd ~/my_project                       # create folder
uv venv                               # create the venv
source .venv/bin/activate             # activate the venv
uv pip install -r requirements.txt    # install dependencies

# run the script like
python my_job.py
# or 
python -m my_job
```

From here you can setup to run with a cronjob or another program. 

Cronjob:
```bash
crontab -e

# save this in the crontab file that opens
0/20 * * * * source /Users/tyleranderson/PyCharmProjects/project/backup_tmp_dir.sh 
```

or Airflow:
```python
import subprocess
import datetime
from airflow.decorators import dag, task

@dag(default_args={"owner": "airflow"},
     schedule_interval="*/10 * * * *",
     dagrun_timeout=datetime.timedelta(hours=1),
     max_active_runs=1,
     max_active_tasks=1,
     start_date=datetime.datetime(2025, 5, 1),
     catchup=False)
def run_job():
    @task
    def job_1():
        subprocess.run(["bash", "-c", "source /path/to/file"], check=True)
        
    @task
    def job_2():
        subprocess.run(["bash", "-c", "source /path/to/another_file"], check=True)
        
    job_1 >> job_2

        
run_job()
```

- Pros: simple, fast.
- Cons: less portable, harder to reproduce if env drifts.

---

### 🐳 Docker Container

Best for services you want **consistent across dev/prod**. Much more robust.

* Write a Dockerfile:

```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY .. .
CMD ["python", "my_job.py"]
```

* **Deploy**: `docker build -t my_job .` then `docker run my_job`
* **Schedule**: cron on the host, or Kubernetes Job

Pros: consistent, portable.
Cons: more setup overhead than bare venv.

### 🤖Executable File

You can also use pyinstaller (or other libraries that freeze your python code) to create an
executable file. This would be a good idea for a desktop app or something that a user chooses
to run on their own. 

Pro: no need for user to have python installed on their computer, easy to distribute.

## Docker, Python, and Multiple Execution Points

In most modern setups, if you have a Python package that contains multiple ETL jobs, 
the **common pattern is to containerize the entire package** and then deploy that image wherever you run jobs.

The differences are in **how you execute the individual jobs** inside that container and how you **manage orchestration**.

---

### **Typical Pattern**

1. **Single container image**

    * You build one Docker image for your Python package (with all dependencies baked in).
    * This image is versioned and pushed to a container registry (e.g., AWS ECR, GCP Artifact Registry, Docker Hub).
    * Keeps dependencies consistent across jobs.

2. **Multiple entry points / commands**

    * Each ETL job is exposed via a CLI entry point in your `pyproject.toml` or `setup.py`

      ```toml
      [project.scripts]
      etl_job_a = "my_package.jobs.job_a:main"
      etl_job_b = "my_package.jobs.job_b:main"
      ```
    * At runtime, the orchestrator decides which command to run:

      ```bash
      docker run my-etl-image:1.0 etl_job_a
      ```
    * This avoids rebuilding multiple images for each job.

3. **Orchestrator triggers containers**

    * **Airflow**, **Prefect**, **Dagster**, or Kubernetes **CronJobs** call the container with the appropriate arguments or entry point.
    * Example in Airflow’s `DockerOperator`:

      ```python
      DockerOperator(
          task_id="run_etl_job_a",
          image="my-etl-image:1.0",
          command="etl_job_a",
          ...
      )
      ```

---

### **Why This Approach Works Well**

* **Reusability** — One image can run all jobs, avoiding duplication.
* **Consistency** — All jobs share the same dependency versions and base environment.
* **Smaller CI/CD surface** — You only need to build and push one image per release.
* **Version control** — The image tag maps directly to your package release.

---

💡 **Rule of thumb:**
If all ETL jobs share most dependencies and code, **use one container image** with multiple entry points.
If jobs have very different stacks or run in completely different runtime environments, **split them into separate images**.
