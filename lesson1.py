message = "Hello "
print(message);
user_name= input ('Enter you name: ')
age =int(input('Enter your age '))
date_of_birthday=int(input('Enter your birthday year ' ));
current_age=2022-date_of_birthday;

print('your age is ' +str(current_age))
print(f'{message}{user_name}. You age is {current_age}');


# print(message + user_name);
# # print('Your age  ' + age);

# print('your age is ' +str(current_age));

name ="Art";
print("Age "+str(message))
#"slicing
a="ABCDEFGHJKLMNQiSRT"
# print (a[5:])
# print (a[5:8])
print (a[5:8:2])
# print (a[5:20:2])
# print (a[0:8:2])
# print (a[::2])
# print (a[:10:-2])
# print (a[20:10:-2])
# print (a[-5:10:-2])
# print (a[10::-2])
"""Slice"""
# x=slice(2)
# print(a[x])
# w=slice(-3)
# print(a[w])
e = slice(-3, -1)
print(a[e])
r= slice(-10, -20,-1)
print(a[r])
i= slice(100, -20,-1)
print(a[i])
a=range(3,7,1)
for x in a:
    print(x)

