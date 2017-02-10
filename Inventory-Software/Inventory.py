from collections import defaultdict  # this solves potential problems down the road with erroneous key calls
from Product import Product


class Inventory:
    def __init__(self, name):
        self.name = name
        self.p = Product(0,"error")
        self.products_list = {}
        self.products_list = defaultdict(lambda: [Product(0, "error"), 0], self.products_list)

    def add_product(self, product_to_add):

        if self.products_list[product_to_add.id][1] == 0:
            print "DEBUG: new product added"
            self.products_list[product_to_add.id][0] = product_to_add
            self.products_list[product_to_add.id][1] = 1
        else:
            self.products_list[product_to_add.id][1] += 1

    def print_name(self):
        return "##########\n%s\n##########" % self.name


def create_master_list(inventory_list):
    master_list = {}
    master_list = defaultdict(lambda: [Product(0, "error"),0], master_list)
    for i in inventory_list:
        if i is not Inventory:
            continue
        for key in i.products_list:
            try:
                if master_list[i.products_list[key].id][1] == 0:  # if product not in master list
                    master_list[i.products_list[key].id][1] = 1
                    master_list[i.products_list[key].id][0] = i.products_list[key][0]
                else:
                    master_list[i.products_list[key].id][1] += 1
            except:
                master_list[i.products_list[key].id][1] = 1
                master_list[i.products_list[key].id][0] += 1
    return master_list
