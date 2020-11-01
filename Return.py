                            #Return
"""a = abs(-3)
print(a)
some = max(4, 7, 2, -1, 0)
print(some)

def squar (x):
    #y = x ** 2
    return x ** 2 # возвращаем значение в общую область, все что идет за ретерн не работает

print(squar(5))

def some (x):           # использование нескольких ретернов
    if x % 2 == 0:
        return True
    else :
        return False

print(some(12)) """

def calc (num1, num2, operation):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num1 >= num2:
            return num1 / num2
        else :
            return "be careful num1 < num2 " + str(num1 / num2)
    else:
        return "please choose correct operation"

print(calc(int(input()), int(input()), input()))

