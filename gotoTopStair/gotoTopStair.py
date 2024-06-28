import turtle

class ThrowTrashTopStair:
    def __init__(self, step_num: int = 10) -> None:
        self.window_width = 600
        self.safety_distance = 10
        self.step_num = step_num
        self.step_size = self.window_width // step_num
        self.axis_list: list = []
        turtle.shape("turtle")

    def draw_stair(self):        
        # 화면 그리기 바깥쪽 사각형 그리기
        turtle.tracer(0)
        turtle.color("Red")
        turtle.pensize(5)
        turtle.hideturtle()
        
        x = -self.window_width // 2
        y = -self.window_width // 2

        # 바깥쪽 사각형 그리기
        turtle.speed(0)
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.goto(x, y + self.window_width)
        turtle.goto(x + self.window_width, y + self.window_width)
        turtle.goto(x + self.window_width, y)
        turtle.goto(x, y)

        self.axis_list.append((x + self.safety_distance, y + self.safety_distance))
        # 계단 그리기
        while x < self.window_width // 2:
            x += self.step_size
            turtle.goto(x, y)       
            # 이동 경로 계산
            self.axis_list.append((x - self.safety_distance, y + self.safety_distance))
            y += self.step_size
            turtle.goto(x, y)
            self.axis_list.append((x - self.safety_distance, y + self.safety_distance))
        self.axis_list.pop()

        # 화면 그리드 그리기
        turtle.pensize(1)
        turtle.pencolor("lightgray")
        for i in range(-200, 300, 100):
            turtle.penup()
            turtle.goto(i, -300)
            turtle.pendown()
            turtle.goto(i, 300)
            turtle.penup()
            turtle.goto(-300, i)
            turtle.pendown()
            turtle.goto(300, i)
        turtle.update()
        turtle.tracer(1)
    
    def trash_throw(self, speed: int = 1):
        x = -self.window_width // 2 + self.safety_distance
        y = -self.window_width // 2 + self.safety_distance
        turtle.penup()
        turtle.tracer(0)
        turtle.color("black")
        turtle.goto(x, y)
        turtle.pendown()
        turtle.tracer(1)
        turtle.speed(speed)
        turtle.showturtle()

        # 올라가는 경로
        for i in self.axis_list:
            x, y = i
            turtle.setheading(turtle.towards(x, y))
            turtle.goto(x, y)
        
        trash = turtle.Turtle()
        trash.shape("circle")
        trash.color("blue")
        trash.penup()
        
        turtle.tracer(0)
        trash.goto(x, y)
        turtle.tracer(1)

        self.axis_list.reverse()
        # 내려가는 경로
        for i in self.axis_list:
            x, y = i
            turtle.setheading(turtle.towards(x, y))
            turtle.goto(x, y)

try:
    step_num = int(input("계단의 수를 입력하세요: "))
    
    # 터틀 창을 맨 위로 올리기 위해 tkinter 사용
    root = turtle.getcanvas().winfo_toplevel()
    root.call('wm', 'attributes', '.', '-topmost', '1')
    # 인스턴스 생성 및 실행
    story = ThrowTrashTopStair(step_num)
    story.draw_stair()
    
    speed = int(input("거북이 속도 0~10: "))
    story.trash_throw()
    
    turtle.mainloop()
except ValueError as e:
    print(e)
    exit(0)
