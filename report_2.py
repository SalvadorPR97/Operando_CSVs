# El equipo de marketing quiere saber que clientes han comprado cada producto. 
# Debe generar un fichero llamado “product_customers.csv” con las siguientes columnas: 
# id: ID del producto
# customer_ids: Lista de todos los ID’s que han comprado ese producto (Separados por un espacio)
# Las columnas deben ir correctamente identificadas con el nombre de cada columna en la primera fila de los ficheros.


def product_customers(orders):
    result_dict = {}
    lines = []
    for o in orders.values():
        for e in o["products"]:
            if e not in result_dict.keys():
                result_dict[e] = []
            result_dict[e].append(o["customer"])
    for key in result_dict:
        lines.append(key + "," + " ".join(result_dict[key]))
    return lines