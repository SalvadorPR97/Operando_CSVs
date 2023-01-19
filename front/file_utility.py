import csv


def load_csv(csv_customers, csv_products, csv_orders):
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
            