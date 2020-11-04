                    #Работа с файлами
#'r' открытие на чтение
#'w' открытие на записть,содержимое файла удаляется, если файл не существуе, создается новый
#'x' открытие на записа, если файла н существует,иначе исключение
#'a' открытие на дозапись, информация добавляется в конце файла
#'b' открытие в двоичном режиме
#'t' открытие в текстовом режиме
#'+' открытие на чтение и запись

"""f = open('E:\Pyth0n\python\modules\some1.txt', 'a') #указывает путь файла и если его нет, то создаем
f.write('some text\n') #записывает что-то и переносим на новую сторку
f.write('end\n')
f.close                #закрыли файл 

f = open('E:\Pyth0n\python\modules\some2.txt', 'w') #очищаем документ и записываем свое
f.write('some text\n') #записывает что-то и переносим на новую сторку
f.write('end\n')
f.close      
 
fr = open('E:\Pyth0n\python\modules\some2.txt', 'r') #читаем содержимое файла
text = fr.read()
fr.close

print(text)

str_1 = input('write some text') # вводим наш текст и записываем его в some1

f = open('E:\Pyth0n\python\modules\some1.txt', 'w') 
f.write(str_1)  
f.close 

fr = open('E:\Pyth0n\python\modules\some2.txt', 'rt') #комбинируем режимы r и t
text = fr.read(12) # ограничиваем чтение 12-ю первыми символами
fr.close

print(text) 

fr = open('E:\Pyth0n\python\modules\some2.txt', 'rt') #выводим текст построчно
for line in fr:
    print(line)
fr.close   """


dialogue = "What is your name?\n" #программа-диалог с записью в файл
print(dialogue) 
name = input() + "\n"
dialogue1 = ("Hello, " + name +  "How old are you?\n")
print(dialogue1)
old = int(input())
dialogue_old = str(old) + "\n"
if old > 18 :
    dialogue2 = ("you are an adult\n")
    print(dialogue2)
elif old == 18 :
    dialogue2 = ("Ok, you are " + str(old) + " years old\n")
    print(dialogue2)
else :
    dialogue2 = ("Ok, you are " + str(old) + " years old\n")
    print(dialogue2)
dialogue3 = ("What's you hobby?\n")
print(dialogue3)
hobby = input() + "\n"
print(hobby + " is such an intresting hobby!")
dialogue4 = ("You hobby is "+ hobby + "how many hours do you sleep?" + "\n" )
print(dialogue4)
sleep = int(input())
dialogue_sleep = str(sleep) + "\n"
if sleep < 5 :
    dialogue5 = ("you sleep so little\n")
    print(dialogue5)
elif sleep < 8 :
    dialogue5 = ("you sleep not enought\n")
    print(dialogue5)
elif sleep <= 10 :
    dialogue5 = ("you sleep very well\n")
    print(dialogue5)
else :
    dialogue5 = ("you sleep too long\n")
    print(dialogue5)

f = open('E:\Pyth0n\python\modules\dialogue.txt', 'w')

functions = [dialogue, name, dialogue1, dialogue_old, dialogue2, dialogue3, hobby, dialogue4, dialogue_sleep, dialogue5]
for i in functions:
    f.write(i)
f.close



