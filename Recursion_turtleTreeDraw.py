import turtle
import random

def tree(branch_len, t):
    branch_len = random.randint(branch_len-4, branch_len+4)
    if branch_len > 5:
        degree1 = random.randint(5,65)
        t.pensize(branch_len/5)
        t.forward(branch_len)
        t.right(degree1)
        tree(branch_len-5, t)
        t.left(2*degree1)
        tree(branch_len - 5, t)
        t.right(degree1)
        if 5 < branch_len < 20:
            t.color("green")
        else:
            t.color("brown") 
            t.pensize(branch_len/5)
        t.backward(branch_len)
        
def main():
    t = turtle.Turtle()
    my_win = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    tree(35,t)
    my_win.exitonclick()
    
main()

