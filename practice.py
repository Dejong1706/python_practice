# 터틀 함수를 이용한 오목 만들어보기

import turtle as t

def title():
    t.penup()
    t.goto(-140,270)  
    t.write("====오목 대결====", font = ("맑은 고딕", 18, "bold")) 
def garo_screen():
    y = 250
    for i in range(16):
        t.penup()
        t.goto(-250, y)
        t.pendown()
        t.fd(450)
        y = y - 30
def sero_screen():
    x = -250
    for j in range(16):
        t.penup()
        t.goto(x, 250)
        t.pendown()
        t.fd(450)
        x = x + 30
def right_click(x,y):
    t.fillcolor("black")
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.stamp()
def left_click(x,y):
    t.fillcolor("blue")
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.stamp()

if __name__ == "__main__": 

    t.speed(5)
    t.screensize(500, 500)
    t.shape("circle")
    title()
    garo_screen()
    t.rt(90)
    sero_screen()
    t.onscreenclick(right_click,1)
    t.onscreenclick(left_click,3)

    t.mainloop()

