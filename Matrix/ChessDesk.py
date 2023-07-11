"""
На вход программе подаются два натуральных числа n и m. Напишите программу для создания матрицы размером ×n×m, заполнив её символами. и * в шахматном порядке. 
В левом верхнем углу должна стоять точка. Выведите полученную матрицу на экран, разделяя элементы пробелами.
Формат входных данных:
На вход программе на одной строке подаются два натуральных числа n и m — количество строк и столбцов в матрице.
Формат выходных данных:
Программа должна вывести матрицу, описанную в условии задачи.
"""

n, m = map(int, input().split())

for i in range(n):
    print(' '.join(['.' if (i + j) % 2 == 0 else '*' for j in range(m)]))