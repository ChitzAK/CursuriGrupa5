# print('Ana "are" mere')
# print('Ana are\'s mere')
# print("Ana \"are\" mere")

culoare = "rosii"
nr1 = 2
# Variabila2 = "Ana are {1} mere {0}".format(nr1, culoare)
# Variabila2 = f"\tAna are \n{nr1} mere \n{culoare}"
# Variabila2 = """
# Ana are
# mere
# si atat
# """
# Variabila2 = "Ana are \n" + str(nr1) + " mere " + culoare
# print(Variabila2)
# c = 0
# a = 3
# b = 2
# c = a + b
# c += a
# c = c + a
# c -= a
# c = c - a
# c = a * b
# c = a % b #modulo => rest
# c = a // b #div => cat
# print(f"Rezultatul este: {c}")

# if conditia e adevarata:
#     print('conditie1')
# elif conditia2 e adevarata:
#     print('conditie2')
# elif conditie3 e adevarata:
#     print('conditie3')
# ...
# else:
#     print('final')
# a = 3.2
# b = int("2")
# a, b = 3.2, int("2")
# print(type(b))
# a_boolean = True # => 1
# b_boolean = False # => 0
# text = "Variabilele sunt egale"
# # text = None
#
# if a_boolean:
#     text = f'Variabila a {a} este mai mare'
# elif a < b:
#     text = f"Variabila b {b} este mai mare"
# elif a < 0:
#     text = f"Variabila a {a} este mai mica decat 0"
# print(text)

# while conditie:
#     sintaxa1
#     sintaxa2
#     ...
#     sintaxan
#convertire in string => str(variabila)
#convertire in integer => int(variabila)
#convertire in boolean => bool(variabila)
#convertire in zecimale => float(variabila)
# a = bool(0)
# while a is False:
#     print('bucla infinita')
#     a = True
    # break
# nume_utilizator = input("Care este numele tau: ")
# print(nume_utilizator)
# while nume_utilizator:
#     pass
#     print(f'Numele utilizatorului este: {nume_utilizator}')
#     nume_utilizator = None

    # break
# print(nume_utilizator)
# x = 10
# while x > 1:
#     print(f"x este: {x}")
#     x -= 1
#     continue
# item = "Ana are mere"
# for variabila_temporara in item:
#     bloc_expresii
# for variabila_temporara in reversed(item):
#     print(variabila_temporara)
# for i in range(10, 1, -1):
#     print(i)

# for (i=0; i<0; i++) {
#
# }
# a = ["a", "b"]
# for index, value in enumerate(a):
#     print(index, value)

a = "anv are mere"
# print(a[2::3])
# print(a.find("e"))
# print("ad" in a)
# print(a.split(" "))
# print(a.replace(" ", "_"))
# print("_".join(a.split(" ")))
# for item in a:
    # print(item, a.index(item))
    # if item != ' ' and a.index(item) == 0:
    #     s = lis
# print(b)
# print(list(a))
# s = list(a)
# s[2] = 'b'
# a = "".join(s)
# print(a)
# a = a.replace("a", "d")
# print(a)
lista = ["a", 2, True, ['a', "b", 3]]
# print(lista[:3])
# print(lista[3][1])
# print(len(lista))
# print(lista[4:5])
# for index, value in enumerate(lista):
#     print(f"{index} => {value}")
# lista.append(44)
# lista.insert(0, 'Ana')
# print(lista.pop(2))
# lista.pop(2)
# lista.pop(2)
lista[2] = None
print(type(None))
print(type(""))
# lista.remove(True)
print(lista)
for index, value in enumerate(lista):
    print(f"{index} => {value}")