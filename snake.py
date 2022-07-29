from turtle import Screen, Turtle

starting_position = [(0,0),(-20,0),(-40,0)]
move_distance = 20

UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180



class Snake():

    def __init__(self):
        self.snake_list = []
        self.create_snake()
        self.head = self.snake_list[0]

    def create_snake(self):
        for positions in starting_position:
            self.add_segment(positions)

    def add_segment(self, position):
        snake = Turtle("square")
        snake.color("white")
        snake.penup()
        snake.goto(position)
        self.snake_list.append(snake)        
    
    def extend(self):
        self.add_segment(self.snake_list[-1].position())

    def move(self):
        for snake_num in range(len(self.snake_list)-1 ,0,-1):
            new_x = self.snake_list[snake_num-1].xcor()
            new_y = self.snake_list[snake_num-1].ycor()
            self.snake_list[snake_num].goto(new_x,new_y)
        self.head.forward(move_distance)    

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def game_over(self):
        self.head.home()
        self.head.clear()
        self.head.write(f"GAME OVER!", move = False, align="center", font=("Arial", 12, "normal"))
    

    



                       

     


        
        









