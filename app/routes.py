from flask import Blueprint, render_template, request
from utils.file_io import read_csv
from rdd import RDD
from sql_parser import parse_query

main = Blueprint('main', __name__)

@main.route("/", methods=["GET", "POST"])
def index():
    result = []
    if request.method == "POST":
        file = request.files["dataset"]
        query = request.form["query"]

        # Dosyayı oku
        filepath = "data/uploaded.csv"
        file.save(filepath)
        data = read_csv(filepath)
        header, rows = data[0], data[1:]

        # SQL sorgusunu işle
        try:
            transformer = parse_query(query)
            map_fn, filter_fn = transformer(header)

            rdd = RDD(rows)
            result = rdd.filter(lambda row: filter_fn(row)).map(lambda row: map_fn(row)).collect()
        except Exception as e:
            result = [f"HATA: {str(e)}"]

    return render_template("index.html", result=result)
