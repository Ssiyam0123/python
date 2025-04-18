def calc (num1, num2, operation):
    if operation == "+":
        return num1+num2
    
    elif operation == "-":
        return num1-num2
    
    elif operation =="*":
        return num1*num2
    
    elif operation == "/":
        return num1/ num2
    
    

in1 = float(input("enter your first number :"))

in2 = float(input("enter your second number :"))

opera = input("Please select operation (+, -, *, /) : ")


result = calc(num1=in1, num2=in2, operation=opera)


print("Result : ", result)    