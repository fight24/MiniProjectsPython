# input
# Mở tệp ở chế độ đọc
with open('/100DaysPython/input.txt', 'r', encoding='utf-8') as file:
    # Đọc toàn bộ nội dung của tệp
    content = file.read()

# student_scores = input().split()
student_scores = content.split()
print(student_scores)
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
max_height = 0
for i in student_scores:
    if max_height < i:
        max_height = i
print(f"The highest score in the class is: {max_height}")