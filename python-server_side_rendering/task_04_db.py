from flask import Flask, render_template, request
import json, csv, sqlite3

app = Flask(__name__)


def read_json(file_path):
    with open(file_path) as f:
        return json.load(f)


def read_csv(file_path):
    products = []
    with open(file_path, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            products.append({
                "id": int(row["id"]),
                "name": row["name"],
                "category": row["category"],
                "price": float(row["price"])
            })
    return products


def read_sql(file_path):
    products = []
    try:
        conn = sqlite3.connect(file_path)
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()
        for row in rows:
            products.append({
                "id": row[0],
                "name": row[1],
                "category": row[2],
                "price": row[3]
            })
        conn.close()
    except Exception as e:
        raise e
    return products


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/items")
def show_items():
    data = read_json("items.json")
    items_list = data.get("items", [])

    return render_template("items.html", items=items_list)


@app.route("/products")
def show_products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)
    error = None
    products = []

    if source == 'json':
        products = read_json('products.json')
    elif source == 'csv':
        products = read_csv('products.csv')
    elif source == 'sql':
        products = read_sql('products.db')
    else:
        error = 'Wrong source'

    if not error and product_id is not None:
        filtered = [p for p in products if p["id"] == product_id]
        if not filtered:
            error = "Product not found"
        else:
            products = filtered

    return render_template('product_display.html', products=products, error=error)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
