import math
import random
#
# # begin 1
# a = int(input())
# print('P =', 4*a)
#
# # begin 2
# a = int(input())
# print('S =', a**2)
#
# # begin 3
# c = int(input())
# d = int(input())
# print('S =', c*d, 'P =', 2*(c+d))
#
# # begin 4
#
# d = int(input())
# print(3.14*d)
#
# # begin 5
# a = int(input())
# print('V =', a**3, 'S =', 6*a**2)
#
# # begin 6
#
# a = int(input())
# b = int(input())
# c = int(input())
# print('V =', a*b*c, 'S =', 2*(a*b + b*c + a*c))
#
# # begin 7
#
# r = int(input())
# l = 2 * 3.14 * r
# s = 3.14* r**2
# print('L =', s, 'S =', s)
#
# # begin 8
#
# a = int(input())
# b = int(input())
# print((a+b)/2)
#
# # begin 9
#
# a = float(input())
# b = float(input())
# print(a*b)**0.5
#
# # begin 10
#
# a = int(input())
# b = int(input())
# print((a**2 + b **2), (a**2 - b **2), (a**2 * a**2), (a**2 // b**2))
#
# # begin 11
#
# a = int(input())
# b = int(input())
# print(abs(a)+abs(b), abs(a)-abs(b), abs(a)*abs(b), abs(a)/abs(b))
#
# # begin 12
#
# a = float(input())
# b = float(input())
# c = (a**2+b**2)**0.5
# p = a+b+c
# print('c =', c, 'P =', p)
#
# # begin 13
#
# r1, r2 = int(input()), int(input())
# s1 = 3.14*r1**2
# s2 = 3.14*r2**2
# s3 = s1-s2
# print(s1,s2,s3)
#
# # begin 14
#
# n = int(input())
# r = n/2/3.14
# s = 3.14*r**2
# print('R =', r, 'S =', s)
#
# # begin 15
#
# s = int(input())
# r = (3.14/s)**0.5
# dl = 2*3.14*r
# print('D =', r, 'L =', dl)
#
# # begin 16
#
# x1 = int(input())
# x2 = int(input())
# print(x2-x1)
#
# # begin 17
#
# a = int(input())
# b = int(input())
# c = int(input())
# bc = c-b
# ac = bc-a
# print('B - C =', bc, 'A - C =', ac, bc+ac)
#
# # begin 18
#
# a, b, c = int(input()), int(input()), int(input())
# ac = c-a
# bc = b-c
# print(ac*bc)
#
# # begin 19
#
# x1, x2 = int(input()), int(input())
# y1, y2 = int(input()), int(input())
# p = 2*(abs(x1-x2)+abs(y1-y2))
# s = abs(x1-x2)*abs(y1-y2)
# print('P =', p, 'S =', s)
#
# # begin 20
#
# x1, x2 = int(input()), int(input())
# y1, y2 = int(input()), int(input())
# s = ((x2-x1)**2+(y2-y1)**2)**0.5
# print(s)
#
# for i in range(5, 20):
#     print(i)

# for i in range(20, 5, -2):
#     print(i)

# for i in range(-10, 10, 5):
#     print(i)


# i = -10
# while i == 100:
#     print(i)
#     i += 10

# i = 50
# while i > 30:
#     print(i)
#     i -=0.5

# i = 1
# while i < 100:
#     print(i)
#     i *= 2

# a, b = int(input()), int(input())
# count = 0
# for i in range(a, b + 1):
#     count += 1
#     print(i, count)
#
# a, b = int(input()), int(input())
# count = 0
# for i in range(b - 1, a, -1):
#     count += 1
#     print(i, count)
#
# price = int(input())
# for i in range(11):
#     print(i * price)

# price = int(input())
# for i in range(10, 1, -1):
#     print(i / price)

# a, b = int(input()), int(input())
# summa = 0
# for i in range(a, b+1):
#     sum += i
# print(summa)

# a, b = int(input()), int(input())
# multy = 1
# for i in range(a, b + 1):
#     multy *= i
# print(multy)

# a, b = int(input()), int(input())
# summa = 0
# for i in range(a, b + 1):
#     summa += i ** 2
# print(summa)

# print(*[i for i in range(3, 31, 3)])

# x = int(input())
# summa = 0
# for i in range(x):
#     summa += i
# print(summa)

# for 10
# n = int(input())
# summa = 0
# for i in range(1, n):
#     summa += 1 / i
# print(summa)
#                       LESSON 5

# myList = []
# for _ in range(0, random.randint(5, 20)):
#     myList.append(random.randint(-100, 100))
# print(myList)
# a = myList[0]
# b = myList[-1]
# myList[0] = b
# myList[1] = a
# print(myList)
#
# #
#
# if 2 in myList:
#     print('Yes')
# else:
#     print('No')
#
# #
#
# myList.sort()
# myList.reverse()
# print(myList)
#
# #
#
# myList.pop(0)
# myList.pop(0)
# print(myList)
#
# #
#
# flag = True
# for i in range(len(myList)):
#     if myList[i] < 0:
#         flag = False
# if flag == False:
#     print('Yes')
# else:
#     print('No')
# #
#
# print(len(myList))
#
# #
#
# myList.append(5)
# myList.append(55)
# print(myList)
#
# #
#
# print(myList[0:3])
#
# #
#
# if len(myList) % 2 != 0:
#     myList.pop()
# print(myList)
#
# #
#
# if len(myList) % 2 == 0:
#     print('0')
# else:
#     print(myList[len(myList)//2])
#


#abramyan for 11

# n = int(input())
# summa = n**2
# for i in range(1, n + 1):
#     summa += (n + i) ** 2
# print(summa)
#
# # abramyan for 12

# n = int(input())
# multy = 1
# for i in range(1, n + 1):
#     multy *= 1 + i * 0.1
# print(multy)

#abramyan for 13

# n = int(input())
# itog = 1
# for i in range(n):
#     if i % 2 != 0:
#         itog += i + i * 0.1
#     else:
#         itog -= i + i * 0.1
# print(itog)

# lesson 4, dict
#
# myDict = {
#     "postId": 1,
#     "id": 1,
#     "name": "id labore ex et quam laborum",
#     "email": "Eliseo@gardner.biz",
#     "body": "laudantium enim quasi est quidem magnam voluptate ipsam eos\ntempora quo necessitatibus"
# }
#
# #
# print(myDict['name'])
#
# #
#
# print(len(myDict['email']))
#
# #
#
# print(myDict.keys())
#
# #
#
# print(myDict.values())
#
# #
#
# print(len(myDict['body']))
#
# #
#
# myDict.update({'email':'justcode@gmail.com'})
# print(myDict)
#
# #
#
# myDict.update({'date': '14.05.2022'})
# print(myDict)
#
# #
#
#
# myDict['id'] += 1
# print(myDict['id'])
# print(myDict)
#
# #
#
# myDict.pop('postId')
# print(myDict)

# homework

# dictionary_1 = {'a': 300, 'b': 400}
# dictionary_2 = {'c': 500, 'd': 600}
# dictionary_1.update(dictionary_2)
# print(dictionary_1)

#

# dict = {}
# for i in range(1, 10):
#     dict.update({i:i**2})
# print(dict)

#

# keys = ['red', 'green', 'blue']
# values = ['#FF0000','#008000', '#0000FF']
# dict = {}
# for i in range(len(keys)):
#     dict.update({keys[i]: values[i]})
# print(dict)

#abramyan for 14

# n = int(input())
# s = 0
# for i in range(1, n + 1):
#     x = 2 * i - 1
#     s += x
#     print('** =',  x, 'summa is', s)

#abramyan for 15

# a, n = int(input()), int(input())
# x = 1
# for i in range(1,n + 1):
#     x *= a
# print(x)

# abramyan for 16

# a, n = int(input()), int(input())
# x = 1
# for i in range(1,n + 1):
#     x *= a
#     print(x)

# abramyan for 17

# a, n = int(input()), int(input())
# summa = 0
# for i in range(1,n + 1):
#     summa += a ** i
# print(summa)

# abramyan for 18
#
# a, n = int(input()), int(input())
# itog = 0
# for i in range(1, n + 1, 2):
#     itog -= a ** i + a ** (i + 1)
#     print(itog+(-1)**n*a**n)

# abramyan for 19

# n = int(input())
# fctrl = 1
# for i in range(1,n+1):
#     fctrl *= i
# print(math.factorial(n), fctrl)

#                                   LESSON 6

# def cifry(a, b):
#     for i in range(a, b + 1):
#         print(i)
#
# a = int(input())
# b = int(input())
#
# cifry(a, b)

#

# def firstdef():
#     print('Hello, world!')
#
# def seconddef(a):
#     return a ** 2
#
# a = int(input())
#
# firstdef()
#
# print(seconddef(a))

# abramyan proc 2
#
# def PowerA234(A, B, C, D):
#     B = A ** 2
#     C = A ** 3
#     D = A ** 4
#     return B, C, D
# print(PowerA234(3,0,0,0))

# abramyan proc 3

# def Mean(x, y, amean, gmean):
#     amean = (x + y) / 2
#     gmean = (x*y)** 0.5
#     return amean, gmean
#
# a,b,c,d = int(input()), int(input()),int(input()),int(input())
# print(Mean(a,b,c,d), Mean(a,c,d,b), Mean(a,d,b,c))

#

# def season(mes):
#     if mes == 12 or mes == 1 or mes == 2:
#         return 'зима'
#     if mes>=3<=5:
#         return 'весна'
#     if mes >= 6 <= 8:
#         return 'лето'
#     if mes >= 9 <= 11:
#         return 'осень'
# a = int(input())
#
# print(season(a))

#

# def bank(a, years):
#     for i in range(1, years + 1):
#         a += a * 0.1
#     return a
#
# a = int(input())
# years = int(input())
#
# print(bank(a, years))

#

# def is_prime(num):
#     if num == 1:
#         return False
#     for i in range(2, num + 1):
#         if num % i == 0:
#             return False
#     return True
#
# n = int(input())
# print(is_prime(n))

#

# def date(day, month, year):
#     if day <= 0 or day > 31:
#         return False
#     if month <= 0 or month > 12:
#         return False
#     else:
#         return True
#
# day, month, year = int(input()), int(input()), int(input())
# print(date(day, month, year))

#

# def summa(num):
#     summa = 0
#     for i in range(n+1):
#         summa += i
#     return summa
# n = int(input())
#
# print(summa(n))

#

# def listm(numbers):
#     lst = numbers.split()
#     return max(lst), min(lst)
#
# numbers = input()
#
# print(listm(numbers))