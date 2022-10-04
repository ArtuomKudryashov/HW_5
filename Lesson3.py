
# Create list
# l=[];
# print(l)
# sentence ="What a wonderful life!"
#
# my_list = list(sentence)
# print(my_list)
#
# my_list1=sentence.split(' ')
# print(my_list1)
# print(my_list1[-1])
# print(my_list1[0])
# x=6
# if x > 5:
#     print ("Ок")
# elif x<5:
#     print('меньше 5')
# else:
#     print('Five')
#
#
# i=1
# while (i<5):
#     print("hi")
#     i=i+1;
#
# # u=1;
# # while u<8:
# #     if u==4:
# #         continue
# #     print(u, 'Hello')
# #     u = u + 1
# u = 1
# while u < 8:
#     u += 1
#     if u == 4:
#         continue
#     print(u, 'Hello')
#
# for i in range (5):
#     print(i,'Hello!')
# #boolean
# name=""
# print(bool(name))
# name=1
# print(bool(name))
# #Функции
# def give_me_power(num,n):
#     return num**n
# print(give_me_power(5,3))
# g=give_me_power(5,6)
# print(g)
# # string =input("Enter word: ")
# # for letter in string:
# #     # print(letter)
# #     print(letter,end=" ")
# a=17
# if a %2 ==0:
#     print("Четное")
# else:
#     print("Не четное ")
x=int(input("Enter year: "))

if(x%4==0 and x%100!=0):
    print("visokosniy")

elif(x%400==0):
    print("Vis")

else:
    print ("Ne")