number = float(input("Enter your mark : "))

if 90 <= number <= 100:
    print("Your grade is : A")

elif 80 <= number <= 89:
    print("Your grade is : B")

elif 70 <= number <= 79:
    print("Your grade is : C")

elif 60 <= number <= 69:
    print("Your grade is : D")

elif 50 <= number <= 59:
    print("Your grade is : E")

elif 40 <= number <= 49:
    print("Your grade is : E-")

elif 0 <= number < 40:
    print("Your grade is : F")

else:
    print("Please enter your mark between 0-100")
