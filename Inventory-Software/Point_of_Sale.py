from Inventory import Inventory
import sys


class PointOfSale:
    def __init__(self, inventory_list):
        for i in inventory_list:
            if i is not Inventory:
                sys.exit(0)
        self.inventories = inventory_list
        self.current_sale = []
        self.master_sale_list = []
        self.master_product_list = Inventory.create_master_list(self.inventories)

    def pretend_to_process_payment(self):
        pass

    def get_product(self, id):
        return self.mlist[id][0], self.mlist[id][1]  # return tuple of product and quantity

    def add_to_sale(self, id):
        self.current_sale.append(self.get_product(id))

    def remove_from_sale(self, id):
        for sale_index in range(len(self.current_sale)):
            if self.current_sale[sale_index][1].id == id:
                del self.current_sale[sale_index]
                break

    def complete_sale(self, id, quantity):
        prod_for_sale = self.get_product(id)
        if quantity <= 0:
            return "Error: please request a quantity greater than 0"
        if prod_for_sale[1] <= quantity:
            self.pretend_to_process_payment()
            self.master_sale_list.append(self.current_sale)
            self.current_sale = []
            return "Sale complete"
        else:
            return "Error: currently in stock %d" % prod_for_sale[1]

