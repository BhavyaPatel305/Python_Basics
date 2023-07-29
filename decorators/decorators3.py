def user(func):
    def inner(age):
        if age < 18:
            print("You are not eligible to login")
            return 
        else:
            return func(age)
    return inner

@user
def aged(age):
    print("You are eligible to login.")
    
aged(20)