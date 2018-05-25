import turtle as t

def draw_square(brad):

     for i in range(4):
        brad.forward(100)
        brad.right(90)

def draw_traingle(brad):

     for i in range(3):
        brad.forward(100)
        brad.right(120)
   
    

def draw_art():
    window = t.Screen()
    window.bgcolor("red")
    brad = t.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(3)

    for i in range(36):
        draw_traingle(brad)
        brad.right(10)

    window.exitonclick()

draw_art()
