for number in range(1, 10):
    print(number)

# The forloop and range function wont include the number 10
# You need to write it like this if you want to include the number 10.

for number in range(1, 11):
    print(number)

# To count and skip by a number

for number in range(1, 11, 3):
    print(number)

# to count to 100 and add the number to the next one

total = 0

for number in range(1, 101):
    total += number

print(total)

# practice exercise 1: adding all the even numbers

total_exercise = 0

for number in range(2, 101, 2):
    total_exercise += number

print(total_exercise)

input("What is your name?")
