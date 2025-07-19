import sys
age=int(input("Enter age:"))
if age<18:
    print("You are a minor-- you are not eligible")
    sys.exit()
print("you are eligible---------")