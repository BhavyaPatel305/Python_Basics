def divide(func):
    
    #func = division
    def inner(a,b):
        print("I am going to divide", a , "and", b)
        if b == 0:
            print("Whoops! cannot login")
            return
        
    return inner

@divide
def division(a,b):
    print("...")
    return a/b

x = division(100,2)
print(x)