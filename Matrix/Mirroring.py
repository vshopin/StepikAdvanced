"""
Дана квадратная матрица чисел. Напишите программу, которая зеркально отображает её элементы относительно горизонтальной оси симметрии.
Формат входных данных:
На вход программе подаётся натуральное число n
n — количество строк и столбцов в матрице, затем элементы матрицы построчно через пробел.
Формат выходных данных:
Программа должна вывести матрицу в которой зеркально отображены элементы относительно горизонтальной оси симметрии.
"""
n = int(input())
matrix = [input().split() for _ in range(n)]

for i in range(n // 2):
    matrix[i], matrix[n - i - 1] = matrix[n - i - 1], matrix[i]
for row in matrix:
    print(*row)
