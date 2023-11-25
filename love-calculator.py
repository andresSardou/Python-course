print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name_lower1 = name1.lower()
name_lower2 = name2.lower()
both_names = name_lower1 + name_lower2

t = both_names.count("t") 
r = both_names.count("r")
u = both_names.count("u")
e = both_names.count("e")
first_digit = t + r + u + e

l = both_names.count("l")
o = both_names.count("o")
v = both_names.count("v")
e = both_names.count("e")
second_digit = l + o + v + e

total = int(str(first_digit) + str(second_digit))
if (total < 10) and (total > 90):
  print(f"Your score is {total}, you go together like coke and mentos")
elif (total > 40) and (total < 50):
  print(f"Your score is {total}, you are alright together.")
else:
  print(f"Your score is {total}")
