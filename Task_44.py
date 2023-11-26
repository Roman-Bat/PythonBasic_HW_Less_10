# Задача 44: В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца.
# Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?
# import random
# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI':lst})
# data.head()
# https://colab.research.google.com/drive/1qKamnDiRmpRZkpiqWPkunBdAhmzhMcGz?usp=sharing

import random
import pandas as pd

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# Выполнение Домашнего задания:
data['robot'] = (data['whoAmI'] == 'robot').astype(int)
data['human'] = (data['whoAmI'] == 'human').astype(int)

# Выведем новые получившиеся столбцы
# print(data)

# Удалим исходный столбец 'whoAmI'
data.drop('whoAmI', axis=1, inplace=True)

# Выведем первые 5 значений получившейся работы
print(data.head())

