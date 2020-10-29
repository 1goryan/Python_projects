"""                            #ЦИКЛЫ И СПИСКИ
#basket = ["milk", "bread", "butter", "cheese", "pasta", "salt"]
#for f in basket: #синтаксис списка каждый элемент присваивает f 
#    print(f) #вывели весь список

#basket = ["milk", "bread", "butter", "cheese", "pasta", "salt"]
#for f in basket: 
#    if f == "butter":
#        some = f + "+"
#        print(some)

#basket = ["milk", "bread", "butter", "cheese", "pasta", "salt"]
#for f in basket: 
#   print(len(f)) #len считает длинну 

#basket = ["milk", "bread", "butter", "cheese", "pasta", "salt"]
#for f in basket[:3]: # работаем с первыми 3-мя элементами списка
#    print(f)

#basket = ["milk", "bread", "butter", "cheese", "pasta", "salt"]    
#for f in basket[3:]: # пропускаем первые 3 элемента списка
#    print(f)

list1 = ["1", "2", "3", "4", "5", "6", "7"] #Добавляем в список 2 эл. списка 1
list2 = ["milk", "bread", "butter", "cheese", "pasta", "salt"]
for f in list1:
    list2.append(f)     #метод append добавляет элемент в конец списка
print(list2) """

                            #ФУНКЦИЯ Range    
# range (старт, стоп, шаг)
#some = list(range(5)) #создаем список из 5 элементов иф 1 цифра, то только стоп
#print(some)

#some = list(range(2, 5)) #создаем список из 5 элементов иф 2 цифра, то стоп старт и стоп
#print(some)

#some = list(range(2, 10, 2)) #выводим список с 2 до 10 с шагом 2
#print(some)

#for f in range(5): #печатаем 5 раз
#    print("some")

""" цикл перебирает числа от 0 до 100 с шагом один и каждое число,которое делится
 на 5 или 10 увеличивает счетчик на 1 , в конце вывести значение счетчика"""
i = 0
for f in range(0, 100, 1):
    if f % 10 == 0 or f % 5 == 0 :
        i += 1
print(i)       