# lista_1 = [1, 2, 3]

# print(list(map(lista_1, lista_2)))

# def suma(n):
#     return n + n


# lista_1 = [[1, 'string1'], [2, 'string2']]
# lista_1 = [[1, 'string1'], 2, 3, 5]
# lista_2 = [[4, 'string2'], [5, 'string3']]
# lista_2 = [[4, 'string2'], 5, 6, 6, 7]
# rezultatul = map(suma, lista_1)
# print(list(rezultatul))

# rezultat = map(lambda x, y: x[0] + y[0], lista_1, lista_2)
# print(list(rezultat))
from datetime import datetime

# lista_1 = [1, 2, 3, 4]
# lista_2 = ['4', '5', '6']
# lista_3 = [7, 8, 9, 10]
# print(list(zip(lista_1, lista_2)))
# for item in zip(lista_1, lista_2, lista_3):
#     element_1, element_2, element_3 = item
#     # print(element_1, element_2, element_3)
#     c = element_1 + element_2
#     print(c)

# s1 = {1, 2, 3}
# s2 = {'a', 'b', 'c'}
# print(list(zip(s1, s2))[0])
#
# lista=[('mihnea', 44), ('ana', 66)]
# functie = lambda data: (data[0].upper(), data[1]/2)
# print(list(map(lambda data: (data[0].upper(), data[1]/2), lista)))
#
# # Data: a1,a2,a3
# # functie: f
# # map (functie,data) => f(a10) , f(a2), f(a3)
#
# date = str(input('Enter the deadline (i.e. 2021,7,21): '))
# year, month, day = map(int, date.split(','))
# due = datetime(year, month, day)
# due = str(due)
# due = due[:10]

#
# def functie(variabila):
#     litere = ['a', 'b', 'c']
#     print(variabila)
#     if variabila in litere:
#         # print('if', variabila)
#         # print(True)
#         # return True
#         return 1
#     else:
#         # return False
#         return '0'
#
#
litere = ['a', 'b', 'c']
secventa_litere = ['d', 'e', 'a', 'b']
#
filtrare = filter(lambda x: x in litere, secventa_litere)
print(list(filtrare))
# for item in filtrare:
#     print(item)

# lista = [1, 'a', '0', False, True, 0, '1', 'c']

# lista_filtrata = filter(None, lista)
# print(list(lista_filtrata))

# Se da urmatoarea lista:
# lista_nume = [‘Maria’, ‘Irina’, ‘Claudiu’, ‘Ionut’, ‘Irina’, ‘Matei’, ‘Irina’, ‘Maria’, ‘Claudiu’]
# Se cere:
# 1. Sortati lista dupa nume
# 2. Determinati numarul de aparitii al fiecarui nume
# 3. Listati numele care apare de cele mai multe ori in lista initiala.
# 4. Listati numele care apare de cele mai putine ori in lista initiala.
