# Turtle을 이용한 별빛 프로젝트
#  
import turtle
import random
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QLabel, QPushButton

colors = [
    "aliceblue", "antiquewhite", "aqua", "aquamarine", "azure",
    "beige", "bisque", "blanchedalmond", "cornsilk", "cyan",
    "floralwhite", "gainsboro", "ghostwhite", "honeydew", "ivory",
    "lavender", "lavenderblush", "lemonchiffon", "lightblue",
    "lightcoral", "lightcyan", "lightgoldenrodyellow", "lightgreen",
    "lightgrey", "lightpink", "lightsalmon", "lightseagreen",
    "lightskyblue", "lightslategray", "lightsteelblue", "lightyellow",
    "linen", "mintcream", "mistyrose", "moccasin", "navajowhite",
    "oldlace", "papayawhip", "peachpuff", "pink", "plum",
    "powderblue", "seashell", "snow", "thistle", "wheat", "white",
    "whitesmoke", "yellow", "yellowgreen"
]

turtle.ht()  # 거북이 숨기기
turtle.speed(0)  # 거북이 속도 설정
turtle.bgcolor("black")  # 배경색 설정
turtle.Screen().tracer(0)  # 화면 갱신속도 설정

total_star = 100
init_star_x = (-300, 300)
init_star_y = (-100, 300)
init_star_size = (5, 15)
init_star_distance = (1, 5)

class DrawStar:
    def __init__(self, turtle):
        self.turtle = turtle
        self.color = random.choice(colors)
        self.reset_star()

    def reset_star(self):
        self.x = random.randint(*init_star_x)
        self.y = random.randint(*init_star_y)
        self.size = random.randint(*init_star_size)
        self.distance = random.randint(*init_star_distance)
        self.turtle.color(self.color)

    def draw_star(self):
        self.y -= self.distance
        if self.y < -turtle.window_height() // 2:
            self.reset_star()

        self.turtle.penup()
        self.turtle.goto(self.x, self.y)
        self.turtle.pendown()
        self.turtle.begin_fill()
        for _ in range(5):
            self.turtle.forward(self.size)
            self.turtle.right(144)
            self.turtle.forward(self.size)
            self.turtle.left(72)
        self.turtle.end_fill()

    def space(self):
        self.turtle.clear()

def update_stars():
    if not running:
        return
    for star in stars:
        star.space()
        star.draw_star()
    turtle.Screen().update()
    turtle.ontimer(update_stars, 17)  # 약 60Hz (1000ms / 60 ≈ 17ms)


class InputBoxExample(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # QLabel
        self.label = QLabel('Enter star numbers:', self)
        layout.addWidget(self.label)

        # QLineEdit
        self.line_edit = QLineEdit(self)
        layout.addWidget(self.line_edit)

        # QPushButton
        self.button = QPushButton('input', self)
        self.button.clicked.connect(self.show_text_and_quit)
        layout.addWidget(self.button)

        # Set layout
        self.setLayout(layout)

        self.line_edit.returnPressed.connect(self.button.click)

        # Window settings
        self.setWindowTitle('Init Star Numbers 1~1000')
        self.setGeometry(100, 100, 300, 200)
        self.show()

    def show_text_and_quit(self):
        global total_star 
        try:
            total_star = int(self.line_edit.text())
            if total_star < 1 or total_star > 1000:
                print('Please enter a number between 1 and 1000')
                raise   ValueError
        except ValueError:
            print('Please enter a number')
            total_star = 100
        
        print(f'You entered: {total_star}')
        QApplication.instance().quit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = InputBoxExample()
    app.exec_()
    del ex
    print(f'You entered: {total_star}')
    running = True
    stars = [DrawStar(turtle.Turtle()) for _ in range(total_star)]
    
    
    update_stars()
    
    turtle.Screen().mainloop()
