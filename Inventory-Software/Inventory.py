from collections import defaultdict  # this solves potential problems down the road with erroneous key calls
from Product import Product

class Inventory:
    def __init__(self, name):
        self.name = name
        self.p = Product(0,"error")
        self.products_list = {}
        self.products_list = defaultdict(lambda:[Product(0,"error"),0],self.products_list)

    def add_product(self, product_to_add):

        if self.products_list[product_to_add.id][1] == 0:
            print "DEBUG: new product added"
            self.products_list[product_to_add.id][0] = product_to_add
            self.products_list[product_to_add.id][1] = 1
        else:
            self.products_list[product_to_add.id][1] += 1

    def print_name(self):
        return "##########\n%s\n##########" % self.name