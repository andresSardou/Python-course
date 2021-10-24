# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆hig

sum_of_students = 0
number_of_students = 0
for height in student_heights:
    sum_of_students += height
    number_of_students += 1

average = sum_of_students / number_of_students
print(round(average))

# Write your code below this row 👇
