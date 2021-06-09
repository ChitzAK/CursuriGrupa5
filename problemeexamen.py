# # 1
# x = 1
#
#
# def f():
#     return x
#
#
# print(x)
# print(f())

# rez posibile
#a) error
#b) 1
#c) 1 1
#d) 0 1


# x = [1, 2, "hello", "world", ["another", "list"]]
# print(len(x[3]))


#a) TypeError: object of type 'int' has no len()
# b) 5
# c) 0
# d) 2

# x = (1, 2, 3)
# x[1] = 4

# rezultat TypeError

# a = [1, 2, 3]
# b = [4, 5]
#
# print(a+b*3)

# a) [1, 2, 3, 4, 5]
# b) [1, 2, 3]
# c) error
# d) [1, 2, 3, 4, 5, 4, 5, 4, 5] correct


# x = [1, 2, 3, 4]
# print(x[-1:])

# a) [1, 2, 3]
# b) [4]
# c) [1, 2, 3, 4]
# d) [3, 2, 1]

# x = [0, 1, [2]]
# x[2][0] = 3
# x[2].append(4)
# x[2] = 2
# print(x)

# a) [0, 1, 3]
# b) [1, 3, 2]
# c) [0, 1, 2] correct
# d) error


# def exercitiu(i):
#     for i in range(i):
#         return i
#
#
# x = exercitiu(3)
# print(x)

# a) error
# b) 0 1 2
# c) 3
# d) 0 correct

# a = range(10)
# y = [x*x for x in a if x % 2 == 0]
# print(y)

# a) [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# b) [2, 4, 6, 8]
# c) [0, 4, 16, 36, 64] correct
# d) [0, 2, 16, 36, 64]


# def make_account():
#     return {'balance': 0}


# def deposit(account, amount):
#     print(account, amount)
#     account['balance'] += amount
#     print(account)
#     return account['balance']


# a = make_account()
# print(a)
# print(deposit(a, 10))

# a) error
# b) 0
# c) 10
# d) None

# print("foo" + 2)

# try:
#     print("a")
# except:
#     print("b")
# else:
#     print("c")
# finally:
#     print("d")

# a) a b c d
# b) a b c
# c) a c d
# d) error

# for k in {"x": 1, "y": 2}:
#     print(k)
#
# dict = {"x": 1, "y": 2}
# for k in dict.values():
#     print(k)

# a) {“x”:1, “y”: 2}
# b) x y correct
# c) 1 2
# d) error

# print(list("python"))

# a) [‘python’]
# b) ‘p’, ‘y’, ‘t’, ‘h’, ‘o’, ‘n’
# c) error
# d) [‘p’, ‘y’, ‘t’, ‘h’, ‘o’, ‘n’] correct

# def func(*args):
#     return 3 + len(args)
#
#
# print(func(4, 4, 4))

# a) 4
# b) error
# c) 6 correct
# d) 15

# count = (3, 2, 5, 4)
# while len(count) < 5:
#     count0 = count[0] + 1
#     print("Hello Geek")

# a) Hello Geek
# b) loop infinit in care se afiseaza Hello Geek correct
# c) None
# d) error


# def exercitiu(var):
#     for letter in "geeksforgeeks":
#         if letter == 'e' or letter == 's':
#             continue
#         print("Current letter :", letter)
#         var = 10
#         return var
#
#
# print(exercitiu(20))

# a) 10
# b) None
# c) Current Letter : g
#    10
# d) Current Letter: g
#    20

# def f(a, list=[]):
#     print("lista =>", list)
#     for i in range(a):
#         list.append(i*i)
#     print(list)
# #
# #
# f(3)
# f(2, [1, 2, 3])
# f(2)

# a) [0, 1, 4] [1,2,3,0,1] [0, 1, 4, 0, 1]
# b) [0, 1, 4] [1,2,3,0,1] [0, 1]
# c) Error
# d) [0, 1, 4]


# list = []


# def functie(a):
#     return list.append(a)
#
#
# print(functie(3))
# def functie(a):
#     lista = [1]
#     print(lista)
#     print(lista.append(a))
#     print(lista)
#     return lista
#
#
# print(functie(3))

list = ['1', '2', '3', '4', '5']
print(list[12:])

# a) index error
# b) []
# c) None
# d) list este cuvant rezervat
