from turtle import Turtle, Screen
import random

is_race_on = False  # Flag to check
screen = Screen()
screen.setup(width=500, height=400)     #Setting screen size
screen.register_shape("sedan (1).gif")  #Registering different car shapes
screen.register_shape("sedan (2).gif")
screen.register_shape("sedan (3).gif")
screen.register_shape("sedan (4).gif")
screen.register_shape("sedan (5).gif")
screen.register_shape("sedan (6).gif")
shape = ["sedan (1).gif", "sedan (2).gif", "sedan (3).gif", "sedan (4).gif", "sedan (5).gif", "sedan (6).gif"]  #List of car shapes
colors = ["green", "violet", "blue", "black", "orange", "red"]  #List of car colors
all_turtles = []
for i in range(0, 6):
    new_turtle = Turtle(shape=shape[i]) #Creating new turtle object with shapes from list
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(-210, -60 + 30 * i) #Setting turtle position
    all_turtles.append(new_turtle)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")    #Taking user input
if user_bet:
    is_race_on = True
while is_race_on:   #Loop to move the turtle
    for turtle in all_turtles:  #Loop to move each turtle
        if turtle.xcor() > 230: #Checking if turtle has reached the finish line
            is_race_on = False  #Setting flag to false
            winning_color = turtle.pencolor()   #Getting the color of winning turtle
            if winning_color == user_bet:   #Checking if user has won the bet
                print("You've won the bet.")
                exit()
            else:
                print(f"You've lost the bet. {winning_color} turtle has won.")  #Printing the winning turtle color
                exit()

        random_distance = random.randint(0, 10) #Generating random distance to move the turtle
        turtle.forward(random_distance) #Moving the turtle

