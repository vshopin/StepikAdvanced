"""
Напишите программу, которая проверяет симметричность квадратной матрицы относительно главной диагонали.
Формат входных данных:
На вход программе подаётся натуральное число n
n — количество строк и столбцов в матрице, затем элементы матрицы построчно через пробел.
Формат выходных данных:
Программа должна вывести YES, если матрица симметрична относительно главной диагонали, и слово NO в противном случае.
"""

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

# Проверяем, что матрица симметрична относительно главной диагонали
for i in range(n):
    for j in range(i, n):
        if matrix[i][j] != matrix[j][i]:
            print("NO")
            exit()

print("YES")
