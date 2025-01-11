# 1. Дано число n. Создайте список от n до 0.

n = int(input())
new_list = []
for i in range(n, -1, -1):
    new_list.append(i)
print(new_list)
