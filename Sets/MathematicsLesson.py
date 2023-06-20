"""
Даны оценки по математике трёх учеников в 10-балльной шкале. Напишите программу, которая выводит такие оценки,
которые встречаются не более, чем у двух учеников.
Формат входных данных
На вход программе подаются оценки трех учеников, разделенные символом пробела (оценки каждого ученика на отдельной строке).
Формат выходных данных
Программа должна вывести множество оценок в порядке возрастания на одной строке, разделенных пробелами, в соответствии с условием задачи.
Примечание. Оценка ученика находится в диапазоне от 0 до 10 включительно.
"""
num1 = set(int(i) for i in input().split())
num2 = set(int(i) for i in input().split())
num3 = set(int(i) for i in input().split())

set1 = num1.intersection(num2).intersection(num3)
set2 = num1.union(num2).union(num3)
set3 = set2.difference(set1)

print(*sorted(set3))