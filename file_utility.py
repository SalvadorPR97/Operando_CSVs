import csv
import os

if os.path.exists("csv/customers.csv"):
    csv_customers = "csv/customers.csv"
else:
    print("Introduzca ruta absoluta del fichero customers.csv")
    csv_customers = input()
    
if os.path.exists("csv/products.csv"):
    csv_products = "csv/products.csv"
else:
    print("Introduzca ruta absoluta del fichero products.csv")
    csv_products = input()
    
if os.path.exists("csv/orders.csv"):
    csv_orders = "csv/orders.csv"
else:
    print("Introduzca ruta absoluta del fichero orders.csv")
    csv_orders = input()

def load_csv():
    customers = {}
    products = {}
    orders = {}
    
    with open(csv_customers) as f:
        reader = csv.DictReader(f)
        for row in reader:
            val = {
                "firstname" : row["firstname"],
                "lastname" : row["lastname"]
            }
            customers[int(row["id"])] = val 
    
    with open(csv_products) as g:
        reader = csv.DictReader(g)
        for row in reader:
            val = {
                "name" : row["name"],
                "cost" : float(row["cost"])
            }
            products[row["id"]] = val 
        
    with open(csv_orders) as h:
        reader = csv.DictReader(h)

        for row in reader:
            val = {
                "customer" : row["customer"],
                "products" : row["products"].split(" ")
            }
            orders[row["id"]] = val 
    return customers, products, orders


def write_to_csv(lines, file, header):
    with open(file, "w") as f:
        f.write(header + "\n")
        for line in lines:
            f.write(line + "\n")
            