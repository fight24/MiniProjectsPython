# Mở tệp ở chế độ đọc
with open('/100DaysPython/input.txt', 'r', encoding='utf-8') as file:
    # Đọc toàn bộ nội dung của tệp
    content = file.read()

# In nội dung
print(content)