
# -*- coding: utf8 -*-
import turtle               # 匯入turtle套件，允許我們使用turtle指令
window = turtle.Screen()        # 產生畫布以進行畫圖
window.bgcolor("lightblue")# 設定畫布底色為淺綠色

john = turtle.Turtle()          # 建立一個海龜turtle，它的名字叫john
john.pensize(5)

color = ["red", "orange", "yellow", "green", "blue"]
for o in color:
    john.color(o)
    john.forward(100)
    john.right(144)

window.exitonclick()                    # 等待使用者關閉視窗
