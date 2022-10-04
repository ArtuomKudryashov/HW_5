list_1=[1,20,333,-4,50,6,50,20]
print(list_1)

# letters = ('apple', ['ananas', 'mango'], 'melon')
# letters[1][0] = 'cherry'
# print(letters)
# list=list(letters)
# print(list)
# tuple=tuple(list)
# print(tuple)



# list_1=list(set(list_1))
# print(list_1)

print("Перевод  в Dictionary")
dict_1= {}

print("Прогоняем форлупом")

for index in  range(len (list_1)):
    dict_1[index]=list_1[index]
print(dict_1)


a="You are welcome"
for letter_index in  range(len(a)):
    print(letter_index,end=" ")


print(dict_1)
print(dict_1.keys())
print(dict_1.values())
print(dict_1.items())

for ind, val in enumerate (dict_1.items(),2):
    print(f' {ind}------->{val}')

print(dict_1.get(1))