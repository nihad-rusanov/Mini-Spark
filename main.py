from rdd import RDD
from utils.file_io import read_csv
from sql_parser import parse_query

data = read_csv("data/product.csv")
rdd = RDD(data[1:])  
result = (
    rdd
    .filter(lambda row: float(row[3]) > 500)
    .map(lambda row: row[1])  
    .collect()
)

data = read_csv("data/product.csv")
print(data)
header, rows = data[0], data[1:]

query = "SELECT name FROM products WHERE price > 500"
transformer = parse_query(query)
map_fn, filter_fn = transformer(header)

rdd = RDD(rows)
result = rdd.filter(lambda row: filter_fn(row)).map(lambda row: map_fn(row)).collect()
print("SQL Result", result)


