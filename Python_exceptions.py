#Исключения в питон try, except

"""a = 100
b = "2"
try:
    c = a / b
except ZeroDivisionError : #отлавливаем именно эту ошибку, на другие не сработает, если отлавливаем все ошибки пишем просто except:
    print('eror in division')
    print('var a = ', a)"""

f = open('E:\Pyth0n\python\modules\some3.txt', 'a')
ints = []
try:
    for line in f:
        ints.append(int(line))
except ValueError:
    print("it isn't a number")
except Exception:
    print("what's it?")
else:           #используется если исключения не было
    print('all is well') 
finally: #используется тогда, когда непременно нужно что-то сделать, не смотря на отловленную ошибку
    f.close()
    print('I close the file')