# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 20:41:31 2019

@author: inter000
"""

import re
import numpy as np
import scipy.spatial.distance

# Считываем построчно (по предложениям) файл с данными
with open('sentences.txt', 'r') as file:
    propos = list(map(lambda x: x.lower(), file.readlines()))

# Производим токенезацию по словам
propos = list(map(lambda x: re.findall('[a-z]+[a-z]*', x), propos))

# Присвоим каждому уникальному слову его уникальный номер
words = dict()
num = 0
for _list in propos:
    for word in _list:
        if not (word in words):
            words[word] = num
            num += 1
# Инвертируем словарь, так как в следующем пункте нам будут нужны именно номера слов
words = {value: key for key, value in words.items()}

# Создадим матрицу со строками - предложениями и столбцами - словами
# Элементы матрицы - количество вхождений слова j в предложение i
columns_n = len(words)
rows_n = len(propos)
words_mtx = np.zeros((rows_n, columns_n))
for i in range(rows_n):
    for j in range(columns_n):
        words_mtx[i][j] = propos[i].count(words[j])
        
# Считаем косинусное расстояние между первой строкой и остальными
cosdist_res = [1] * rows_n
for i in range(1, rows_n):
    cosdist_res[i] = scipy.spatial.distance.cosine(words_mtx[0], words_mtx[i])

# Выводим результаты в файл
first_ind = cosdist_res.index(min(cosdist_res))
cosdist_res[first_ind] = 1
second_ind = cosdist_res.index(min(cosdist_res))
with open('submission-1.txt', 'w') as file:
    file.write(str(first_ind) + ' ' + str(second_ind))