from flask import Flask, render_template, request, send_file
from zipfile import ZipFile
import os 

import file_utility
import csv_builder


app = Flask(__name__)

TMP_ROUTE = "tmp/"
@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/upload", methods= ["GET", "POST"])
def upload():
    if request.method == "POST":
        cust = request.files["uploaded_file"]
        custom_route = os.path.join(TMP_ROUTE, cust.filename)
        cust.save(custom_route)
        prod = request.files["uploaded_file2"]
        product_route = os.path.join(TMP_ROUTE, prod.filename)
        prod.save(product_route)
        ord = request.files["uploaded_file3"]
        order_route = os.path.join(TMP_ROUTE, ord.filename)
        ord.save(order_route)
        
        custom, product, orde = file_utility.load_csv(custom_route, product_route, order_route)
        csv_builder.run(custom, product, orde)
        
        zipObj = ZipFile('result.zip', 'w')
        zipObj.write('customer_ranking.csv')
        zipObj.write('order_prices.csv')
        zipObj.write('product_customers.csv')
        zipObj.close()

        trash = [custom_route, product_route, order_route, 'customer_ranking.csv', 'order_prices.csv', 'product_customers.csv']
        for t in trash:
            os.remove(t)
        
        return send_file('result.zip',
                mimetype = 'zip',
                download_name= 'result.zip',
                as_attachment = True)
    return "/"


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)