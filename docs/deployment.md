# Deployment

Deployment of a python program depends on what type of program you are deploying. Desktop apps, web apps, ETL scripts,
API's, internal tools, etc. all have different requirements.

Here are some practical deployment approaches for smaller projects, depending on how simple or complex they are:

---

## 🚀 1. Local Script / Cron Job

Best for **simple scripts** (ETL, backups, notifications, etc.)

* **Deploy**: copy code to server (via `git clone`, `scp`, or syncing)
* **Env**: use a virtual environment (`uv venv`, `python -m venv`, or `conda`)
* **Run**: directly with `python script.py` or via cron/systemd

👉 Example:

```bash
cd ~/my_project
uv venv
source .venv/bin/activate
uv pip install -r requirements.txt
python my_job.py
```

Pros: simple, fast.
Cons: less portable, harder to reproduce if env drifts.

---

## 📦 2. Installable Package

Best for projects you’ll re-use across multiple places.

* **Deploy**: build into a wheel or sdist
* **Install**: `pip install my_package-0.1.0-py3-none-any.whl`
* **Run**: `python -m my_package` or a CLI entry point

👉 Works well when you want:

* Versioning (`0.1.0`, `0.2.0` …)
* To install on multiple servers without manually copying source

---

## 🐳 3. Docker Container

Best for services you want **consistent across dev/prod**.

* Write a Dockerfile:

```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "my_job.py"]
```

* **Deploy**: `docker build -t my_job .` then `docker run my_job`
* **Schedule**: cron on the host, or Kubernetes Job

Pros: consistent, portable.
Cons: more setup overhead than bare venv.

## ⚡️ Quick Decision Tree

* **One-off script** → copy + venv
* **Reusable internal library** → package + pip install
* **Service/API that should “just work”** → Docker container

---

In most modern setups, if you have a Python package that contains multiple ETL jobs, 
the **common pattern is to containerize the entire package** and then deploy that image wherever you run jobs.

The differences are in **how you execute the individual jobs** inside that container and how you **manage orchestration**.

---

## **Typical Pattern**

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

## **Why This Approach Works Well**

* **Reusability** — One image can run all jobs, avoiding duplication.
* **Consistency** — All jobs share the same dependency versions and base environment.
* **Smaller CI/CD surface** — You only need to build and push one image per release.
* **Version control** — The image tag maps directly to your package release.

---

## **Alternatives**

* **One image per job**

    * Sometimes used if jobs have wildly different dependencies or resource requirements.
    * Downside: more images to maintain and slower builds if you change common code.
* **Shared base + thin job layers**

    * You create a common base image for your package and layer job-specific commands/images on top.
    * Speeds up rebuilds for large pipelines.

---

💡 **Rule of thumb:**
If all ETL jobs share most dependencies and code, **use one container image** with multiple entry points.
If jobs have very different stacks or run in completely different runtime environments, **split them into separate images**.

---

If you want, I can draw you a **container + orchestrator diagram** showing how a single Python package with 
multiple ETL jobs gets deployed and triggered. That’s usually the easiest way to visualize it.
