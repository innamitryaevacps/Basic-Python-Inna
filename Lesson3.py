#!/usr/bin/env python
# coding: utf-8

# <center>
# <img src="../img/python_theme.png">
# # MLClass. "Прикладной анализ данных"
# # Модуль "Инструментарий Data Science"
# <img src="../img/mlclass_logo.jpg" height="240" width="240">
# 
# ## Автор материала: Юрий Кашницкий, ФКН НИУ ВШЭ
# </center>
# Материал распространяется на условиях лицензии <a href="https://opensource.org/licenses/MS-RL">Ms-RL</a>. Можно использовать в любых целях, кроме коммерческих, но с обязательным упоминанием автора материала.

# # Задачи к уроку 3
# http://informatics.mccme.ru/mod/statements/view.php?id=16206#1

# In[ ]:


# Python 2 and 3 compatibility
# pip install future
from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from builtins import *


# ## Задача A
# Даны два целых числа A и B (при этом A $\leq$ B). Выведите все числа от A до B включительно.

# In[ ]:


A = int(input())
B = int(input())
for x in range(A, B+1):
    print(x)


# ## Задача B
# По данному натуральном n вычислите сумму $1^2+2^2+3^2+ \ldots +n^2$.

# In[ ]:


n = int(input())
summa = 0
for x in range(1, n+1):
    summa += x**2
print(summa)


# ## Задача C
# По данному целому неотрицательному n вычислите значение n!.

# In[ ]:


n = int(input())
num = 1
summa = 1
while num < n:
    num += 1
    summa *= num
print(summa)


# ## Задача D
# По данным целым неотрицательным n и k вычислите значение числа сочетаний из n элементов по k, то есть $\frac{n!}{k!(n-k)!}$.

# In[ ]:


n = int(input())
k = int(input())
def factorial(n):
    num = 1
    summa = 1
    for _ in range(n):
        summa *= num
        num += 1
    return summa
print(factorial(n)/(factorial(k)*factorial(n-k)))


# ## Задача E
# Напишите программу, которая по данному числу n от 1 до 9 выводит на экран n пингвинов. Изображение одного пингвина имеет размер 5×9 символов, между двумя соседними пингвинами также имеется пустой (из пробелов) столбец. Разрешается вывести пустой столбец после последнего пингвина. Для упрощения рисования скопируйте пингвина из примера в среду разработки.
# 
# 

# In[ ]:


penguine = ["   _~_    ",
            "  (o o)   ",
            " /  V  \ ",
            "/(  _  )\ ",
            "  ^^ ^^   "]


# In[ ]:


n = int(input())
from tabulate import tabulate
penguine = ["   _~_    ",
            "  (o o)   ",
            " /  V  \ ",
            "/(  _  )\ ",
            "  ^^ ^^   "]
print(tabulate([[".   _~_    "]*n, [".  (o o)   "]*n, [". /  V  \ "]*n,
["./(  _  )\ "]*n, [".  ^^ ^^   "]*n]))

#Все равно съезжали, поэтому добавила точки


# ## Задача F
# Шоколадка имеет вид прямоугольника, разделенного на n×m долек. Шоколадку можно один раз разломить по прямой на две части. Определите, можно ли таким образом отломить от шоколадки ровно k долек.

# In[ ]:


n = int(input())
m = int(input())
k = int(input())
print("YES" if k <= n*m and (k%n == 0 or k%m == 0) else "NO")


# ## Задача G
# Дано линейное уравнение $ax + b = 0$. Решите уравнение, напечатайте ответ. Если ответов бесконечно много, выведите "INF", если их нет - "NO".

# In[ ]:


a = int(input())
b = int(input())
if a == 0:
    if b == 0:
        print("INF")
    else:
        print("NO")
print("{:.2f}".format(-b/a))


# ## Задача H
# Для данного числа n < 100 закончите фразу “На лугу пасется...” одним из возможных продолжений: “n коров”, “n корова”, “n коровы”, правильно склоняя слово “корова”.

# In[ ]:


n = int(input())
phrase = "На лугу пасется {} коров".format(n)
if n%10 == 1 and n != 11:
    print(phrase + "а")
elif (n%10 in [2, 3, 4]) and n!= 12 and n != 13 and n!= 14:
    print(phrase + "ы")
else:    
    print(phrase)


# # Задача I. Диофантово уравнение

# Даны числа a, b, c, d. Выведите в порядке возрастания все целые числа от 0 до 1000, которые являются корнями уравнения $ax^3+bx^2+cx+d=0$.

# In[ ]:


import time
import numpy as np

a, b, c, d = int(input()), int(input()), int(input()), int(input())

def diofant_equation(a,b,c,d):
    roots = []
    for x in range(1001):
        if a*(x**3) + b*(x**2) + c*x + d == 0:
            roots.append(x)
    return roots


get_ipython().run_line_magic('timeit', 'diofant_equation(a,b,c,d)')


# In[ ]:


#Vectorized version
import time
import numpy as np

a, b, c, d = int(input()), int(input()), int(input()), int(input())

def is_root(x):
    return a*(x**3) + b*(x**2) + c*x + d == 0

nums = np.arange(1001)

vfunc = np.vectorize(is_root)

print(nums[vfunc(nums)])
get_ipython().run_line_magic('timeit', 'nums[vfunc(nums)]')


# In[ ]:


#SciPy optimization
import time
import numpy as np
import scipy

a, b, c, d = int(input()), int(input()), int(input()), int(input())

def cubic_func(x):
    return a*(x**3) + b*(x**2) + c*x + d

vfunc = np.vectorize(cubic_func)

opt_func = scipy.optimize.root(vfunc, [0])
opt_func.x
get_ipython().run_line_magic('timeit', 'opt_func')


# ## Задача J
# Квадрат трехзначного числа оканчивается тремя цифрами, равными этому числу. Найдите и выведите все такие числа.

# In[ ]:


import time

def find_num():
    for x in range(100, 1000):
        if x == (x**2)%1000:
            print(x, end = '\r')

get_ipython().run_line_magic('timeit', 'find_num()')


# In[ ]:


# Vectorized version
import numpy as np
import time

def is_num(x):
    return x == (x**2)%1000

nums = np.arange(100, 1001)
vfunc = np.vectorize(is_num)
get_ipython().run_line_magic('timeit', 'nums[vfunc(nums)]')


# ## Задача K
# По данному натуральному $n \leq 9$ выведите лесенку из n ступенек, i-я ступенька состоит из чисел от 1 до i без пробелов.

# In[ ]:


import timeit

n = int(input())

def string_solution(n):
    nums = "123456789"
    for i in range(n+1):
        print(nums[:i], end = '\r')

# Через вложенный цикл
def loop_solution(n):
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(j, sep='', end='\r')
        print(end = '\r')


# In[ ]:


get_ipython().run_line_magic('timeit', 'string_solution(n)')
get_ipython().run_line_magic('timeit', 'loop_solution(n)')


# ## Задача L
# Дано три числа. Упорядочите их в порядке неубывания. Программа должна считывать три числа a, b, c, затем программа должна менять их значения так, чтобы стали выполнены условия $a \leq b \leq c$, затем программа выводит тройку a, b, c.

# In[ ]:


a = int(input())
b = int(input())
c = int(input())

if a > b:
    a, b = b, a
if a > c:
    a, c = c, a
if b > c:
    b, c = c, b
print(a, b, c)


# ## Задача M
# Давным-давно билет на одну поездку в метро стоил 15 рубля, билет на 10 поездок стоил 125 рублей, билет на 60 поездок стоил 440 рублей. Пассажир планирует совершить n поездок. Определите, сколько билетов каждого вида он должен приобрести, чтобы суммарное количество оплаченных поездок было не меньше n, а общая стоимость приобретенных билетов — минимальна.

# In[ ]:


n = int(input())

n1, n2, n3 = 1, 10, 60
p1, p2, p3 = 15, 125, 440

q_n1 = n%n2
q_n2 = (n%n3)//n2
q_n3 = n//n3

if p1*q_n1 > p2:
    q_n1 = 0
    q_n2 += 1
if p1*q_n1 + p2*q_n2 > p3:
    q_n1 = 0
    q_n2 = 0
    q_n3 += 1

print(q_n1, q_n2, q_n3)


# Попробуйте решить как задачу линейного программирования с помощью SciPy

# In[ ]:


from scipy.optimize import linprog

n = int(input())

n1, n2, n3 = 1, 10, 60
p1, p2, p3 = 15, 125, 440

c = [p1, p2, p3]
A = [[-n1, -n2, -n3]]
b = [-n]
q_n1_bounds, q_n2_bounds, q_n3_bounds = (0, None), (0, None), (0, None)

res = linprog(c, A, b, bounds=(q_n1_bounds, q_n2_bounds, q_n3_bounds))

print(res)


# ## Задача N. Сумма факториалов
# По данному натуральном n вычислите сумму 1! + 2! + 3! + ... +n!. В решении этой задачи можно использовать только один цикл.

# In[ ]:


n = int(input())

addend = 1
total_sum = 0
for i in range(n):
    addend *= i+1
    total_sum += addend
print(total_sum)


# In[ ]:




