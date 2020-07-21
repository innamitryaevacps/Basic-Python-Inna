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

# In[1]:


# Python 2 and 3 compatibility
# pip install future
from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from builtins import *


# ## Задача A
# Даны два целых числа A и B (при этом A $\leq$ B). Выведите все числа от A до B включительно.

# In[1]:


A = int(input())
B = int(input())
for x in range(A, B+1):
    print(x)


# ## Задача B
# По данному натуральном n вычислите сумму $1^2+2^2+3^2+ \ldots +n^2$.

# In[2]:


n = int(input())
summa = 0
for x in range(1, n+1):
    summa += x*x
print(summa)


# ## Задача C
# По данному целому неотрицательному n вычислите значение n!.

# In[3]:


n = int(input())
num = 1
summa = 1
while num < n:
    num += 1
    summa *= num
print(summa)


# ## Задача D
# По данным целым неотрицательным n и k вычислите значение числа сочетаний из n элементов по k, то есть $\frac{n!}{k!(n-k)!}$.

# In[4]:


n = int(input())
k = int(input())
def factorial(n):
    num = 1
    summa = 1
    while num < n:
        num += 1
        summa *= num
    return summa
print(factorial(n)/(factorial(k)*factorial(n-k)))


# ## Задача E
# Напишите программу, которая по данному числу n от 1 до 9 выводит на экран n пингвинов. Изображение одного пингвина имеет размер 5×9 символов, между двумя соседними пингвинами также имеется пустой (из пробелов) столбец. Разрешается вывести пустой столбец после последнего пингвина. Для упрощения рисования скопируйте пингвина из примера в среду разработки.
# 
# 

# In[5]:


penguine = ["   _~_    ",
            "  (o o)   ",
            " /  V  \ ",
            "/(  _  )\ ",
            "  ^^ ^^   "]


# In[6]:


n = int(input())
penguine = ["   _~_    ",
            "  (o o)   ",
            " /  V  \ ",
            "/(  _  )\ ",
            "  ^^ ^^   "]
for i in range(len(penguine)):
    print(penguine[i]*n)


# ## Задача F
# Шоколадка имеет вид прямоугольника, разделенного на n×m долек. Шоколадку можно один раз разломить по прямой на две части. Определите, можно ли таким образом отломить от шоколадки ровно k долек.

# In[7]:


n = int(input())
m = int(input())
k = int(input())
print("YES" if k%n == 0 or k%m == 0 else "NO")


# ## Задача G
# Дано линейное уравнение $ax + b = 0$. Решите уравнение, напечатайте ответ. Если ответов бесконечно много, выведите "INF", если их нет - "NO".

# In[8]:


a = int(input())
b = int(input())
if a == 0:
    if b == 0:
        print("INF")
    else:
        print("NO")
print(-b/a)


# ## Задача H
# Для данного числа n < 100 закончите фразу “На лугу пасется...” одним из возможных продолжений: “n коров”, “n корова”, “n коровы”, правильно склоняя слово “корова”.

# In[9]:


n = int(input())
phrase = "На лугу пасется {} коров".format(n)
if str(n)[-1] == "1" and n != 11:
    print(phrase + "а")
elif (str(n)[-1] == "2" or str(n)[-1] == "3" or str(n)[-1] == "4") and n!= 12 and n != 13 and n!= 14:
    print(phrase + "ы")
else:    
    print(phrase)


# # Задача I. Диофантово уравнение

# Даны числа a, b, c, d. Выведите в порядке возрастания все целые числа от 0 до 1000, которые являются корнями уравнения $ax^3+bx^2+cx+d=0$.

# In[10]:


a = int(input())
b = int(input())
c = int(input())
d = int(input())
for x in range(1001):
    if a*(x**3) + b*(x**2) + c*x + d == 0:
        print(x)


# ## Задача J
# Квадрат трехзначного числа оканчивается тремя цифрами, равными этому числу. Найдите и выведите все такие числа.

# In[11]:


for x in range(100, 1000):
    if str(x) == str(x**2)[-3:]:
        print(x)


# ## Задача K
# По данному натуральному $n \leq 9$ выведите лесенку из n ступенек, i-я ступенька состоит из чисел от 1 до i без пробелов.

# In[3]:


n = int(input())
nums = "123456789"
for i in range(n+1):
    print(nums[:i])


# ## Задача L
# Дано три числа. Упорядочите их в порядке неубывания. Программа должна считывать три числа a, b, c, затем программа должна менять их значения так, чтобы стали выполнены условия $a \leq b \leq c$, затем программа выводит тройку a, b, c.

# In[7]:


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

# In[12]:


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

# In[19]:


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

# In[15]:


n = int(input())

addend = 1
total_sum = 0
for i in range(n):
    addend *= i+1
    total_sum += addend
print(total_sum)


# In[ ]:




