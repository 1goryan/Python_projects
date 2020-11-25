import turtle
#создаем рабочую область
win = turtle.Screen()
win.title("My Game")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

#создаем ракетки
racket_a = turtle.Turtle() #создаем экземпляр класса
racket_a.speed(0) #задаем скорость элемента
racket_a.shape("square") #задаем форму
racket_a.color("blue") #задаем цвет
racket_a.shapesize(stretch_len=1, stretch_wid=5) #задаем размеры экземпляра
racket_a.penup() #метод для перемещения ээкземпляра
racket_a.goto(-350, 0)

racket_b = turtle.Turtle() #создаем экземпляр класса
racket_b.speed(0) #задаем скорость элемента
racket_b.shape("square") #задаем форму
racket_b.color("yellow") #задаем цвет
racket_b.shapesize(stretch_len=1, stretch_wid=5) #задаем размеры экземпляра
racket_b.penup() #метод для перемещения ээкземпляра
racket_b.goto(350, 0)

#создаем шарик

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)

#реализация движения ракеток

def racket_a_up():
    y = racket_a.ycor() #метод записывает в переменную у местоположение ракетки
    y += 20 #переместили ракетку_a на 20 пикселей вверх
    racket_a.sety(y) # задаем новое значение y

def racket_a_down():
    y = racket_a.ycor() #метод записывает в переменную у местоположение ракетки
    y -= 20 #переместили ракетку_a на 20 пикселей вниз
    racket_a.sety(y) # задаем новое значение y

def racket_b_up():
    y = racket_b.ycor() #метод записывает в переменную у местоположение ракетки
    y += 20 #переместили ракетку_b на 20 пикселей вверх
    racket_b.sety(y) # задаем новое значение y

def racket_b_down():
    y = racket_b.ycor() #метод записывает в переменную у местоположение ракетки
    y -= 20 #переместили ракетку_b на 20 пикселей вниз
    racket_b.sety(y) # задаем новое значение y

#привязка к клавиатуре
win.listen()
win.onkeypress(racket_a_up,"w")
win.onkeypress(racket_a_down,"s")
win.onkeypress(racket_b_up,"Up")
win.onkeypress(racket_b_down,"Down")



while True:
    win.update()