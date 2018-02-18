import turtle

def draw_triangle(points, color, my_turtle):
    my_turtle.fillcolor(color)
    my_turtle.up()
    my_turtle.goto(points[0][0],points[0][1]) 
    my_turtle.down()
    my_turtle.begin_fill()
    my_turtle.goto(points[1][0],points[1][1])
    my_turtle.goto(points[2][0],points[2][1])
    my_turtle.goto(points[0][0],points[0][1])
    my_turtle.end_fill()

def mid_points(p1,p2):
    return( (p1[0]+p2[0]) / 2, (p1[1] + p2[1]) /2 )
    
def sierpinski(points, degree, my_turtle):
    color_map = ['blue', 'red', 'green', 'white', 'yellow', 'violet', 'orange']
    
    draw_triangle(points, color_map[degree], my_turtle)
    if degree > 0:
        sierpinski([points[0],
                    mid_points(points[0],points[1]),
                    mid_points(points[0],points[2]),
                    degree - 1 ,my_turtle)
    
    sierpinski([points[1],
                    mid_points(points[1],points[0]),
                    mid_points(points[1],points[2]),
                    degree - 1 ,my_turtle)
    
    sierpinski([points[2],
                    mid_points(points[2],points[1]),
                    mid_points(points[0],points[2]),
                    degree - 1 ,my_turtle)

def main():
    my_turtle = turtle.Turtle()
    my_win = turtle.Screen()
    my_points = [[-100, -50],[0, 50],[100, -50]]
    sierpinski(my_points,3,my_turtle)
    my_win.exitonclick()

main()
