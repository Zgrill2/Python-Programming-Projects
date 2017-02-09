#!/usr/bin/python

from Inventory import Inventory
from Product import Product

import random

if __name__ == "__main__":
    i = []
    p = []
    for f in range(10):
        i.append(Inventory("inventory_%d" % f))
        p.append(Product(random.randint(0,100),("product_%d" % f),(random.random()*100.0)))

    for inv in i:
        pr = inv.print_name()
        for prod in p:
            if random.random() < .5:
                inv.add_product(prod)  # adds products with a 50% chance
                print "products added\n%s" % pr

        for key in inv.products_list:
            inv.products_list[key][0].print_product()
