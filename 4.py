                            #Условный оператор if, elif и else
"""age = 20
if age < 20 :
    print("your age is less than 20")
elif age == 20:
    print("your age is 20")
else:
    print("your age higher then 20")

name = "ii"
if name is 'ii' :    #is - аналог ==
    print("name contains II")
else : 
    print("name doesn't contain II") """


print("What is your name?") #программа чата с операторами
name = input()
print("Hello " + name + "!")
print("How old are you?")
old = int(input())
if old > 18 :
    print("you are an adult")
elif old == 18 :
    print("Ok, you are " + str(old) + " years old")
else :
    print("you are still a child")
print("What's you hobby?")
hobby = input()
print(hobby + " is such an intresting hobby!")
print("how many hours do you sleep?")
sleep = float(input())
if sleep < 5 :
    print("you sleep so little")
elif sleep < 8 :
    print("you sleep not enought")
elif sleep <= 10 :
    print("you sleep very well")
else :
    print("you sleep too long")

"""num1 = float(input()) #простейший калькулятор
num2 = float(input())
operation = input()
if operation == "/" :
    summ = num1 / num2
elif operation == "*" :
    summ = num1 * num2
elif operation == "+" :
    summ = num1 + num2
elif operation == "-" :
    summ = num1 - num2
else :
    print("please choose correct operation")
print(summ)"""