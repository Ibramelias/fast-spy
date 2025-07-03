import turtle

screen = turtle.Screen()
screen.bgcolor('white')
screen.title('Turtle Shape Drawer')

#create a turtle
t = turtle.Turtle()
t.pensize(3)
t.speed(3)

#function to draw a square
def draw_square():
    for _ in range(4):
        t.forward(100)
        t.left(90)


#function to draw triangle
def draw_triangle():
    for _ in range(3):
        t.forward(100)
        t.left(120)


#function to draw circle
def draw_circle():
    t.circle(50)


#main menu
def show_menu():
    print("\n Choose a shape to draw")
    print("1- Draw a square")
    print("2- Draw a triangle")
    print("3- Draw a circle")
    print("4- Exit.")


#Command-line interaction
while True:
    choice = input('Enter your choice (1-4): ')
    t.clear()

    if choice == "1":
        draw_square()
    elif choice == "2":
        draw_triangle()
    elif choice == "3":
        draw_circle()
    elif choice == "4":
        print("Exiting....")
        break
    else:
        print("Invalid choice, Try again")


turtle.done()
