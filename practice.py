# 터틀 함수를 이용한 오목 만들어보기
# 게임 규칙 
# 1. 마우스 왼쪽클릭은(빨강) player1, 오른쪽클릭은(검정) player2가 된다
# 2. 홀수번째 차례는 player1이 바둑알을 두고 짝수번째 차례는 player2가 바둑알을 둔다
# 3. 게임의 승패는 먼저 가로, 세로, 대각선으로 바둑알을 5개를 먼저 정렬시키면 게임의 승자가 된다
# <마우스를 클릭한곳에 바둑알이 놓아지니 선에 맞춰 잘클릭하셔야 합니다!!!>
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
    t.fillcolor("red")
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
    t.onscreenclick(right_click,3)
    t.onscreenclick(left_click,1)

    t.mainloop()

