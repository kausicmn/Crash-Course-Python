class product:
    def __init__(self,value):
        self.price=value
    
    @property
    def price(self):
        return self.__value
    
    @price.setter
    def price(self,valuee):
        if valuee<0:
            raise ValueError("error")
        self.__value=valuee
    #price=property(get_price,set_price)
Product=product(50)
print(Product.price)