# def my_function():
#     pass

# cuvant obligatoriu def
# numele functie my_function, trebuie sa contina _ in cazul in care este format din mai multe cuvinte
# niciodata cu litera mare, incep cu litera mica
# nu incepe cu cifre sau caractere speciale
# argumentul functiei este optional
# o functie trebuie sa returneze ceva




# variabila = my_function()
# # print(variabila)
# a = 1
# b = 2
# c = a + b
# print(c)

b = 4

def suma(a: int = 1, b: int = 2) -> (int, int):
    """
    :param a: prima valoare din suma
    :param b: a doua valoare din suma
    :return: suma a doua numere
    """
    # b = 4
    # print(int(a) + int(b))
    return int(a) + int(b), int(a) - int(b)

c, diferenta = suma(3, 3)
# c = suma(3, 3)
# print(c)


def nume_functie(a: int, b: int, c: int = 3) -> (int, int):
    """
    @param a:
    @param b:
    @param c:
    @return:
    """
    if a == 2:
        return 2 * 2 * 2, 2 + 2 + 2
        # d = 2 - 2 - 2
    return a * b * c, a + b + c


variabila1, variabila2 = nume_functie(2, b=3, c=4)
print(variabila1, variabila2)
