a=1
b=2

if a==1 and b==2:
    print("Both conditions are true")
else:
    print("At least one condition is false")

def check_conditions(x, y):
    if x > 0 and y > 0:
        return "Both numbers are positive"
    elif x < 0 and y < 0:
        return "Both numbers are negative"
    else:
        return "One number is positive and the other is negative"
