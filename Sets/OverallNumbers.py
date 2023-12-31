"""
На вход программе подается натуральное число n, а затем n различных натуральных чисел, каждое на отдельной строке.
Напишите программу, которая выводит все общие цифры в порядке возрастания у всех введенных чисел.
Формат входных данных:
На вход программе подаются натуральное число n≥1, а затем n различных натуральных чисел, каждое на отдельной строке.
Формат выходных данных:
Программа должна вывести цифры в соответствии с условием задачи. Если общих цифр нет, то ничего выводить не нужно.
"""

my_list = [set(input()) for _ in range(int(input()))]
print(*sorted(set.intersection(*my_list)))
