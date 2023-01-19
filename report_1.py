# El equipo de ventas quiere saber el total de cada pedido. Debe generar un fichero llamado “order_prices.csv” con las siguientes columnas:
# id: ID del pedido
# total: Total del pedido en euros
# Las columnas deben ir correctamente identificadas con el nombre de cada columna en la primera fila de los ficheros.


def sumCost(orders, products):
    lines = []
    for ord in orders:
        sum = 0
        order = orders[ord]
        for prod in order["products"]:
            sum += products[prod]["cost"]
        lines.append(ord + "," + str(sum))
    return lines

