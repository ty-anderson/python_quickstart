# Important Libraries - Getting Started

## Pandas

Pandas is a well-known data handling library. It has the ability to extract, manipulate, and load data.

The central component to pandas is the DataFrame. This is where tabular data is loaded and lives in memory.
```py
import pandas as pd

# blank dataframe
df = pd.DataFrame()

# load a dict into a dataframe
sample_data = {'id', [1, 2, 3], 'value', [200, 300, 400]}
df = pd.DataFrame(sample_data)

# load direct from other formats
df = pd.read_csv('path/to/csv/file.csv')
df = pd.read_parquet('path')
df = pd.read_excel('path')
df = pd.read_json('path')
df = pd.read_sql('sql statement', sqlalchemy_conn)
df = pd.read_html('io')
df = pd.read_xml('io')
df = pd.read_clipboard()
```

More here https://pandas.pydata.org/docs/reference/io.html

### Transformations

Once you have data loaded into a dataframe, you can perform all kinds of operations on the values.
There are generally two ways of performing modifications. Iterating through each value (not recommended) and
across columns (called vectorization). A vectorized operation can look like this:

```py
df = pd.read_csv('path/to/file.csv') # sample data

# performing math computations across columns. You can overwrite existing columns or create new columns
df['int_column_new'] = df['int_column_01'] + df['int_column_02']
df['int_column_01'] = df['int_column_01'] - df['int_column_02']
df['float_column_new'] = df['float_column_01'] * df['float_column_02']
df['float_column_01'] = df['float_column_01'] / df['float_column_02']

# perform string operations
df['string_col'] = df['string_col'].str.replace('-', '')
```

### Filtering

```py
df = pd.read_csv('path/to/file.csv') # sample data

# filter where column_name is equal to a value
df = df[df['column_name'] == 'certain_value']
# not equal
df = df[df['column_name'] != 'certain_value']
# substring
df = df[df['column_name'].str.contains('partial_string_match')]
# drop rows where column_name equals any of the list values
df = df[~df['column_name'].isin(['list', 'of', 'values'])]
```

### Change Data Types

```py
df = pd.read_csv('path/to/file.csv') # sample data

df['str_num_values'] = df['str_num_values'].astype(int)
df['str_num_values'] = df['str_num_values'].astype(str)
df['str_num_values'] = df['str_num_values'].astype(float)

# dates
df['date_str_values'] = pd.to_datetime(df['date_str_values'])  # gives datetime format
df['date_str_values'] = pd.to_datetime(df['date_str_values']).dt.date  # gives just date, no time
```

Helpful functions:

[Merge (like SQL join)](https://pandas.pydata.org/docs/reference/api/pandas.merge.html)
[Melt (convert columns to rows)](https://pandas.pydata.org/docs/reference/api/pandas.melt.html)

## SQLAlchemy

SQLAlchemy is a robust database management utility library. There are two main components; Core and ORM.
Core is more base level, closer to the database API, while ORM aims to abstract some of the complexity
of managing connections with sessions. Generally Core is better for pure database operations while the 
ORM is geared toward web applications.

Has full compatibility with Postgres, MySQL, SQLite, SQL Server, and Oracle.

Connection strings look like this:

```py
db_str = 'dialect+driver://username:password@host:port/database'

postgres = "postgresql+psycopg2://scott:tiger@localhost/public"

sql_server = 'mssql+pyodbc://host/database?trusted_connection=yes&driver=ODBC+Driver+18+for+SQL+Server&TrustServerCertificate=yes'
```

Modeling Tables

```py
from sqlalchemy import (create_engine, Table, MetaData, Column, String, 
                        Integer, Double, Date, DateTime, Boolean, func)

engine = create_engine('postgresql+psycopg2://scott:tiger@localhost/public')  # engines are what connects to the db

meta = MetaData()  # create a metadata object to attach tables to

# model out the table
table1 = Table('table_name',
               meta,
               Column('id', Integer, primary_key=True),
               Column('column1', String(255), unique=True),
               Column('column2', Double),
               Column('column3', Boolean, default=False),
               Column('column4', Date),
               Column('created_date', DateTime,
                        server_default=func.now()),
               schema='public'
               )

meta.create_all(engine)  # create all the tables that are connected to the metadata object, in the database
```

Once you have your model and engine ready, you can connect and start running operations:

```py
from sqlalchemy import create_engine, text

engine = create_engine('connection_string_to_db')

with engine.connect() as conn:
    query = 'SELECT * FROM table_name'
    result = conn.execute(text(query)).fetchall()
```
This will return a list of Row objects which contain the values in tuples (even if you only selected one column).
To pull these out of the nested tuples, you can use list comprehension.

```py
result = [r[0] for r in result]
```

Note that to run a raw SQL query we had to put it into a text() function. This function will sanitize the query to 
make sure there is no malicious injection happening. Sometimes it is difficult to transform data values in python
into a raw SQL query. SQLAlchemy has objects that can perform the same database functions, but in a more pythonic way.

```py
from sqlalchemy import select, insert, update, delete

df = pd.DataFrame(values)
data_dict = df.to_dict(orient='records')  # transform pandas dataframe into a dictionary of values

with engine.connect() as conn:                              # connect to database
    insert_stmt = insert(table_object).values(data_dict)    # create the insert statement
    conn.execute(insert_stmt)                               # execute the statement
    conn.commit()                                           # commit the changes
    
    value = conn.execute(select(table_object)).fetchone()
    values = conn.execute(select(table_object)).fetchall()
    
    update_stmt = update(user_table).where(user_table.c.id == 5).values(name="user #5")
    conn.execute(update_stmt)
    
    delete_stmt = delete(user_table).where(user_table.c.id == 5)
    conn.execute(delete_stmt)
    conn.commit()
```

## SQLite

SQLite is an embeddable OLTP database. In other words, it is a database that can be run in memory or from a file.
It is the most common database in the world being used in web apps, phone apps, IoT devices, and more.

[SQLite Docs](https://www.sqlite.org/docs.html)

## DuckDB

DuckDB is similar to SQLite, but is an OLAP database. It is incredibly fast and effective and processing large amounts
of data in memory. It can connect to other databases and perform direct queries on it, even being able to 
write queries on multiple separate databases 
[Mix and Match](https://duckdb.org/2024/01/26/multi-database-support-in-duckdb.html#mix-and-match).

[DuckDB Docs](https://duckdb.org/docs/)


## Pyspark

Spark is a distributed data handling library written in Java. It has a python API that allows users to
use Spark with Pyspark. In some ways it is very similar to pandas, but it can directly read and write to
Delta Lake tables, and it spreads the data handling tasks across multiple machines (distributed).

```py
df = spark.createDataFrame(data)
current_records = spark.sql("SELECT COALESCE(MAX(created_date), '2000-01-01') FROM lh_gold_01.fact_cms_star_rating").first()[0]
```

## dotenv

dotenv is a lightweight package that allows you to load environment variables into memory from a file. 

``pip install python-dotenv``

Create a ``.env`` file in your project like:

```dotenv
ENV_VAR_NAME='ENV_VAR_VALUE'
API_KEY_01='2JHDKFJH3KF'
```

```py
import os
from dotenv import load_dotenv

load_dotenv()

env_var = os.getenv('ENV_VAR_NAME')
api_key = os.getenv('API_KEY_01')
```

## Requests

Requests is a user-friendly way to make HTTP calls. Very good for API's.

``pip install requests``

```py
import requests

url = 'https://data.cms.gov/provider-data/api/1/metastore/schemas/dataset/items/4pq5-n9py?show-reference-ids=false'
response = requests.get(url)
print(response.status_code)
print(response.headers)
print(response.text)
```

Send post requests with auth details and payload.

```py
import requests
from io import BytesIO

response = requests.get(url, 
                        auth={'user': 'username', 'password': 'password_here'},
                        data={'payload_json': {'data': 'value'}},
                        files={'file': BytesIO()})
```

## Airflow

Airflow is an orchestration tool to run and monitor jobs. It allows you to program it in a way that it can
have dependencies. For example, only run one script after another has run successfully.

[Airflow Docs](https://airflow.apache.org/docs/apache-airflow/stable/index.html)

## Flask

Flask is a popular web app framework. It is very lightweight and has many "plugin" type packages that are built to 
be pieced together to achieve all desired features.

Web workers rule of thumb:

- Sync workers: ~50 - 100 concurrent users per worker.
- Async workers: ~500 - 1000+ concurrent users per worker.

Running a flask server:

- Standard run Flask: ``flask --app <.py file> run`` like ``flask --app app run``
- Run Flask on different port: ``flask --app app run --port 8080``
- Run Flask and expose to network: ``flask --app web_app/app run --host 0.0.0.0 --port 8080``
- Run Flask in prod with gunicorn: ``gunicorn -w 4 -b 0.0.0.0:8080 web_app.app:app``


### Self Hosting

Make sure to activate your python interpreter!

If you want to host your own flask app, gunicorn is a WSGI pure python server used for production.
You'll need to ``pip install gunicorn`` and then run the commands.

Running locally:

``gunicorn -w 4 'module_name:app_name'``

``-w`` is the number of workers, default is 1.

If you want to be able to access the site on the network, you need to bind to 0.0.0.0:

``gunicorn -w 4 -b 0.0.0.0:8000 'app:app''``

``0.0.0.0`` binds the app to all available network interfaces, making it accessible on your network.
This is a special ip address that tells your application to listen on all available network interfaces
of the machine, instead of just localhost. 

To make this accessible from the internet, you need to configure your router to forward traffic that 
goes to your chosen port (8000 in this case) to the machine that is running the app. This is done
with port forwarding in your router admin settings. Visually it might look like 
``public_ip:8000 -> server_local_ip:8000``. BTW this is called port forwarding.

You may need to update firewall config on the server to allow external connections 
on port 8000 (linux ``sudo ufw allow 8000``). 

If your ISP changes your public IP, you make need to use a dynamic DNS (DDNS) service like No-IP or DynDNS.

Security Warning: exposing your app to the internet comes with security risks. To mitigate:

1. Use HTTPS: Serve your app behind a reverse proxy like nginx with an SSL certificate.
2. Restrict Access: Limit access to specific IPs or use authentication to secure your app.
3. Monitor Logs: Monitor your server logs for unusual activity.

Stopping the app:

Use ``pgrep -fl gunicorn`` to show a list of gunicorn processes with their PIDs.

kill by bid: ``kill <pid>`` (kill by process ID)

OR

kill all gunicorn: ``pkill gunicorn`` (kill by process name)

For a more stable production environment, a process manager is better.

Create a systemd service file.

Then you can enable/disable/start/stop the app as a service.

```
sudo systemctl enable gunicorn  # auto start on boot
sudo systemctl start gunicorn  # prevent auto start on boot
sudo systemctl status gunicorn
sudo systemctl stop gunicorn
sudo systemctl restart <service-name>
```

When you make changes to a service file, you need to reload the service:

``sudo systemctl daemon-reload``

[Flask Docs](https://flask.palletsprojects.com/en/stable/)

## FastAPI

FastAPI is one of the most performant web frameworks available for python.

## Pyinstaller

Pyinstaller is a great way to create executable files. This makes your python program run
without needing python on the host machine. Great for sharing a python program with others
who do not have python on their computer.

```bash
# install
pip install pyinstaller

# create executable in one file.
pyinstaller --onefile script_name.py

# there are several flags that can be used
pyinstaller --onefile --noconsole --icon=your_icon.ico --add-data "config.json;." script_name.py
```

Pyinstaller will capture other .py files if you have more than one and they are imported.



## Other Interesting Libraries

### Locust

Locust is a load testing framework that can send millions of requests.

[Locust Docs](https://locust.io/)

### Reportlab

Creating PDF's can be difficult or require external software like LaTeX or wkhtmltopdf.

If you don't want to have these dependencies, reportlab is a pure python library to create PDFs.

``pip install reportlab``

ReportLab includes a low-level API for generating PDF documents directly from Python, 
and a higher-level template language—similar to HTML and the template systems used in 
web development—called RML. Generally, the second option is usually more convenient 
for those who must make exhaustive use of the capabilities of the library when 
generating documents. For the rest of the cases, the low-level API that we will 
describe in this article will suffice. However, you can find the official 
documentation here [https://docs.reportlab.com/](https://docs.reportlab.com/).

```py
from reportlab.pdfgen import canvas

c = canvas.Canvas("hello-world.pdf")
c.save()
```

```py
# import the canvas object
from reportlab.pdfgen import canvas

# create a Canvas object with a filename
c = canvas.Canvas("rl-hello_again.pdf", pagesize=(595.27, 841.89))  # A4 pagesize
# draw a string at x=100, y=800 points
# point ~ standard desktop publishing (72 DPI)
# coordinate system:
#   y
#   |
#   |   page
#   |
#   |
#   0-------x
c.drawString(50, 780, "Hello Again")
# finish page
c.showPage()
# construct and save file to .pdf
c.save()
```

Use standard page sizes like letter, A4, and more.

```py
from reportlab.lib.pagesizes import letter

c = canvas.Canvas("hello-world.pdf", pagesize=letter)
```

Make shapes in PDF.

```py
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

w, h = A4
c = canvas.Canvas("shapes.pdf", pagesize=A4)
c.drawString(30, h - 50, "Line")
x = 120
y = h - 45
c.line(x, y, x + 100, y)
c.drawString(30, h - 100, "Rectangle")
c.rect(x, h - 120, 100, 50)
c.drawString(30, h - 170, "Circle")
c.circle(170, h - 165, 20)
c.drawString(30, h - 240, "Ellipse")
c.ellipse(x, y - 170, x + 100, y - 220)
c.showPage()
c.save()
```

You can make tables from a pandas dataframe

```py
from reportlab.lib.pagesizes import letter, landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors

filename = "landscape_table_fit.pdf"
doc = SimpleDocTemplate(filename, pagesize=landscape(letter))

# Example DataFrame
import pandas as pd
df = pd.DataFrame({
    "Column 1": ["A", "B", "C"],
    "Column 2": [1, 2, 3],
    "Column 3": [4.5, 5.5, 6.5],
    "Column 4": ["Long Text Example", "Another Example", "More Text"],
    "Column 5": ["X", "Y", "Z"]
})

# Convert DataFrame to list of lists
data = [df.columns.tolist()] + df.values.tolist()

# Calculate dynamic column widths to fit the page
page_width = landscape(letter)[0]
available_width = page_width - 40  # Subtract margins
num_columns = len(df.columns)
col_width = available_width / num_columns

# Create a table with fixed column widths
table = Table(data, colWidths=[col_width] * num_columns)
table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ('GRID', (0, 0), (-1, -1), 1, colors.grey),
]))

# Add the table to the elements list
elements = [table]

# Build the document
doc.build(elements)

print(f"PDF saved as {filename}")
```
