print("Calculator")
print("Press '1' to do Addition . Press '2' to do Subtraction . Press '3' to Multiply . Press '4' to Divide .")

Choice =   input("Choose what you want to do ")
num1   =   input("Enter The First Number - ")
num2   =   input("Enter The Second Number - ")

Add = (num1 + num2)
Subtract =(num1 - num2)
Multiply = (num1 * num2)
Divide = (num1 / num2)

if Choice == 1:
    print("The Added Number is ", Add)
else Choice == 2:
    print("The Subtracted Number is ",Subtract)
else Choice == 3:
    print("Your Multiplied Number is ",Multiply)
else Choice == 4:
    print("Your Divided Number is ",Divide)
else:
    print("The Operation is invalid")    