maths = int(input("Enter your maths marks: "))
science = int(input("Enter your science marks: "))
english = int(input("Enter your english marks: "))
total = maths + science + english
percentage = (total/300)*100

if percentage>=80:
    print("You got A grade")
elif percentage>=60:
    print("You got B grade")
elif percentage>=40:
    print("You got C grade")
else:
    print("You Failed!")