n = int(input("Введите число: "))

list = []

for i in range (1, n + 1):
    if i % 2 != 0:
        list.append(i)
print("Список из нечётных чисел от одного до N:", list)
