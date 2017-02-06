
# -*- coding: utf8 -*-
import turtle               # 匯入turtle套件，允許我們使用turtle指令
window = turtle.Screen()        # 產生畫布以進行畫圖
window.bgcolor("lightblue")# 設定畫布底色為淺綠色

john = turtle.Turtle()          # 建立一個海龜turtle，它的名字叫john
john.pensize(5)

    john.forward(100)
    john.right(144)
    john.forward(100)
    john.left(216)
    john.forward(100)
    john.left(216)
    john.forward(100)
    john.right(144)
    john.forward(100)
window.exitonclick()                    # 等待使用者關閉視窗
