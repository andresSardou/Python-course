print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L \n").lower()
add_pepperoni = input("Do you want pepperoni? Y or N \n").lower()
extra_cheese = input("Do you want extra cheese? Y or N \n").lower()

#Small Pizza
if size == "s":
  bill = 15
  if add_pepperoni == "y":
    bill += 2
  if extra_cheese == "y":
    bill += 1

#Medium Pizza
if size == "m":
  bill = 20
  if add_pepperoni == "y":
    bill += 3
  if extra_cheese == "y":
    bill +=1

#Large Pizza
if size == "l":
  bill = 25
  if add_pepperoni == "y":
    bill += 3
  if extra_cheese == "y":
    bill += 1

print(f"Your final bill is: ${bill}.")


 

    
 
