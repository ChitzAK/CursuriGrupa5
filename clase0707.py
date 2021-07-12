# class Clasa:
#     variabila = 1
#
#     def __init__(self):
#         self.var = 2
#         # self.x = 0
#
#     def method(self):
#         self.x = 5
#         return self.x
#
#     def __hidden(self):
#         pass
#
#
# obiect = Clasa()
# # print(obiect.__dict__)
# # print(Clasa.__dict__)
# # print(obiect.variabila, Clasa.variabila)
# # print(obiect.var)
# # print(obiect.x)
# # print(obiect.method())
# print(type(obiect).__name__)

# class Star:
#     def __init__(self, name, galaxie):
#         self.name = name
#         self.galaxie = galaxie
#
#     def __str__(self):
#         # return f"{self.name} in {self.galaxie}"
#         return '1'
#
#
# sun = Star("Sun", "Milky Way")
# print(sun)

# class Animale:
#
#     variabila2 = 1
#     variabila1 = 5
#
#     def __init__(self):
#         self.val = 6
#
#     def __int__(self):
#         return self.val
#
#     def functie_1(self):
#         return 102
#
#
# class Mamifere(Animale):
#
#     variabila1 = 2
#     # variabila2 = 5
#
#     def __init__(self):
#         super().__init__()
#         # print(self.val)
#         self.val = 7
#         # print(self.val, '59')
#         # Animale.__init__(self, valoare)
#         # super().__init__(valoare)
#
# obj = Mamifere()
# # print(obj.variabila1)
# # print(obj.variabila2)
# print(obj.val)
# print(int(obj))

# class Insecte:
#     pass
#
#
# class Domestice(Mamifere, Insecte):
#     pass

# obiect_1 = Animale(3)
# print(int(obiect_1))
# obiect_2 = Animale(2)
# obiect_3 = obiect_1
# obiect_3.val += 1
#
# print(obiect_1 is obiect_2)  # False
# print(obiect_2 is obiect_3)  # False
# print(obiect_3 is obiect_1)  # True
# print(obiect_1.val, obiect_2.val, obiect_3.val)
#
# string_1 = "Maria are mere "
# string_2 = "Maria are mere si pere"
# string_1 += "si pere"
# print(string_1 == string_2, string_1 is string_2)


#
class Joc:

    def __init__(self):
        self.name = 'john'


class Jucator(Joc):

    def __init__(self):
        super().__init__()
        self.prenume = 'ss'

obj = Jucator()
print(obj.name)
#
#     variabila2 = 1
#     variabila1 = 5
#
#     def __init__(self):
#         self.val = 6
#
#     def __int__(self):
#         return self.val
#
#     def functie_1(self):
#         return 102
#
#
# class Insecte:
#
#     def functie_1(self):
#         return 104
#
#
# class Mamifere(Animale):
#
#     variabila1 = 2
#
#     def __init__(self):
#         super().__init__()
#         self.val = 7
#
#     # def functie_1(self):
#     #     return 103
#
#
# class Domestice(Mamifere, Insecte):
#     pass
#
# obj = Domestice()
# print(obj.functie_1())


class Dog:

    legs_no = 4

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name}"

    def __change_name(self, name):
        self.name = name
        return self.name

    @staticmethod
    def speak():
        return "Ham ham"


my_dog = Dog("Rex")
# print(my_dog.change_name("Max"))
# print(Dog.speak())
print(my_dog._Dog__change_name("Max"))
# print(my_dog.speak())

