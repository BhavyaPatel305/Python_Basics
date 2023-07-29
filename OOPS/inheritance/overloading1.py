from multipledispatch import dispatch

class Amazon():
    
    @dispatch(str)
    def product(self, pname):
        print("product called with product name", pname)
        
    @dispatch(str, int)
    def product(self, pname1, price):
        print("product called with product name and price", pname, price)
        
    @dispatch(str, int)
    def product(self, n, p):
        print("product called with product name and price...", n, p)
        
    @dispatch(int, str)
    def price(self, price, pname):
        print("product called with price and pname", price, pname)
        
    @dispatch(int)
    def product(self, price):
        print("product called int price", price)
        
    @dispatch(float)
    def product(self, price):
        print("product called float price", price)
        
a = Amazon()

#a.product("mobile")        
a.product("mobile",1000)
#a.product(1000,"mobile")
a.product(1000)
a.product(1000.0)
