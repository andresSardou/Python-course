#This is a program used to calculate tip when splitting the bill

print("Welcome to the Tip calculator")
bill = input("What is the total bill? $")
tip = input("What is the percent tip you would like to use? 10, 12, or 15? ")
people = input("How many people will be splitting the bill? ")

percent_tip = (int(tip) / 100 + 1)
final_bill = round((float(bill) / int(people)) * percent_tip, 2)
print(f"Each person should pay: ${final_bill}")