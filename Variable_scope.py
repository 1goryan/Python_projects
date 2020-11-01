                        # Область видимости переменной
"""def gender(sex = "Unknown"): #Задали значение по умолчанию.Теперь можно передавать функцию с параметром и без
    if sex == "m":
        sex = "Male"
    elif sex == "f":
        sex = "Female"
#    else:
#        sex = "Unknown"
    return sex

print(gender())

global_some = 111 #глобальная переменна к ней можно обратиться с любого места

def var1():
    local_some = 123 #локальная переменная, другие функции ее не видят
    print(local_some)

def var2():
    print(local_some)

var1()
var2() # выдает ошибку, так как не видит переменную локал_сам """

"""Создал глобальную переменную со значением 0
Создал две функции
Первая добавляет 5 к текущей переменной и печатает это в принт
Вторая добавляет 10 к глобальной переменной и возвращает ее же через return
Распечатал после вызова обеих функций глобальную переменную и посмотрел на ее значение
"""
global_var = 0

def increase_5 (var):
    var += 5
    print(var)

def increase_10(global_var):
    global_var += 10 
    return global_var

increase_5(global_var)
increase_10(global_var)
print(global_var) 

