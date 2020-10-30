                            #ФУНКЦИИ
#print() #название функции(аргумет)
#int() #приводит число к целому типу
#input() #получает данные от пользователя

#def some():     #синтаксис создания функции без аргументов
#    print("some")
#some()          #вызов функции

#def bitcoin_to_usd(bts, curs):  #синтаксис создания функции с аргументами
#    amount = bts * curs
#    print(amount)

#bitcoin_to_usd(10, 4100)        #вызов функции


def addition(num1, num2): #функция сложения двух чисел
    summ = num1 + num2
    print(summ)

#addition(int(input()), int(input()))

def multiplication(num1, num2): #функция умножения двух чисел
    resault = num1 * num2
    print(resault)

#multiplication(int(input()), int(input()))

def division(num1, num2):   #функция деления двух чисел с проверкой большего числа
    if num1 > num2:
        resault = num1 / num2
        print(resault)
    else:
        print("be careful first number lower than second")
        resault = num1 / num2
        print(resault)

division(int(input()), int(input()))