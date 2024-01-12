import tkinter as tk
import json
import turtle
import random

# Initialize turtle screen
screen = turtle.Screen()
screen.title("Turtle Race & Rock-Paper-Scissors")
screen.bgcolor("white")

# Create turtles for the race
player = turtle.Turtle()
player.shape("turtle")
player.color("red")
player.penup()
player.goto(-200, 50)

computer = turtle.Turtle()
computer.shape("turtle")
computer.color("green")
computer.penup()
computer.goto(-200, 0)

turtles = [player, computer]

# Create a turtle for the rock-paper-scissors interface
interface_turtle = turtle.Turtle()
interface_turtle.hideturtle()
interface_turtle.penup()
interface_turtle.goto(0, -150)

# Function to reset the turtles to their starting positions
def reset_turtles():
    for turtle in turtles:
        turtle.goto(-200, turtles.index(turtle) * 50)

# Function to simulate the turtle race
def run_race():
    for _ in range(150):
        for turtle in turtles:
            distance = random.randint(1, 5)
            turtle.forward(distance)

    # Reset turtles to starting positions
    reset_turtles()

'''def player_buff(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif user_choice == "rock" and computer_choice == "scissors":
        return "You Win!"
    elif user_choice == "paper" and computer_choice == "rock":
        return "You Win!"
    elif user_choice == "scissors" and computer_choice == "paper":
        return "You Win!"



def com_buff():'''

# Function for rock-paper-scissors game
def rock_paper_scissors():
    user_choice = screen.textinput("Rock-Paper-Scissors", "Enter your choice (rock, paper, or scissors): ").lower()
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)

    interface_turtle.clear()
    interface_turtle.write(f"Your choice: {user_choice}\nComputer's choice: {computer_choice}", align="center", font=("Arial", 14, "normal"))

    if user_choice == computer_choice:
        return "It's a tie!"
    elif user_choice == "rock" and computer_choice == "scissors":
        return "You Win!"
    elif user_choice == "paper" and computer_choice == "rock":
        return "You Win!"
    elif user_choice == "scissors" and computer_choice == "paper":
        return "You Win!"

    else:
        return "Computer wins!"
    player_buff(user_choice, computer_choice)

# Run the game three times with interludes
for i in range(3):
    print(f"\nRace {i + 1}")
    run_race()

    print("\nRock-Paper-Scissors Interlude")
    result = rock_paper_scissors()
    print(result)


# Keep the turtle graphics window open
screen.mainloop()
