# def my_function(param_1, param_2):
#     if param_1 == 0:
#         return 0
#     print(param_1, param_2)
#     return param_1 + param_2 + my_function(param_1=param_1 - 1, param_2=2)
#
#
# print(my_function(3, 2))


# def get_sum(n):
#     if n == 0:
#         return 0
#     print(n)
#     return n + get_sum(n-1)


# print('Rezultat final', get_sum(3))

# msg = 'Mesaj1'
# print(msg, 'msg')
#
#
# def functie():
#     global msg
#     msg = 'Mesaj'
#     print(msg)
#     return msg
#
#
# print(msg, 'msg29')
# functie()
# print(msg)
# msg = 'Mesaj2'
# print(msg, 'msg35')

# msg = 'copac'


# def my_function_second():
#     print(f"a doua functie: {msg}")
#     return msg


# def my_function():
#     global msg
#     msg = "padure"
#
#     def my_function_second():
#         print(f"a doua functie: {msg}")
#         return msg
#     my_function_second()
#     print(f"functia mea: {msg}")
#     return msg
#
#
# a = my_function()
# my_function_second()
# print(a)

# import functii2 as y
from functii2 import floare as y


def my_function():
    print(f"a doua functie: {msg}", y())
    return msg

msg = 'test'



print(__name__)

if __name__ == '__main__':
    my_function()

