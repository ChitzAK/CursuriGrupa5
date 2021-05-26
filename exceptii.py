my_var = input('Numar intreg: ')
try:
    my_int = int(my_var)
    # print(not_defined)
except ValueError as e:
    print('Eroare de valoare', e)
    # raise Exception
except NameError:
    print('Eroare de denumire variabila')
# except Exception as e:
#     print(e)
#     print('Exceptie generala')
else:
    print('Nicio eroare')
finally:

    print('Executam oricum')


