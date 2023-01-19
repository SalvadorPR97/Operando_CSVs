from fastapi import FastAPI
from starlette.responses import RedirectResponse
import file_utility
import csv_builder


app = FastAPI()


HOST = "http://127.0.0.1:8000/"

@app.get("/")
def index():
    return "Hello World"


@app.get("/{customerscsv}/{productscsv}/{orderscsv}")
def download(customerscsv, productscsv, orderscsv):
    customers, products, orders = file_utility.load_csv(customerscsv, productscsv, orderscsv)
    csv_builder.run(customers, products, orders)
    return RedirectResponse(HOST + "download_ready")


@app.get("/download_ready")
def ready():
    return "Your download is ready"
