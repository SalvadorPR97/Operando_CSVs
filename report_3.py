#  Para evaluar a los clientes, necesitamos un fichero que contenga todos los pedidos ordenados descendentemente por el total en euros:
# Debe generar un fichero llamado “customer_ranking.csv" con las siguientes columnas: 
# id: ID del cliente
# name: Nombre del cliente
# lastname: Apellidos del cliente
# total: Total en euros que el cliente ha comprado en productos.
# Las columnas deben ir correctamente identificadas con el nombre de cada columna en la primera fila de los ficheros.

def prod_customer(orders):
    custo_produc_dict = {}
    for o in orders:
        order = orders[o]
        if order['customer'] not in custo_produc_dict.keys():
            custo_produc_dict[order["customer"]] = []
        for element in order["products"]:
            custo_produc_dict[order["customer"]].append(element)
    custo_produc_dict = {int(k): v for k,v in custo_produc_dict.items()}
    return custo_produc_dict


def total_customer(buy, products):
    new_dict = {}
    for c in buy:
        sum = 0
        for product in buy[c]:
            sum += products[product]["cost"]
        new_dict[c] = sum
    return new_dict
    

def ord_total(total):
    sort_dict = dict(sorted(total.items(), key=lambda item: item[1], reverse=True))
    return sort_dict


def build_lines(result, customers):
    lines = []
    for i in result:
        lines.append(str(i) + "," + customers[i]["firstname"] + "," + customers[i]["lastname"] + "," + str(result[i]))
    return lines
