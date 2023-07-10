"""
Тимур записал телефоны всех своих друзей, чтобы автоматизировать поиск нужного номера. 
У каждого из друзей Тимура может быть один или более телефонных номеров. Напишите программу, которая поможет Тимуру находить все номера определённого друга.
Формат входных данных
В первой строке задано одно целое число n — количество номеров телефонов, информацию о которых Тимур сохранил в телефонной книге. В следующих 
n строках заданы телефоны и имена их владельцев через пробел. В следующей строке записано целое число m — количество поисковых запросов от Тимура. В следующих 
m строках записаны сами запросы, по одному на строке. Каждый запрос — это имя друга, чьи телефоны Тимур хочет найти.
Формат выходных данных
Для каждого запроса от Тимура выведите в отдельной строке все телефоны, принадлежащие человеку с этим именем (независимо от регистра имени). Если в телефонной книге нет телефонов человека с таким именем, выведите в соответствующей строке «абонент не найден» (без кавычек).
Примечание 1. Телефоны одного человека выводите в одну строку через пробел в том порядке, в каком они были заданы во входных данных.
Примечание 2. Количество строк в ответе должно быть равно числу m.
Примечание 3. Телефон — это несколько цифр, записанных подряд, а имя может состоять из букв русского или английского алфавита. Записи не повторяются.
"""
phone_book_dict = {}
for i in range(int(input())):
    value, key = input().split()
    if key.lower() in phone_book_dict:
        phone_book_dict[key.lower()].append(value)
    else:
        phone_book_dict[key.lower()] = [value]

for j in range(int(input())):
    name = input().lower()
    if name in phone_book_dict:
        print(*phone_book_dict[name])
    else:
        print('абонент не найден')
