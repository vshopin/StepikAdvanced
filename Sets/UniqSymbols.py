"""
Напишите программу для вывода количества уникальных символов каждого считанного слова без учета регистра.
Формат входных данных:
На вход программе в первой строке подается число n – общее количество слов. Далее идут n строк с словами.
Формат выходных данных:
Программа должна вывести на отдельной строке количество уникальных символов для каждого слова.
"""

my_list = [print(len(set(input().lower()))) for _ in range(int(input()))]


