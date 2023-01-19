import file_utility
import report_1
import report_2
import report_3



def run(customers, products, orders):
    sum_cost = report_1.sumCost(orders, products)
    prod1 = file_utility.write_to_csv(sum_cost, "order_prices.csv", "id, total")
    product_customer = report_2.product_customers(orders)
    prod2 = file_utility.write_to_csv(product_customer, "product_customers.csv", "id, customer_ids")
    buys = report_3.prod_customer(orders)
    total_custo = report_3.total_customer(buys, products)
    result_dict = report_3.ord_total(total_custo)
    ranking = report_3.build_lines(result_dict, customers)
    prod3 = file_utility.write_to_csv(ranking, "customer_ranking.csv", "id, name, lastname, total")
    return prod1, prod2, prod3
