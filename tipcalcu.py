print("Welcome to the tip calculator")
bill=int(input("What was the total bill? $ "))
tip=int(input("How much tip would you like to give? 10, 12, 13 "))
split=int(input("How many people to split the bill?"))

x=float(bill/split)

print(f"Each person should pay : ${x}")

