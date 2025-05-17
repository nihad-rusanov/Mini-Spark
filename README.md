## 📊 MiniSpark – Lightweight Data Processing Engine with SQL & Web UI

**MiniSpark** is a simplified, Spark-inspired data processing engine built in Python. It supports map/filter/reduce operations on large datasets and provides a web-based UI where users can upload CSV files and execute basic SQL-like queries.

---

## 🚀 Features

* Lightweight RDD engine (Resilient Distributed Dataset)
* Lazy evaluation with collect()
* Basic SQL query support (SELECT, WHERE with comparison ops)
* CSV/JSON file loading
* Web UI (Flask-based)
* Ready for deployment on platforms like Render

---

## 🧠 How It Works

Under the hood, MiniSpark:

* Parses your SQL query into RDD operations
* Builds a DAG (Directed Acyclic Graph) of operations
* Executes the DAG lazily when `collect()` is triggered
* Returns results to the browser

---

## 💻 Tech Stack

* Python 3.10
* Flask (Web UI)
* Gunicorn (WSGI server)
* CSV/JSON file parsing

---

## 🌐 Live Demo (if applicable)

> Deployed on [Render](https://mini-spark-1.onrender.com/)
> Upload your own dataset and try a query like:
> `SELECT name FROM products WHERE price > 1000`

---

## 🔍 SQL Query Limitations

Only simple queries are supported:

```sql
SELECT <column> FROM products WHERE <column> <operator> <value>
```

* Supported operators: `=`, `>`, `<`, `>=`, `<=`
* Only one `SELECT` column
* Only one condition in `WHERE`
* No support for `AND`, `OR`, `JOIN`, etc.
* String values don't require quotes: `category = Stationery`

---

## 📁 Project Structure

```
mini-spark/
├── app/                # Flask application
│   ├── __init__.py
│   ├── routes.py
│   ├── templates/
│   └── static/
├── rdd.py              # RDD implementation
├── sql_parser.py       # SQL to RDD translator
├── utils/
│   └── file_io.py      # CSV / JSON helpers
├── web_main.py         # App entry point
├── requirements.txt
└── render.yaml
```

---

## ⚙️ Running Locally

### 1. Clone the project

```bash
git clone https://github.com/nihad-rusanov/Mini-Spark.git
cd Mini-Spark
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the web app

```bash
python web_main.py
```

Visit `http://localhost:5000`

---

## ☁️ Deployment (Render.com)

If you're deploying without Docker:

* Ensure you have:

  * `requirements.txt`
  * `render.yaml`

### Example Render configuration:

```yaml
services:
  - type: web
    name: mini-spark
    runtime: python
    buildCommand: pip install -r requirements.txt
    startCommand: gunicorn web_main:app --bind=0.0.0.0:$PORT
```

---

## 🧪 Example Dataset

You can generate a 100,000-row realistic dataset using:

```bash
python generate_products_csv.py
```

Or use your own CSV with columns like:

```
id,name,category,price,stock
1,Laptop,Electronics,1200.00,10
...
```

---

## ✅ TODO / Future Enhancements

* Support for multiple SELECT columns
* Support for `AND` / `OR` in SQL WHERE
* Aggregation functions: `COUNT`, `AVG`, `SUM`
* GroupBy operations
* Web-based DAG visualization
* Parallel map execution

---

## 📜 License

MIT License – use freely, contribute openly.
