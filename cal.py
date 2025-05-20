

print("THIS CALCULATOR MADE WITH PYTHON")


print("Please choose a following option,\n")

print("1-Square\n2-Circle\n3-Triangle\n")
select = int(input("Choose one option : "))
while select < 1 or select > 3:
    print("Please select from 1,2,3 ")
    select = int(input("choose one option : "))



if select == 1:
    print("You choosed Square ")
    height = float(input("Enter height : "))
    length = float(input("Enter the length : "))

    result = height*length

    print(f"The area is :{result}")

if select == 2:
    print("You choosed Circle,")
    radius = float(input("Enter the radius : "))

    result = 3.1472*radius*radius

    print(f"The area is : {result}")

if select == 3:
    print("You choosed Triangle,")
    base = float(input("Enter the length nof the base : "))
    height1 = float(input("Enter the height of triangle : "))

    result = base*height1/2

    print(f"The area is : {result}")
    
