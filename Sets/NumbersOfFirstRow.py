"""На вход программе подаются две строки текста, содержащие числа. Напишите программу, которая выводит все числа в
порядке возрастания, которые есть в первой строке, но отсутствуют во второй.
Формат входных данных:
На вход программе подаются две строки текста, содержащие числа, отделенные символом пробела.
Формат выходных данных:
Программа должна вывести множество чисел, встречающихся только в первой строке.
"""

set1 = set(int(i) for i in input().split())
set2 = set(int(i) for i in input().split())

print(*sorted(list(set1.difference(set2))))