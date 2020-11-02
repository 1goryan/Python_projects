                        #Распаковка аргументов
"""def calorie_calculator(name, get_calorie, spend_calorie):
    if get_calorie > spend_calorie:
        msg = name + " getting fat"
    else:
        msg = name + " lose weight"
    return msg
    
person = ["Ivan", 1900, 1200]

print(calorie_calculator(*person))  # *даем ссылку на список     
print(calorie_calculator("Ihor", 2000, 2110))   """

"""def some(*args):   #создаем функция для неизвестного колличества аргументов
    resault = 0
    for a in args:
        resault += a
    print(resault)

some(3, 12, 55)"""

""" Создана функция, которая принимает любое количество аргументов (числа)
    Аргументы вводятся посредством функции input в список
    Функция берет аргументы с списка
    Перемножает их
    Считать количество аргументов
    Выводить результат и количество через return """

numbers = []  

numbers = input().split() #split метод возвращающий список строк, разрезав исходную строку на части по пробелам

for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

def multiplication(*args):
    resault = 1
    quantity = 0
    for f in args:
        resault *= f
        quantity += 1
    return "resault = " + str(resault) + " quantity = " + str(quantity)


print(multiplication(*numbers))


