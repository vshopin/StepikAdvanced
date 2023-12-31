"""
Даны по 10-балльной шкале оценки по информатике трех учеников. Напишите программу, которая выводит множество оценок,
которые есть и у первого и у второго учеников, но которых нет у третьего ученика.
Формат входных данных:
На вход программе подаются оценки трех учеников, разделенные символом пробела (оценки каждого ученика на отдельной строке).
Формат выходных данных:
Программа должна вывести множество оценок в порядке убывания на одной строке, разделенных пробелами, в соответствии с условием задачи.
Примечание. Оценка ученика находится в диапазоне от 0 до 10 включительно.
"""
num1 = set(int(i) for i in input().split())
num2 = set(int(i) for i in input().split())
num3 = set(int(i) for i in input().split())

print(*sorted(num1.intersection(num2).difference(num3), reverse=True))
