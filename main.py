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

# def senReverse(x):
#     # return x[::-1]
#     text = ""
#     for i in x:
#         text = i + text
#     return text
#
# print(senReverse('Hola'))


# 1

# def name_whypython():
#     print('Rolandas')
#     print('Pasirinkau, nes noriu seti gyvenima su IT')
#
# (name_whypython())
# (name_whypython())
# (name_whypython())

# 2

# def poetic():
#     print('Look up…')
#     print('From bleakening hills')
#     print('Blows down the light, first breath')
#     print('Of wintry wind...look up, and scent')
#     print('The snow!')
#
# times = int(input('How many times: '))
#
# for i in range(times):
#     poetic()

# 3

# def first_text():
#     print('Just ')
#
# def secondd_text():
#     print('do')
#
# def third_text():
#     print('Nothing')
#
# first_text()
# secondd_text()
# third_text()

# 4

# def first_sentence():
#     print('Mano vardas ')
#
# def second_sentence():
#     print('Rolandas')
#
# def result():
#     first_sentence()
#     second_sentence()
#
# result()

# 5

# def random_numbers():
#     a = random.randrange(0, 10)
#     b = random.randrange(0, 10)
#     print(f'{a} + {b} = {a + b}')
#
# random_numbers()
# random_numbers()
# random_numbers()

# 6

# def police_officer_info():
#     name = 'John'
#     surname = 'Fibi'
#     age = 34
#     income = '3000$'
#     position = 1.0
#     work = 'Documents'
#
#     print('Policininko informacija ')
#     print(f'Vardas: {name}')
#     print(f'Pavarde: {surname}')
#     print(f'Amzius: {age} years old')
#     print(f'Alga: {income}')
#     print(f'Etatas: {position}')
#     print(f'Specializacija: {work}')
#
# police_officer_info()

# 7

# def random_numbers():
#     count = 0
#     for x in range(10):
#         x = random.randrange(0, 11)
#         print(x)
#         count += 1
#         if count == 10:
#             print(' ')
#
# random_numbers()
# random_numbers()
# random_numbers()

# 8

# def ran_num():
#     num = random.randrange(0, 11)
#     print(num)
#
# for i in range(10):
#     ran_num()

# 9

# def hello_name(hiname):
#     print(f'Sveiki {hiname}')
#
# def goodbye_name(byename):
#     print(f'Viso gero {byename}')
#
# name = input('Vardas: ')
# hello_name(name)
# goodbye_name(name)

# 10

# def numbers(first, second):
#     if first > second:
#         print(f'Pirmas skaicius {first} didesnis')
#     elif second > first:
#         print(f'Antras skaicius {second} didesnis')
#     else:
#         print('Abu skaiciai yra lygus')
#
# a = int(input('Jusu pirmas skaicius: '))
# b = int(input('Jusu antras skaicius: '))
#
# numbers(a, b)

# 11

# testi = 'taip'
#
# def car_info(marke, modelis, metai, turis):
#     print(f'Car mark: {marke}')
#     print(f'Car model: {modelis}')
#     print(f'Release year: {metai}')
#     print(f'Power: {turis}')
#
#
# while testi == 'taip':
#     a = (input('Marke: '))
#     b = (input('Modelis: '))
#     c = int(input('Metai: '))
#     d = (input('Turis: '))
#     car_info(a, b, c, d)
#     testi = (input('Tesiam (taip/ne): '))
#     if testi == 'ne':
#         print('Aciu')

# 12

# def number_sum(a, b):
#     print(f'{a} + {b} = {a + b}')
#
# def number_minus(a, b):
#     print(f'{a} - {b} = {a - b}')
#
# def number_multiply(a, b):
#     print(f'{a} * {b} = {a * b}')
#
# def number_divide(a, b):
#     print(f'{a} / {b} = {a / b}')
#
# def rand_numbers():
#     first = random.randrange(1, 11)
#     second = random.randrange(1, 11)
#     number_sum(first, second)
#     number_minus(first, second)
#     number_multiply(first, second)
#     number_divide(first, second)
#
# rand_numbers()
# rand_numbers()
# rand_numbers()

# 13

# def list(mas):
#     a = 0
#     for x in mas:
#         a = len(x)
#         print(f'{x}, {a} raidziu kiekis')
#
# masyvas = ['labas', 'senokai', 'matytas', 'drauge']
# list(masyvas)

# 14

# def number_list(list):
#     for i in list:
#         print(f'Skaicius {i}, skaiciaus kvadratas {i*i}, skaicius padalyntas pusiau {i/2}')
#
# list1 = [1, 4, 8, 12, 16, 20]
# list2 = [3, 7, 11, 13, 17, 21]
#
# number_list(list1)
# print('---------')
# number_list(list2)

# 15

# def student_grades_info(grades, info):
#     print(f'Studento vardas: {info}')
#     print(f'Studento pazymiai: {grades}')
#     count = 0
#     sum = 0
#     for i in grades:
#         sum = sum + i
#         count += 1
#         if len(grades) == count:
#             print(f'Vidurkis {sum / count}')
#
# gradelist = [7, 9, 4, 10, 10]
# namesurname = 'Jack Sparrow'
#
# student_grades_info(gradelist, namesurname)

# 16

def sumednumbers(masyvas):
    print(max(masyvas))

def ran_num_generator(ran):
    for i in range(0, 10):
        i = random.randrange(0, 101)
        ran.append(i)
    return ran


list1 = []
list2 = []
list3 = []

ran_num_generator(list1)
sumednumbers(list1)
print(list1)
ran_num_generator(list2)
sumednumbers(list2)
print(list2)
ran_num_generator(list3)
sumednumbers(list3)
print(list3)
