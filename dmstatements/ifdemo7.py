print("Press 1 to order a pizza")
print("Press 0 to cancel order")
inp1 = int(input("Enter either 0 or 1"))

if inp1 == 0:
    print("Order cancelled")
elif inp1 == 1:
    print("Press 1 to get cheese pizza")
    print("Press 2 to get a burger")
    inp2 = int(input("Enter either 1 or 2"))
    
    if inp2 == 1:
        print("Press 1 to get thin crust pizza")
        print("Press 2 to get thick crust")
        print("Press 3 to get normal crust")
        
        inp3 = int(input("Enter either 1 or 2 or 3"))
        
        if inp3 == 1:
            print("You have ordered a thin crust cheese pizza")
        elif inp3 == 2:
            print("You have ordered a thick crust cheese pizza")
        elif inp3 == 3:
            print("You have ordered a normal crust cheese pizza")
        else:
            print("Invalid input")
    elif inp2 == 2:
        print("press 1 to get a vegetable burger")
        print("press 2 to get a pork burger")
        print("press 3 to get a chicken burger")
        
        inp4 = int(input("Enter either 1 or 2 or 3"))
        
        if inp4 == 1:
            print("You have ordered a vegetable burger")
        elif inp4 == 2:
            print("You have ordered a pork burger")
        elif inp4 == 3:
            print("You have ordered a chicken burger")
        else:
            print("Invalid input")
    else:
        print("Invalid input")
else:
    print("Invalid input")
        
    