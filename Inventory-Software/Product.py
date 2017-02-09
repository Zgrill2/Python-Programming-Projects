class Product:
    def __init__(self, id, description, price=0.0):
        self.id = id
        self.description = description
        self.price = price

    def print_product(self):
        print "$$$$$ product_%d:%s:$%.2f $$$$$" % (self.id,self.description,self.price)