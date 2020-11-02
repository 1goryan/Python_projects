                        #Списки, словари и множества
"""list1 = [123, "some text", 12, 73] #список

#множества

names = {'Ivan', 'Nikolay', 'Klara', 'Andrei','Ivan', 'andrei'} 
#множества не допускают повторений, регистрозависимы, учитывает колличество пробелов
print(len(names)) 

#cловари {ключ:значение}

class_room = {'Ivan' : 17, 'Nikolay' : 16, 'Klara' : 16}
#print(class_room['Nikolay']) #вывели значение по ключу

for k, v in class_room.items():  # синтаксис цикла для словаря
    print(k + " " + str(v)) """
    

class_room = {}  #cохдана прогрмма, которая заполняет словать значениями,которые пользователь вводит
list1 = input().split()
list2 = input().split()
for k,v in zip(list1, list2):
    class_room[k] = v
    
print(class_room)
