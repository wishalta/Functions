import random
# 1

# def sum(a = 0, b = 0):
#     return a + b
#
# a = int(input('Skaicius: '))
# b = int(input('Skaicius: '))
#
# result = sum(a, b)
# print(result)

# 2

# def PISq(): #Funkcija grazina
#     return 9.8596
# print(PISq())

# 3

# a = int(input('1 skaicius: '))
# b = int(input('2 skaicius: '))
#
# def sumInt(a = 0, b = 0):# priima, grazina
#     return a * b
#
# result = sumInt(a, b)
# print(result)

# 4

# def spausdinti(masyvas):
#     print(masyvas)
#
# masyvas = [1, 2, 3, 4, 5]
# spausdinti(masyvas)

# 5

# a = int(input('Skaicius: '))
# b = int(input('Skaicius: '))
#
# def rand(a, b):
#     if a > b:
#         print(random.randrange(b, a))
#     elif b > a:
#         print(random.randrange(a, b))
#
#
# ats = rand(a, b)
# print(ats)

# 6


# a = 0
# i = 0
#
# def rand(min, max, len):
#     masyvas = [random.randint(min, max) for x in range(len)]
#     return masyvas
#
# min = 10
# max = 50
# mas = 5
#
# ats = rand(min, max, mas)
# print(ats)
#
# # 7
#
#
# def sumNumList(sum):
#     suma = 0
#     for i in ats:
#         print(i)
#         suma = suma + i
#     return suma
#
#
# atsakymas = sumNumList(sum)
# print(atsakymas)

# 8

# atts = 0
# attts = 0
#
# def listAverage():
#     suma = 0
#     count = 0
#     for i in ats:
#         suma = suma + i
#         count += 1
#     return suma, count
#
#
# atts = listAverage()[0]
# attts = listAverage()[1]
# print(atts)
# answer = atts / attts
# print(answer)

# 9

# a = int(input('Eiluteja: '))
# b = int(input('Stulpeliu: '))
#
# def Staciakampis(a, b):
#     for i in range(b):
#         print('*' * a)
#
# Staciakampis(a, b)

# 10
# Šiandien labai graži diena
# string = input('Sakinys: ')
#
# def sentenceSymbols(string):
#     count = 0
#     tarpas = 0
#     for i in string:
#         if i == ' ':
#             tarpas += 1
#         else:
#             count += 1
#     return count, tarpas
#
# print(f'Tiek raidziu: {sentenceSymbols(string)[0]}')
# print(f'Tiek tarpu: {sentenceSymbols(string)[1]}')

# 11

def senReverse(x):
    return x[::-1]

sentence = input('Sakinys: ')
sentence = senReverse(sentence)
print(senReverse(sentence))