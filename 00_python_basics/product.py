class product : 

    def __init__(self, product_name,product_price):
        self.product_name = product_name
        self.product_price = product_price
        
    def get_name(self):
        return self.product_name
    
    def set_name(self, name):
        self.product_name = name
        
    p1 = product(product_name="Laptop", product_price=258369)
    print(p1.product_price)
    print(p1.get_name())
    p1.set_name("Desktop")
    print(p1.get_name())
    print(p1.product_price)
    
    p2 = product(product_name="Mobile", product_price=25836)
    
    
    
public
    
    