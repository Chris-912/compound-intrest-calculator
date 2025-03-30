#compound intrest calculator(time in years)
principle = 0
rate = 100
time = 0
principle = float(input("Enter principle "))
rate = float(input("Enter rate " ))
time = float(input("Enter time "))

if principle<=0 or rate >=0 or time <=0:
    print("invalid input Answer Wrong ")
else:
    print("Amount")
total = principle * (1+rate/100)**time
print(f"${total}")





























