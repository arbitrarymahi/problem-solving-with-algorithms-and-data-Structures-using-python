import turtle
#import time
my_turtle = turtle.Turtle()
my_win = turtle.Screen()

def draw_spiral(my_turtle, line_len):
    if line_len > 0:
        my_turtle.backward(line_len)
        my_turtle.right(90)
        #time.sleep(2)
        draw_spiral(my_turtle, line_len - 3)
        
draw_spiral(my_turtle, 300)
my_win.exitonclick()

