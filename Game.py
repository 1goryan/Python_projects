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
racket_b.color("green") #задаем цвет
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
ball.dx = 0.2 #скорость движения шарика по х
ball.dy = 0.2  #скорость движения шарика по у

#создаем счет
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("red")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0 || Player B: 0", align = "center", font = ("Verdana", 22, "normal"))

score_a = 0
score_b = 0

#реализация движения ракеток

def racket_a_up():
    y = racket_a.ycor() #метод записывает в переменную у местоположение ракетки
    if y > 225:
        racket_a.goto(-350, 245)
    else:
        y += 20 #переместили ракетку_a на 20 пикселей вверх
        racket_a.sety(y) # задаем новое значение y

def racket_a_down():
    y = racket_a.ycor() #метод записывает в переменную у местоположение ракетки
    if y < -225:
        racket_a.goto(-350, -245)
    else:
        y -= 20 #переместили ракетку_a на 20 пикселей вниз
        racket_a.sety(y) # задаем новое значение y

def racket_b_up():
    y = racket_b.ycor() #метод записывает в переменную у местоположение ракетки
    if y > 225:
        racket_b.goto(350, 245)
    else:
        y += 20 #переместили ракетку_b на 20 пикселей вверх
        racket_b.sety(y) # задаем новое значение y

def racket_b_down():
    y = racket_b.ycor() #метод записывает в переменную у местоположение ракетки
    if y < -225:
        racket_b.goto(350, -245)
    else:
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
    #движение шарика
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1   

    if ball.xcor() > 390: #если не отбили шарик - он стартует с центра и движется в другую сторону
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {} || Player B: {}".format(score_a, score_b), align = "center", font = ("Verdana", 22, "normal"))
        
    if ball.xcor() < -390:#если не отбили шарик - он стартует с центра и движется в другую сторону
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {} || Player B: {}".format(score_a, score_b), align = "center", font = ("Verdana", 22, "normal"))
        #проверка если позиция мячика >340 проверяем позицию правой рактки, если мячик попал в ракетку, то мы его отбили 
    if ball.xcor() > 340 and ball.ycor() < racket_b.ycor() + 50 and ball.ycor() > racket_b.ycor() -50:
        ball.dx *= -1
        #проверка если позиция мячика >340 проверяем позицию правой рактки, если мячик попал в ракетку, то мы его отбили, 
    if ball.xcor() < -340 and ball.ycor() < racket_a.ycor() + 50 and ball.ycor() > racket_a.ycor() -50:
        ball.dx *= -1
    