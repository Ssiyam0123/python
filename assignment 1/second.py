num1 = float(input("Enter the first number : "))
operator = str(input("Select any operation, =,-,*,/ : "))
num2 = int(input("Enter the second number : "))

if operator == "+" : print("Result :",num1+num2)
elif operator == "-" : print("Result :",num1-num2)
elif operator == "*" : print("Result :",num1*num2)
elif operator == "/" : print("Result :",num1/num2)
else : print("invalid operation")
