                            #ЦИКЛ WHILE
"""i = 5
while i >= 1: #синтаксис цикла вайл
    print(i)
    i -= 1"""

i = 0   #Используя цикл WHILE выввели через функцию print() парные числа от 0 до 50
while i < 50:
    i += 1
    if i % 2 == 0: 
        print(i)
    
for i in range(0, 51, 1): # тоже самое, но с циклом FOR
    if i % 2 == 0:
        print(i)
