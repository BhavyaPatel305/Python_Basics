def decorator_message(fun):
    print(fun)
    def addWelcomeGreet(sitename):
        return "Welcome to " + fun(sitename)
    
    return addWelcomeGreet

@decorator_message
def site(site_name):
    return site_name

print(site("WWW.google.com"))