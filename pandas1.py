import pandas as pd
#
# # print(pd.__version__)
# # a = [1, 7, 2]
#
# # a = {'x': 1, "y": 7, "z": 2}
# # variabila = pd.Series(a, index=['x', 'y', 'z'])
# # variabila = pd.Series(a, index=["x", "z"])
#
# # print(variabila)
#
# data = {
#     "key1": [0, 1, 2],
#     "key2": [3, 4, 5]
# }
#
# variabila = pd.DataFrame(data, index=["linie1", "linie2", "linie3"])
#
# # print(variabila.loc[[0, 1]])
# print(variabila)
# print('________')
# # print(variabila["key2"])
# print(variabila.loc["linie2"])

# df = pd.read_csv('EXEMPLU.csv')
# print(df)
# data = {
#   "Duration":{
#     "0":60,
#     "1":60,
#     "2":60,
#     "3":45,
#     "4":45,
#     "5":60
#   },
#   "Pulse":{
#     "0":110,
#     "1":117,
#     "2":103,
#     "3":109,
#     "4":117,
#     "5":102
#   },
#   "Maxpulse":{
#     "0":130,
#     "1":145,
#     "2":135,
#     "3":175,
#     "4":148,
#     "5":127
#   },
#   "Calories":{
#     "0":409,
#     "1":479,
#     "2":340,
#     "3":282,
#     "4":406,
#     "5":300
#   }
# }
#
# df = pd.DataFrame(data)
# print(df)

df = pd.read_csv('test.csv')
print(df)
# df1 = None
# for x in df.index:
#     if df.loc[x, 'AL'] == ': ':
#         df1 = df.drop(x)
# df1 = df.duplicated()
import matplotlib.pyplot as plt
df1 = df.drop_duplicates()
print(df1.to_csv('test1.csv'))
# print(df.corr())
print(df.describe())

print(df.mean())
# df.plot(kind='scatter', x='AT', y='BE')
# df.plot(kind='scatter', x='AT', y='BE')
df['AT'].plot(kind='hist')
plt.show()
# print(df.head(10))
# print(df.tail(10))
# print(df.info())

# new_df = df.dropna(inplace=True)
# print(df.to_string())

# df2 = df.fillna(888)
# df['AL'].fillna(130, inplace=True)
# df.ffill()
# df2.loc[7, "AL"] = 45
# print(df2)
# new_df = df.replace(': ', 999)
# print(new_df)


# df = pd.read_csv('EXEMPLU2.csv')
# print(new_df.to_string())
# dataset = [
#    ('AL', [': ', ': ', ': ', ': ', ': ', ': ', ': ', '84 ', ': ']),
#    ('AT', ['75 ', '79 ', '81 ', '81 ', '82 ', '85 ', '89 ', '89 ', '90 ']),
#    ('BA', [': ', ': ', ': ', ': ', ': ', ': ', ': ', '69 ', '72 ']),
#    ('BE', ['77 ', '78 ', '80 ', '83 ', '82 ', '85 ', '86 ', '87 ', '90 ']),
#    ('BG', ['45 ', '51 ', '54 ', '57 ', '59 ', '64 ', '67 ', '72 ', '75 ']),
#    ('CH', [': ', ': ', ': ', '91 ', ': ', ': ', '93 b', ': ', '96 ']),
#    ('CY', ['57 ', '62 ', '65 ', '69 ', '71 ', '74 ', '79 ', '86 ', '90 '])]
#
# d = dict()
# for v, k in dataset:
#     d[v] = k
# print(d)
# df = pd.DataFrame(d)
# # print(df)
# transformed_data = dict(dataset)
# df = pd.DataFrame(transformed_data)
# print(df)
# print(df.transpose())


