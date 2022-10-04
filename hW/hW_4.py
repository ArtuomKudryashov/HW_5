from math import sqrt
from functools import reduce
def square(side):
  return (side*side, side*4, round(sqrt(side**2*2)))
print(square(5))
# 4.2. Напишите фукнцию, которая принимает произвольное количество именнованных аргументов и выводит их построчно
#      в формате аргумент: значение. Например:
# 	name: John
# 	last_name: Smith
# 	age: 35
	# position: web developer
def employee(**kwargs):
    for k, v in kwargs.items():
        print(f'{k}: {v}')

employee(Caruseli ="caruseli" ,last_name='Popov', name='Max', age=40, position='web developer')
print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<4.3>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
#4.3. Используя лямбда-выражение, из списка
# my_list = [20, -3, 15, 2, -1, -21] с
# оздайте новый список, содержащий только
   #  положительные числа
my_list = [20, -3, 15, 2, -1, -21]
my_list2=(filter(lambda x: x>0,my_list))
print(my_list2)
#Используя лямбда выражение, получите результат
#перемножения значений в предыдущем списке
print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<4.4>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
sum = reduce (lambda x,y: x*y, my_list)
print(sum)
sum_pos = reduce (lambda x,y: x*y, my_list2)
print(sum_pos)


sum_all = reduce(lambda x, y: x * y,[x for x in my_list if x>0])

print(sum_all)
print(reduce(lambda x, y: x*y, [x for x in my_list if x > 0]))
# 4.5. Создайте файл my_calc.py и пропишите в нем минимум 4 функции, выполняющие базовые арифметические вычисления.
#      Примените эти функции в качестве методов в другом файле.
print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<4.5>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
from hW4 import *

prod_res = prod(100, 20)
print(prod_res)

div_res1 = divide(45, 9)
print(div_res1)

div_res2 = divide(5, 0)
print(div_res2)

add_res = add(585, 1987)
print(add_res)

remain_res = remain(541, 6)
print(remain_res)

sub_res = subtract(230, 149)
print(sub_res)


def tests():
    assert prod(100, 20) == 2000, f'Wrong number, actual result is {prod(100, 20)}'
    assert divide(10, 0) == "Can't divide by zero", "Shouldn't divide by zero"
    assert add(5, 8) == 13, f'Wrong number, actual result is {sum(5, 8)}'
    assert remain(9, 4) == 1, f'Wrong number, actual result is {remain(9, 4)}'
    assert subtract(85, 28) == 57, f'Wrong number, actual result is {subtract(85, 28)}'
tests()


