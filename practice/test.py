def hourToMinConverter(hour):
    return hour*60

userHour = float(input("Enter hour : "))
 
convertedMin = hourToMinConverter(userHour)

print("hour to min : ",convertedMin) 