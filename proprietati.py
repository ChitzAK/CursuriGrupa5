# class Exemplu:
#     __counter = 0
#
#     def __init__(self, value=1):
#         self.__first = value
#         Exemplu.__counter += 1
#
#     def set_second(self, value=2):
#         self.__second = value
#
#
# obiect_1 = Exemplu()
# obiect_2 = Exemplu(2)
# obiect_2.set_second(3)
#
# obiect_3 = Exemplu(4)
# obiect_4 = Exemplu(4)
# obiect_4 = Exemplu(5)
# # obiect_3.__third = 5
#
# print(obiect_1.__dict__, obiect_1._Exemplu__counter)
# print(obiect_2.__dict__, obiect_2._Exemplu__counter)
# print(obiect_3.__dict__, obiect_3._Exemplu__counter)

class Exemplu:

    attr1 = 1

    def __init__(self, val):
        if val % 2 != 0:
            self.a, self.b = 1, 0
        else:
            self.b, self.a = 2, 0


# obiect_1 = Exemplu(1)
# print(obiect_1.a)
# print(obiect_1.b)
# print(hasattr(Exemplu, 'attr1'))
# print(hasattr(Exemplu, 'attr'))
print(dir(Exemplu))

