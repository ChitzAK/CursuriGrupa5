cuvant = 'onomatopee'
lista_cuvant = []
for i in cuvant:
    if i != cuvant[0] and i != cuvant[-1]:
        lista_cuvant.append('_')
    else:
        lista_cuvant.append(i)
print(' '.join(lista_cuvant))
numar_incercari_utilizator = 1
litere_deja_incercate = []
while numar_incercari_utilizator <= 7:
    litera_utilizator = input("Alege o litera: ")
    if litera_utilizator == '':
        print('Introdu o litera')
    if str(litera_utilizator).lower() in lista_cuvant:
        print('Litera deja afisata pe ecran')
    elif str(litera_utilizator).lower() in litere_deja_incercate:
        print(f"Deja ai incercat litera {litera_utilizator}, deja ai incercat {' '.join(litere_deja_incercate)}")
    elif str(litera_utilizator).lower() in str(cuvant).lower():
        for iterator, valoare in enumerate(cuvant):
            print(iterator, '->>', valoare)
            if str(valoare).lower() == str(litera_utilizator).lower():
                lista_cuvant[iterator] = valoare  # poate sa fie si litera_utilizator
    else:
        litere_deja_incercate.append(str(litera_utilizator).lower())
        if str(litera_utilizator).lower() not in cuvant:
            numar_incercari_utilizator += 1  # echivalent cu numar_incercari_utilizator = numar_incercari_utilizator + 1
        print(f"Mai ai {8 - int(numar_incercari_utilizator)} incercari")
    if 8 - int(numar_incercari_utilizator) == 0:
        print(f"Ai pierdut! Cuvantul era {cuvant}")
    elif ''.join(lista_cuvant) == cuvant:
        print('Ai castigat!')
        break
    else:
        print(' '.join(lista_cuvant))
