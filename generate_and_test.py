import csv
import random
import os

def generate_large_product_csv(filename="products_large.csv", num_rows=100000):
    categories = ['Electronics', 'Stationery', 'Books', 'Clothing', 'Home', 'Beauty', 'Tools']
    product_names = [
        'Laptop', 'Phone', 'Book', 'Pen', 'Notebook', 'Tablet', 'Monitor', 'Headphones',
        'Shirt', 'Chair', 'Desk', 'Mouse', 'Keyboard', 'Lamp', 'Mirror', 'Backpack'
    ]

    # Klasörü oluştur
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['id', 'name', 'category', 'price', 'stock'])

        for i in range(1, num_rows + 1):
            name = random.choice(product_names)
            category = random.choice(categories)
            price = round(random.uniform(5.00, 5000.00), 2)
            stock = random.randint(0, 1000)
            writer.writerow([i, name, category, price, stock])

    print(f"✅ CSV dosyası oluşturuldu: {filename} ({num_rows} satır)")

if __name__ == "__main__":
    generate_large_product_csv("data/products_large.csv", num_rows=100000)
