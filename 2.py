"""                                    #СПИСКИ
players = [17, 5, 3, 21, 12]
print(players[3])         #выводим элемент списка
players[3] = 7            #заменяем элемент списка
print(players[3]) 
a = players + [4, 11, 29] #добавляем элементы в список на одно событие
print(a)
players.append(4)         #добавляем элементы в конец списка
print(players)
b = players[:2]           #обрезаем список и оставляем два первых элемента
print(b)
players[:3] = [0, 'true']  #заменяем три первых элемента на два новых
print(players)
players[:] = []
print(players)              #очищаем список """

                            #ПЕРЕМЕННЫЕ
var = 11
varSome = "some"
num1 = 22
num2 = 33
res = num1 + num2
print(res)
num2 = "some word"
#res = num1 + num2
str1 = str(num1)        #приведение к типу строчная переменная
res = str1 + num2
print(res)