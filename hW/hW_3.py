# Дан список my_list = ['a', 'b', [1, 2, 3], 'd'].
# Распечатайте значения 1, 2, 3
# my_list = ['a', 'b', [1, 2, 3], 'd']
# print(my_list[2][0])
# print(my_list[2][1])
# print(my_list[2][2])
#
# list1 = my_list[2]
# print(*list1, sep='\n')
# #3.2 Дан список list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
#    # - получите сумму всех чисел,
#    # - распечатайте все строки, где есть буква 'a'
# list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
# #Using lambda and filter
# print(sum(filter(lambda x: isinstance(x, int), list_1)))
# #Using list comprehension
# print([x for x in list_1 if isinstance(x, str) and 'a' in x])
# # 3.3. Превратите лист ['cat', 'dog', 'horse, 'cow'] в кортеж
#
# list2=['cat', 'dog', 'horse', 'cow']
# print(tuple(['cat', 'dog', 'horse', 'cow']))
# 3.4. Напишите программу, которая определяет, какая семья больше.
#       1) Программа имеет два input() - например, family_1, family_2.
#       2) Членов семьи нужно перечислить через запятую.
#      Ожидаемый результат - программа выводит семью с бОльшим составом. Если состав одинаковый, print("Equal')
# family_1 = tuple(input('Введите текст через запятую: ').split(','))
# family_2 = tuple(input('Введите текст через запятую: ').split(','))
# if len(family_1) == len(family_2):
#     print('Equal')
# elif len(family_1) > len(family_2):
#     print('family_1')
# else:
#     print('family_2')
# 3.5. Создайте словарь film c ключами title, director, year, budget, main_actor, slogan. В значения можете передать информацию
#     о вашем любимом фильме.
#     - распечатайте только ключи
#     - распечатайте только значения
    # - распечатайте пары ключ - значение
# Film= {
#     'title': 'Thriller',
#     'director': 'Christopher Nolan',
#     'year': 2008,
#     'budget': 185000000,
#     'main_actor':"Heath Ledger",
#     'slogan':"What dosnt kill us, make us stranger"
# }
# print(Film)
# print(id(Film))
# print(Film.keys())
# print(Film.values())
# print(Film.items())
# 3.6. Найдите сумму всех значений в словаре
# my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
# result= 0
# for x in my_dictionary:
#     result+=my_dictionary[x]
# print(result)
# # Option 2
# my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
# print(sum(my_dictionary.values()))
# # 3.7. Удалите повторяющиеся значения из списка
# new_list=[1, 2, 3, 4, 5, 3, 2, 1]
# new_list2=set([1, 2, 3, 4, 5, 3, 2, 1])
#
# print(new_list2)
# 3.8. Даны два множества: set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}, set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
#      - найдите значения, которые встречаются в обоих множествах
#      - найдите значения, которые не встречаются в обоих множествах
     # - проверьте являются ли эти множества подмножествами друг друга
set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}
set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
print("3.8888")

print(set2.intersection(set1))
print(set2.difference(set1))

print(set1.issubset(set2))
print(set2.issubset(set1))