# r => drepturi doar de citire,
#      valoare default,
#      daca fisierul nu exista, apare eroare
# w => deschidem fisierul cu drept de scriere,
#      in fisier doar se scrie, nu se si citeste,
#      sterge textul din fisier si adauga altul nou
# a => deschidem fisierul cu drept de adaugare,
#      datele din fisier raman,
#      noile date se adauga la sfarsitul fisierului,
#      daca fisierul nu exista, il adauga
# r+ => deschidem fisierul cu drept atat de scriere, cat si de citire,
#       daca fisierul nu exista, apare eroare
# with open('data.txt', 'w') as file:
#     file.write("\nAna are mere \n Ionut e la piata \n povesti \n povesti cu zane")

# with open('data.txt', 'r') as file:
#     for line in file.readlines():
#         print('linie', line)

# with open('data.txt', 'r') as file:
#     # print(file)
#     # print(list(file)[1])
#     # print(list(file.split(' ')))
#     x = []
#     for line in list(file):
#         # print(line.split(' '))
#         x += [x for x in line.split(' ')]
#     print(x)
# from functii import nume_functie as abc

# abc()
# with open('data.txt', 'r') as file:
#     while True:
#         line = file.readline()
#         if not line:
#             break
#         print(line)