# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
# Write your code below this row 👇
sum = 0
for i in student_heights:
  sum+=i
num_of_student = len(student_heights)
average_height = round(sum/len(student_heights))
print(f"total height = {sum}\nnumber of students = {num_of_student}\naverage height = {average_height}")

