from Inventory import Inventory
from Product import Product
import sys


class PointOfSale:
    def __init__(self, inventory_list):
        for i in inventory_list:
            if not i is Inventory:
                sys.exit(0)
        self.inventories = inventory_list

    def get_product(self, id):
        Inventory.create_master_list(self.inventories)
