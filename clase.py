# Animale
# mamifer, reptile, pasari, pesti
# salbatice, domestice

# class Salbatice(Mamifer, Animale)

# Max este o pisica grasa care doarme toata ziua.

# max -> obiect (substantiv)
# pisica -> clasa
# grasa -> proprietate (adjectiv)
# activitati -> metoda a clasei (verb)

# Ford este o masina rosie care merge repede pe drum.

# obiect -> ford
# clasa -> masina
# proprietate -> rosie
# activitate -> merge (metoda a clasei)

# class PrimaClasa:
#     pass
#
#
# my_first_object = PrimaClasa()
# print(my_first_object)

# stiva -> First In Last Out -> Last In First out (LIFO)
# coada -> first in first out (FIFO)

stack = []


def push(val):
    stack.append(val)
    return stack


def pop():
    val = stack[-1]
    del stack[-1]
    return val


push(3)
push(2)
push(1)
print(stack)
print(pop())
print(pop())
print(pop())


