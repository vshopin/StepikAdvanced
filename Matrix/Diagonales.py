"""
Дана квадратная матрица чисел. Напишите программу, которая меняет местами элементы, стоящие на главной и побочной
диагонали, при этом каждый элемент должен остаться в том же столбце (то есть в каждом столбце нужно поменять местами
элемент на главной диагонали и на побочной диагонали).
Формат входных данных:
На вход программе подаётся натуральное число n
n — количество строк и столбцов в матрице, затем элементы матрицы построчно через пробел.
Формат выходных данных:
Программа должна вывести матрицу с элементами главной и побочной диагонали, поменявшимися своими местами.
"""

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if (i == j) or (i == n - 1 - j):
            print(matrix[n - 1 - i][j], end=' ')
        else:
            print(matrix[i][j], end=' ')
    print()
