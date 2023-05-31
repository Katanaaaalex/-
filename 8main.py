# Задача 18: Требуется найти в массиве A[1..N] самый близкий 
# по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число 
# N – количество элементов в массиве. В последующих  
# строках записаны N целых чисел Ai. 
# Последняя строка содержит число X

# 1 способ
n = int(input("Введите количество элементов в массиве: "))
a = []
for i in range(n):
    a.append(int(input("Введите элемент массива: ")))
x = int(input("Введите число X: "))
b = abs(x - a[0])
num = a[0]
for i in range(1, len(a)):
    if b > abs(x - a[i]):
        b = abs(a[i] - x)
        num = a[i]
print("Число", num, "самый близкий по величине элемент к заданному числу X")

# 2 способ
import random
n = int(input("Введите количество элементов в массиве: "))
a = []
for i in range(n):
    a.append(random.randint(0, 100))
print(a)
x = int(input("Введите число X: "))
b = abs(x - a[0])
num = a[0]
for i in range(1, len(a)):
    if b > abs(x - a[i]):
        b = abs(a[i] - x)
        num = a[i]
print("Число", num, "самый близкий по величине элемент к заданному числу X")