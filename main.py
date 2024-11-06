from turtle import Turtle, Screen

t = Turtle()
screen = Screen()

def move_fd():
    t.fd(10)

def move_bk():
    t.bk(10)

def turn_lt():
    t.lt(10)

def turn_rt():
    t.rt(10)

def clear():
    t.clear()
    t.penup()
    t.home()
    t.pendown()


screen.listen()
screen.onkey(move_fd, "w")
screen.onkey(move_bk, "s")
screen.onkey(turn_lt, "a")
screen.onkey(turn_rt, "d")
screen.onkey(clear, "c")
screen.mainloop()