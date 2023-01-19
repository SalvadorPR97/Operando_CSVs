import report_1
import report_2
import report_3
import unittest
import file_utility_test

customers, products, orders = file_utility_test.load_csv()


class LineTest(unittest.TestCase):
    def test_load(self):
        test = file_utility_test.load_csv()
        self.assertTrue(test != {})
        
    def test_1(self):
        result = report_1.sumCost(orders, products)
        self.assertEqual(result[0], "0,18.943120182823662")
    
    def test_2(self):
        result2 = report_2.product_customers(orders)
        self.assertEqual(result2[0], "1,0 0 22 22 40 32 32 32 45 45 38 38 51 51 6 44 34 34 3 3 3 50 24 24 15 34 5 5 45 41 47 47 46 46 32 35 29 24 10 17 17 9 22 5 44 44 58")

    def test_3(self):
        buys = report_3.prod_customer(orders)
        total_custo = report_3.total_customer(buys, products)
        result3 = report_3.ord_total(total_custo)
        t = 0
        for k,v in result3.items():
            if t == 0:
                t = v
            self.assertLessEqual(v, t)

if __name__ == "__main__":
    unittest.main()