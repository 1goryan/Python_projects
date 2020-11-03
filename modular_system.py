# модульная система , import и from
"""import some #синстаксис импорта
import os 
import random
import time as t
import math as m

some.funct() #сначала название модуля, потом функция

info = os.getcwd() #показывает текущую директорию
print(info)

x = random.randrange(1, 100) #генерируем случайное число от 0 до 100
print(x)
"""
"""x = t.time() # показывает время в секундах с начала эпохи
time = t.ctime(x) # преобразовывает время с начала эпохи в читаемый вид
print(time) 
 
print("input number from 0 to 5") #игра угадайка, программа случайно выдает число от 0 до 5
num1 = random.randrange(0, 5)     #вам нужно его угдать, при правильном ответе будет Win
num2 = int(input())               #при ошибочном будет lose и верное число

if num1 == num2 :
    print("Win")
else:
    print("Lose, correct number was " + str(num1)) 

var = m.factorial(3) #выводим факториал благодаря модулю math
print(var) """

# from/import
#from modules import some # импорт модуля some с папки modules
from some import funct #если модуль лежит в той же папке, что и исполняемый файл
import math

funct()