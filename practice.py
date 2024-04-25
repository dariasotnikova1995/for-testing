# 1 Выведите все элементы, которые меньше 5
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for i in a:
    if i < 5:
        print(i)

# 2 (variant1) вернуть список, который состоит из элементов, общих для этих двух списков
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []
for i in a:
    for j in b:
        if i == j:
            c.append(i)
            break
print(c)

# 2 (variant2)
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
result = list(filter(lambda elem: elem in b, a))
print(result)

# 3 oтсортируйте словарь по значению в порядке возрастания и убывания
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
sorted_number = sorted(d.items(), key=lambda item: item[1])
sorted_number1 = sorted(d.items(), key=lambda item: item[1], reverse=True)
print(sorted_number)
print(sorted_number1)

# 4 слияния нескольких словарей
dict_a = {1: 10, 2: 20}
dict_b = {3:  30, 4: 40}
dict_c = {5: 50, 6: 60}
merged_dictionary = {**dict_a, **dict_b, **dict_c}
print(merged_dictionary)

# 5 Найдите три ключа с самыми высокими значениями в словаре
my_dict = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20}
result = sorted(my_dict, key=my_dict.get, reverse=True)[:3]
print(result)
print(sorted(my_dict.values())[-3:])

# 6 Tреугольника Паскаля
def pascal_triangle(rows):
    row = [1]
    for i in range(rows):
        print(row)
        row = [sum(x) for x in zip([0]+row, row+[0])]
pascal_triangle(6)

# 7 Квадрат
a = int(input("Enter the height of the square: "))
symbol = input("Enter symbol to build square with: ")
for i in range(a):
    for j in range(a):
        print(symbol, end=' ')
    print()

