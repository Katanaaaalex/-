# Задача 30:  Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
n = int(input("Введите количество элементов в массиве: ")) 
array = []
a1 = int(input("Введите первый элемент массива: ")) 
d = int(input("Введите разность элементов: ")) 
array = [a1 + (i - 1) * d for i in range(1, n + 1)]
print((array))