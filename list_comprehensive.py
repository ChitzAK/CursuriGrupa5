# lista = []
# for x in range(10):
#     lista.append(x**2)
# lista = [x**2 for x in range(10)]
# lista_duplicat = []
# lista_duplicat2 = []
# for x in lista:
#     if x < 36:
#         x = x + 1
#     else:
#         x = x * 1000
#     lista_duplicat.append(x)
# lista_duplicat = [x for x in lista if x % 2 == 0]
# lista_duplicat = [x+1 if x < 36 else x * 1000 for x in lista]
# for x in lista:
#     for y in str(x):
#         lista_duplicat.append(y)
# lista_duplicat = [y for x in lista for y in str(x)]
# for col in range(4):
#     lista_duplicat.append(lista_duplicat2)
#     for val in range(3):
#         lista_duplicat2.append(val)
# lista_duplicat = [[col for col in range(3)] for val in range(4)]
# print(lista_duplicat)
# a = 10
# b = 20
# if a < b:
#     min = a
# else:
#     min = b
# min = a if a < b else b
# print(min)

# def functie(a, b, *args):
#     print(args)
#     suma = a + b
#     for i in args:
#         suma += i
#     return suma
# #
# print(functie(1, 2, 3, 4, 5))

# def functie(a, b, **kwargs):
#     print(kwargs)
#     suma = a + b
#     for value in kwargs.values():
#         suma += value
#     return suma
#
#
# # print(functie(1, 2, c=3, d=4))
# def functie_lambda(x, y):
#     return x - y
#
# print(functie_lambda(2, 3))

# functie_lambda = lambda x, y: x - y
# print(functie_lambda(2, 3))
jucatori = [{"nume": 'ion', "prenume": 'Vasile', "nivel": 3},
            {"nume": 'ilie', "prenume": 'gheorghe', "nivel": 4},
            {"nume": 'radu', "prenume": "stanescu", "nivel": 1}]

def jucatori_dupa_nivel(dictionar_de_sortat):
    for item in dictionar_de_sortat:
        print(item)
        return item['nivel']
    # print(dictionar_de_sortat)
    # return dictionar_de_sortat['nivel']

print(jucatori_dupa_nivel(jucatori))
# jucatori_dupa_nivel = lambda jucator: jucator['nivel']
# print(jucatori_dupa_nivel(jucatori))
sortati = sorted(jucatori, key=lambda jucator: jucator['nivel'])
# print(sortati)
