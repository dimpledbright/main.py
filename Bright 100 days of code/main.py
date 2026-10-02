# Day 6 FUNCTIONS & REBOORKS ROBOT GAME
# Functions

# def my_function():
#     print("Hello")
#     print("Bye")

# my_function 


# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()


# def jump()
#     turn_left()
#     move()
#     while not wall_on_right():
#         turn_right, move(), 
#     else:
#         move()


# while not at_goal():
#     if wall_in_front():
#         jump()
#     else:
#         move()


# while not at_goal:
#     if right_is_clear():
#         turn_right()
#         move()

#     elif front_is_clear():
#         move()

#     else:
#         turn_left()






# DAY 7 HANG-MAN GAME
# import random

# word_list = ["ardvack" , "baboon" , "camel"]
# chosen_word = random.choice(word_list)
# end_of_game = False
# word_lenght = len(chosen_word)
# lives = 6

# # print(f'Psst, the solution is {chosen_word}.')

# #Create Blanks
# display = []
# for _ in range(word_lenght):
#     display += "_"
# print(display)

# while not end_of_game:
#     guess = input("Guess a letter: ").lower()

#     if guess in display:
#         print(f"You've already guessed {guess}")

#     for position in range(word_lenght):
#         letter = chosen_word[position]
#         if letter == guess:
#             display[position] = letter

#     if guess not in chosen_word:
#         print(f"You guessed {guess} that's not in the word! You lose a life!")
#         lives -= 1

#         if lives == 0:
#             end_of_game = True
#             print("Out of Lives, GAMEOVER!!")

#     print(display)

#     if '_' not in display:
#         end_of_game = True
#         print("You Win")





        
# DAY 8 - FUNCTIONS WITH INPUTS
# Simple Function
# def greet():
#     print("Hello")
#     print("How do you do")
#     print("How is the weather today?")
# greet()


# Functions with Inputs
# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do{name}")
# greet_with_name("Bright")


# Functions with more than one input (Positional Argument)
# def greet_with(name, location):
#     print(f"Hello {name} ")
#     print(f"What is it like in {location} ")
# greet_with("Bright", "Ayobo")
    

 # Functions with more than one input (Keyword Argument)
# def greet_with(name, location):
#     print(f"Hello {name} ")
#     print(f"What is it like in {location} ")
# greet_with(location = "Ayobo", name = "Bright")


# Area Calculation
# import math

# def paint_calc(height, width, cover):
#     area = height * width 
#     number_of_cans = math.ceil(area/cover)
#     print(f"You'll need {number_of_cans} cans of paint")

# test_h = int(input("Height of wall => "))
# test_w = int(input("Width of wall => "))
# coverage = 5
# paint_calc (height=test_h, width=test_w, cover=coverage)


#CEASER CIPHER GAME
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 
#                 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 
#                 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 
#                 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


#Basic Cipher Code
# def encrypt(plain_text, shift_amount):
#     cipher_text = "  "
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position + shift_amount
#         cipher_text += alphabet[new_position]
#     print(f"The encoded text is {cipher_text}")


# def decrypt(cipher_text, shift_amount):
#     plain_text = ""
#     for letter in cipher_text:
#         position = alphabet.index(letter)
#         new_position = position - shift_amount
#         plain_text += alphabet[new_position]
#     print(f"The decoded text is {plain_text}")


# if direction == 'encode':
#     encrypt (plain_text=text, shift_amount=shift)
# elif direction == 'decode':
#     decrypt (cipher_text=text, shift_amount=shift)


#Advanced Cipher Code(With User Experience)
# def caesar(start_text, shift_amount, cipher_direction):
#     end_text = " "
#     if cipher_direction == 'decode':
#         shift_amount *= -1
#     for char in start_text:
#         if char in alphabet:
#             position = alphabet.index(char)
#             new_position = position + shift_amount
#             end_text += alphabet[new_position]
#         else:
#             end_text += char
#     print(f"Here's the {cipher_direction}d result: {end_text}")



# should_continue = True
# while should_continue:
#     direction = input("Type 'encode' to encrypt, type 'decode' to decrypt => \n")
#     text =  input("Type your message => \n").lower()
#     shift =  int(input("Type the shift number => \n"))
#     shift = shift % 25

#     caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

#     result = input("type 'yes' if you'd like to go again, otherwise type 'no' => ")

#     if result == 'no':
#         should_continue == False
#         print("Goodbye")


# DAY 9 - PYTHON DICTIONARIES AND NESTING
# student_scores = {
#     "Harry": 82,
#     "Ron": 78,
#     "Herminone": 91,
#     "Draco": 74,
#     "Neville": 62
# }

# student_grades = {}

# for student in student_scores:
#     scores = student_scores[student]
#     if scores > 90:
#         student_grades[student] = "Outstanding"
#     elif scores > 80:
#         student_grades[student] = "Exceeds Expectations"
#     elif scores > 70:
#         student_grades[student] = "Acceptable"
#     else:
#         student_grades[student] = "Fail"

# print(student_grades)

# Nesting dictionaries and lists
# travel_log = [
# {   
#     "country": "France",
#     "visits": 12,
#     "cities": ["Paris", "Lille", "Dijon"]
# },
# {   
#     "country": "Germany",
#     "visits": 4,
#     "cities": ["Berlin", "Harmburg", "Stuttgart"]
# }
# ]

# def add_new_country(country_visited, times_visited, cities_visited):
#     new_country = {}
#     new_country["country"] = country_visited
#     new_country["visits"] = times_visited
#     new_country["cities"] = cities_visited
#     travel_log.append(new_country)

# add_new_country("Russia", 2, ["Moscow", "Saint Petersberg"])
# print(travel_log)


#Blind Auction game
# bids = {}
# bidding_finished = False

# def find_highest_bidder(bidding_record):
#     highest_bid = 0
#     winner = " "
#     for bidder in bidding_record:
#         bid_amount = bidding_record[bidder]
#         if bid_amount > highest_bid:
#             highest_bid = bid_amount
#             winner = bidder
#     print(f"The winner is {bidder} with a bid amount of ${highest_bid}")

# while not bidding_finished:
#     name = input("what is your name => ")
#     price = int(input("How much are you bidding? => $"))
#     bids[name] = price
#     should_continue = input("Are they other bidders? type 'yes' to continue or 'no' to end \n")
#     if should_continue == "no":
#         bidding_finished = True
#         find_highest_bidder(bids)






#DAY 10
# Functions with output
# def format_name(f_name , l_name):
#     formatted_f_name = f_name.title
#     formatted_l_name = l_name.title
#     return f"{formatted_f_name} {formatted_l_name}"
# print(format_name("Osaze", "Bright"))


# A python calculator
# def add(n1, n2):
#     return n1 + n2

# def  subtract(n1, n2):
#     return n1 - n2

# def multiply(n1, n2):
#     return n1 * n2

# def divide(n1, n2):
#     return n1 / n2

# operations = {
#     "+" : add, 
#     "-" : subtract, 
#     "*" : multiply, 
#     "/" : divide
# }

# def calculator():
#     num1 = int(input("What's the first number? => "))
#     for symbols in operations:
#         print(symbols)
#     should_continue = True

#     while should_continue:
#         operation_symbol = input("Pick an operation => ")
#         num2 = int(input("What's the next number? => "))
#         calculation_function = operations[operation_symbol]
#         answer = calculation_function(num1, num2)

#         print(f"{num1} {operation_symbol} {num2} = {answer}")

#         if input(f"type 'yes' to continue calculating with {answer}, or type 'no' to start a new calculation => ") == "y":
#             num1 = answer
#         else:
#             should_continue = False
#             calculator()

# calculator()






# DAY 11(BLACK-JACK GAME)
# import random

# def deal_card():
#     '''Returns a random card from the pack'''
#     cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#     card = random.choice(cards)
#     return card

# def calculate_score(cards): 
#     '''Take a list of cards and return the score calculated frm the cards'''
#     if sum(cards) == 21 and len(cards) == 2:
#         return 0
    
#     if 11 in cards and sum(cards) == 21:
#         cards.remove(11)
#         cards.append(1)
#     return sum(cards)

# def compare(user_score, computer_score):
#     if user_score == computer_score:
#         return "Draw"
#     elif computer_score == 0:
#         return "Lose, Opponent has BlackJack"
#     elif user_score == 0:
#         return "Win with a BlackJack"
#     elif user_score > 21:
#         return "You went over, You Lose"
#     elif computer_score > 21:
#         return "Opponent went over, You Win"
#     elif user_score > computer_score:
#         return "You Win"
#     else:
#         return"You Lose"

# #Deal the computer and the user 2 cards each using deal_card()
# def play_game():
#     user_cards = []
#     computer_cards = []
#     is_game_over = False

#     for i in range(2):
#         user_cards.append(deal_card())
#         computer_cards.append(deal_card())

#     while not is_game_over:
#         user_score = calculate_score(user_cards)
#         computer_score = calculate_score(computer_cards)
#         print(f"Your cards => {user_cards}, Your score => {user_score}")
#         print(f"Computers first card => {computer_cards[0]}")


#         if user_score == 0 or computer_score == 0 or user_score > 21:
#             is_game_over = True
#         else:
#             user_should_deal = input("Type 'yes' to get another card, type 'no' to pass => ")
#             if user_should_deal == 'yes':
#                 user_cards.append(deal_card())
#             else:
#                 is_game_over = True

#     while computer_score != 0 and computer_score < 17:
#         computer_cards.append(deal_card())
#         computer_score = calculate_score(computer_cards)



#     print(f" Your final hand is => {user_cards}, Your final score is => {user_score}")
#     print(f" Computer's final hand is => {computer_cards}, Computer's final score is => {user_score}")
#     print(compare(user_score, computer_score))

# while input("Do you want to play agame of BlackJack? Type 'yes' or 'no' => ") == "yes":
#     play_game()






# DAY 12 - LOCAL, GLOBAL SCOPE AND NUMBER GUESSING GAME
# Local Scope

# def drink_portion():
#     portion_strenght = 2
#     print("portion_strenght")


#Global Scope
# player_health = 10

# def game():
#     def drink_portion():
#         portion_strength = 2
#         print(player_health)
    
#     drink_portion()

# print(player_health)


# Modifying Global Scope - (Best done ussing the "return" statement)
# enemies = 1

# def increase_enemies():
#     print(f"Enemies inside function {enemies}")
#     return enemies + 1

# enemies = increase_enemies()
# print(f"Enemies inside function {enemies}")


# NUMBER GUESSING GAME
# from random import randint

# EASY_LEVEL_TURNS = 10
# HARD_LEVEL_TURNS = 5


# def check_answer(user_guess, answer, turns):
#     '''Checks answer aganist guess. Returns the number of turns remaining'''
#     if user_guess > answer:
#         print("Too High")
#         return turns - 1
#     elif user_guess < answer:
#         print("Too Low")
#         return turns - 1
#     else:
#         print(f"You got it! the answer was {answer}")

# def set_difficulty():
#     level = input("Choose a difficulty. Type 'easy' or 'hard' => ")
#     if level == "easy":
#         return EASY_LEVEL_TURNS
#     else:
#         return HARD_LEVEL_TURNS


# def game():
#     print("Welcome to the Number Guessing Game!")
#     print("I'm thinking of a number between 1 and 100.")
#     answer = randint(1, 100)

#     turns = set_difficulty()
#     print(f"You have {turns} attempts remaining")
#     guess = 0
#     while guess != answer:
#         guess = int(input("Make a guess => "))
#         turns = check_answer(guess, answer, turns)
#         print(f"You have {turns} attempts remaining")
#         if turns == 0:
#             print("You've run out of guesses, You lose! HAHA FUCKIING LOSER!!")
#             return
#         elif guess != answer:
#             print("Guess Again")

# game()







# DAY 13 - DEBUGGING (HOW TO FIND AND FIX PROBLEMS)
# 1. Describe the problem

# 2. Reproduce the bug

# 3. Act as the computer and evaluate each license

# 4. Fixing errors and searching for red lines

# 5. Squash the bug with print statements
    
# 6. Using a debugger (Thonny or Python tutor)

# 7. Take a break or Ask a friend or Run the code often or ask StackOverflow






# DAY 14 - HIGHER OR LOWER GAME
# from art import logo, vs
# from game_data import data
# import random
# import os


# #Format the acct data into printable format
# def format_data(account):
#     '''Takes the account data and returns the printable format'''
#     account_name = account["name"]
#     account_descr = account["description"]
#     account_country = account["country"]
#     return f"{account_name}, a {account_descr}, from {account_country}."

# def check_answer(guess, a_followers, b_followers):
#     '''Takes the user guess and follower count and returns if they got it right'''
#     if a_followers > b_followers:
#         return guess == "a"
#     else:
#         return guess == "b"

# print(logo)
# score = 0
# game_should_continue = True
# account_b = random.choice(data)


# while game_should_continue:
#     #Generate a random acct from Game Data
#     account_a = account_b
#     account_b = random.choice(data)
#     if account_a == account_b:
#         account_b = random.choice(data)

#     print(f"Compare A => {format_data(account_a)}.")
#     print(vs)
#     print(f"Aganist B => {format_data(account_b)}.")

#     #Ask the user for a guess
#     guess = input("Who has more followers 'A' or 'B'? => ").lower

#     #To check if user guess is correct
#     #Get the follower count of each account
#     a_follower_count = account_a["follower_count"]
#     b_follower_count = account_b["follower_count"]
#     #Then use an if statement to check if user is correct as we've done using the defined function above and call the function below
#     is_correct = check_answer(guess, a_follower_count, b_follower_count)

#     os.system('cls' if os.name == 'nt' else 'clear')
#     print(logo)

#     #Give user feedback on their guess
#     #keep track of their score
#     if is_correct:
#         score += 2
#         print(f"You're right!. Your current score is : {score}")
#     else:
#         game_should_continue = False
#         print(f"Sorry, that's wrong. Your final score is : {score}")












    
#INTERMEDIATE STAGE
#DAY 15 - COFFEE VENDING MACHINE
# MENU = {
#     "espresso": {
#         "ingredients": {
#             "water" : 50,
#             "coffee" : 18,
#         },
#         "cost" : 1.5,
#     },

#     "latte" : {
#         "ingredients": {
#             "water" : 200,
#             "milk" : 150,
#             "coffee" : 24,
#         },
#         "cost" : 2.5,
#     },

#     "cappuccino" : {
#         "ingredients": {
#             "water" : 250,
#             "milk" : 100,
#             "coffee" : 24,
#         },
#         "cost" : 3.0,
#     }
# }

# profit = 0

# resources = {
#     "water" : 300,
#     "milk" : 200,
#     "coffee" : 100,
# }


# def is_resource_sufficient(order_ingredients):
#     ''' Returns True when order can be made, False if ingredients are insufficient '''
#     for item in order_ingredients:
#         if order_ingredients[item] >= resources[item]:
#             print(f"Sorry there is not enough {item}")
#             return False
#     return True 


# def process_coins():
#     ''' Returns the total calculated from coins inserted '''
#     print("Please inseert coins")
#     total = int(input("How many quarters?: ")) * 0.25
#     total += int(input("How many dimes?: ")) * 0.1
#     total += int(input("How many nickles?: ")) * 0.05
#     total += int(input("How many pennies?: ")) * 0.01
#     return total


# def is_transaction_successful(money_received, drink_cost):
#     ''' Returns True if money is accepted or False if money is insufficient '''
#     change = round(money_received - drink_cost, 2)
#     print(f"Processing... Here is ${change} in change")
#     if money_received >= drink_cost:
#         global profit
#         profit += drink_cost
#         return True
#     else:
#         print("Sorry thats not enough money. Money Refunded.")
#         return False
    
# def make_coffee(drink_name, order_ingredients):
#     ''' Deduct the required ingredients from the resources '''
#     for item in order_ingredients:
#         resources[item] -= order_ingredients[item]
#         print(f"Here's your {drink_name}. Enjoy!!!")


# is_on = True
# while is_on:
#     choice = input("What would you like? (espresso, latte or cappuccino) => ")
#     if choice == "off":
#         is_on = False
#     elif choice == "report":
#         print(f"Water: {resources['water']}ml")
#         print(f"Milk: {resources['milk']}ml")
#         print(f"Coffee: {resources['coffee']}g")
#         print(f"Money:${profit}")
#     else:
#         drink = MENU[choice]
#         if is_resource_sufficient(drink["ingredients"]):
#             payment = process_coins()
#             if is_transaction_successful(payment, drink["cost"]):
#                 make_coffee(choice, drink["ingredients"])









#DAY 16 - OBJECT ORIENTED PROGRAMMING (OOP)
# from turtle import Turtle, Screen
# timmy = Turtle()

# is_on = True
# while is_on:
#     print(timmy)
#     timmy.shape("turtle")
#     timmy.color("coral")
#     timmy.forward(100)
#     timmy.left(100)
#     timmy.forward(100)
#     timmy.color("blue")

# my_screen = Screen()
# print(my_screen.canvheight) 
# my_screen.exitonclick()



# - COFFEE MAKER USING OBJECT ORIENTED PROGRAMMING
# from menu import Menu, MenuItem
# from coffee_maker import CoffeeMaker
# from money_machine import MoneyMachine

# money_machine = MoneyMachine()
# coffee_maker = CoffeeMaker()
# menu = Menu()

# is_on = True

# coffee_maker.report()
# money_machine.report()

# while is_on:
#     options = menu.get_items()
#     choice = input(f"What would you like? ({options}) => ")
#     if choice == "off":
#         is_on = False
#     elif choice == "report":
#         coffee_maker.report()
#         money_machine.report()
#     else:
#         drink = menu.find_drink(choice)
#         is_enough_ingredient = coffee_maker.is_resource_sufficient(drink)
#         is_payment_successful = money_machine.make_payment(drink.cost)
#         if is_enough_ingredient and is_payment_successful:
#             coffee_maker.make_coffee(drink)









# # DAY 17 - THE QUIZ MAKER AND BENEFITS OF OOP
# from quiz_data import question_data
# from question_model import Question
# from quiz_brain import QuizBrain

# question_bank = []
# for question in question_data:
#     question_text = question["text"]
#     question_answer = question["answer"]
#     new_question = Question(question_text, question_answer)
#     question_bank.append(new_question)

# quiz = QuizBrain(question_bank)

# while quiz.still_has_questions():
#     quiz.next_question()

# print("You've completed the quiz")
# print(f"Your final score is {quiz.score}/{quiz.question_number}")



# DAY - 18



# DAY - 19 (MAKING A TURTLE RACING GAME WITH MULTIPLE OBJECT AND INSTANCES)

# Creating Etch A Sketch app
# from turtle import Turtle, Screen
#
# tim = Turtle()
# screen = Screen()
#
# def move_forwards():
#     tim.forward(10)
#
# def move_backwards():
#     tim.backward(10)
#
# def turn_right():
#     new_heading = tim.heading() + 10
#     tim.setheading(new_heading)
#
# def turn_left():
#     new_heading = tim.heading() - 10
#     tim.setheading(new_heading)
#
# def clear():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()


# screen.listen()
# screen.onkey(move_forwards, "w")
# screen.onkey(move_backwards, "s")
# screen.onkey(turn_left, "a")
# screen.onkey(turn_right, "d")
# screen.onkey(clear, "c")
# screen.exitonclick()


#Turtle Racing Game
# from turtle import Turtle, Screen
# import random

# is_race_on = False
# screen = Screen()
# screen.setup(width = 500, height = 400)
# user_bet = screen.textinput(title = "Make your bet", prompt = "Which turtle will win the race? Choose a color => ")
# colors = ["red", "orange", "yellow", "green", "blue", "purple"]
# y_positions = [-70, -30, 10, 50, 90, 130]
# all_turtles = []


# for turtle_index in range(0, 6):
#     new_turtle = Turtle(shape ="turtle")
#     new_turtle.color(colors[turtle_index])
#     new_turtle.penup()
#     new_turtle.goto(x = -230, y = y_positions[turtle_index])
#     all_turtles.append(new_turtle)

# if user_bet:
#     is_race_on = True

# while is_race_on:

#     for turtle in all_turtles:
#         if turtle.xcor() > 230:
#             is_race_on = False
#             winning_color = turtle.pencolor()
#             if winning_color == user_bet:
#                 print(f"You've won! The {winning_color} turtle is the winner!")
#             else:
#                 print(f"You Lost! The {winning_color} turtle is the winner!")

#         random_distance = random.randint(0, 10)
#         turtle.forward(random_distance)









# DAY 21 - (LEARNING CLASS INHERITANCE / BUILDING A SNAKE GAME)
# class Animal:
#     def __init__(self):
#         self.num_eyes = 2

#     def breathe(self):
#         print("Inhale and Exhale")


# class Fish(Animal):
#     def __init__(self):
#         super().__init__()

#     def swim(self):
#         print("is moving")

# nemo = Fish()
# nemo.swim()
# nemo.breathe()
# print(nemo.num_eyes)




#Building a snake game
# from turtle import Screen
# import time
# from scoreboard import Scoreboard
# from snake import Snake
# from food import Food

# screen = Screen()
# screen.setup(width = 600, height = 600)
# screen.bgcolor("black")
# screen.title("My Snake Game")
# screen.tracer(0)

# snake = Snake()
# food = Food()
# scoreboard = Scoreboard()

# screen.listen()
# screen.onkey(snake.up, "Up")
# screen.onkey(snake.down, "Down")
# screen.onkey(snake.left, "Left")
# screen.onkey(snake.right, "Right")

# game_is_on = True
# while game_is_on:
#     screen.update()
#     time.sleep(0.1)
#     snake.move()

#       #TO DETECT COLLISION WITH FOOD
#     if snake.head.distance(food) < 15:
#         food.refresh()
#         snake.extend()
#         scoreboard.increase_score()

#       #TO DETECT COLLISION WITH WALL
#     if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
#         scoreboard.reset()
#         snake.reset()

#       #TO DETECT COLLISION WITH BODY
#     for segments in snake.segments:
#         if segments == snake.head:
#             pass
#         elif snake.head.distance(segments) < 10:
#             scoreboard.reset()
#             snake.reset()
            


# screen.exitonclick()









# DAY 22 - BUILDING A PONG GAME
# from turtle import Screen

# from ball import Ball
# from paddle import Paddle
# from pongscoreboard import Scoreboard
# import time

# screen = Screen()
# screen.setup(width=800, height=600)
# screen.bgcolor("black")
# screen.title("My Pong Game")
# screen.tracer(0)

# r_paddle = Paddle((350, 0))
# l_paddle = Paddle((-350, 0))

# screen  = Screen()
# ball = Ball()
# scoreboard = Scoreboard()

# screen.listen()
# screen.onkey(r_paddle.go_up, "Up")
# screen.onkey(r_paddle.go_down, "Down")
# screen.onkey(l_paddle.go_up, "a")
# screen.onkey(l_paddle.go_down, "z")

# game_is_on = True
# while game_is_on:
#     time.sleep(ball.move_speed)
#     screen.update()
#     ball.move()

#     #Detect collision with wall
#     if ball.ycor() > 280 or ball.ycor() < -280:
#         ball.bounce_y()

#     #Detect collision with paddle
#     if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
#         ball.bounce_x()

#     #Detect if right paddle misses
#     if ball.xcor() > 380:
#         ball.reset_position()
#         scoreboard.l_point()


#     #Detect if left paddle misses
#     if ball.xcor() < -380:
#         ball.reset_position()
#         scoreboard.r_point()


# screen.exitonclick()










# DAY 23 - TURTLE CAR CROSSING GAME
# import time
# from turtle import Screen
# from player import Player
# from car_manager import CarManager
# from car_scoreboard import Scoreboard

# screen = Screen()
# screen.setup(width=600, height=600)
# screen.title("Car Crossing Game")
# screen.tracer(0)

# player = Player()
# car_manager = CarManager()
# car_scoreboard = Scoreboard()

# screen.listen()
# screen.onkey(player.go_up,"Up")
# screen.onkey(player.go_down, "Down")


# game_is_on = True
# while game_is_on:
#     time.sleep(0.1)
#     screen.update()

#     car_manager.create_car()
#     car_manager.move_cars()

#     #Detect collision with car
#     for car in car_manager.all_cars:
#         if car.distance(player) < 20:
#             game_is_on = False
#             car_scoreboard.game_over()

#     #Detect successful crossing
#     if player.is_at_finish_line():
#         player.go_to_start()
#         car_manager.level_up()
#         car_scoreboard.increase_level()


# screen.exitonclick()










# DAY 24 -  DEALING WITH FILES, PATHS AND DIRECTORIES
# with open("my_file.txt", mode = "w") as file:
#     file.write("Hello, My name is Bright. \n I am 12 years old. \n My favourite food is a bowl of hot noodles")

# with open("/Users/User/Desktop/my_file.txt") as file:
#     content = file.read()
#     print(content)

# with open("my_file.txt", mode="a") as file:
#     file.write("\n Hello World, This is my new text")

# with open("new_file.txt", mode="w") as file:
#     file.write("Hello World, this is for the new text file")









#DAY - 25 (WORKING WITH CSV DATAS AND THE PANDA LIBRARY)

#To readlines between the data files
# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)


# #To use the python built in csv module to print out only the temperature
# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#     print(temperature)



#How to use the python pandas modules

# data = pandas.read_csv("weather_data.csv")
# print(data)
# print(data["temp"])

# To use pandas to get the full data as a dict
# data = pandas.read_csv("weather_data.csv")
# data_dict = data.to_dict()
# print(data_dict)
#
# #To use pandas to get the list of temperature
# data = pandas.read_csv("weather_data.csv")
# temp_list = data["temp"].to_list()
# print(temp_list)
#
# #To use pandas to find the mean of the temperature
# data = pandas.read_csv("weather_data.csv")
# mean = data["temp"].mean()
# print(mean)
#
# #To use pandas to find the max no in temperature
# data = pandas.read_csv("weather_data.csv")
# max = data["temp"].max()
# print(max)

#To get data in columns
# data = pandas.read_csv("./data.csv")
# print(data.condition)

#To get data in rows
# data = pandas.read_csv("./data.csv")
# print(data[data.day == "Monday"])

#Create a dataframe from scratch
# data_dict = {
#     "students" : ["Amy", "James", "Angela"],
#     "scores" : [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# print(data)



#The US Squirrel Cencus Game
# import pandas

# data = pandas.read_csv("004 2018-Central-Park-Squirrel-Census-Squirrel-Data.csv")

# grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
# red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
# black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
# print(grey_squirrels_count)
# print(red_squirrels_count)
# print(black_squirrels_count)

# data_dict = {
#     "Fur Color": ["Gray", "Cinnamon", "Black"],
#     "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
# }

# data_frame = pandas.DataFrame(data_dict)
# data_frame.to_csv("squirrel_count.csv")



#The US States-Map Game
# import turtle
# import pandas

# screen = turtle.Screen()
# screen.title("U.S. States Game") 
# image = "blank_states_img.gif"
# screen.addshape(image)
# turtle.shape(image)


# data = pandas.read_csv("50_states.csv")
# all_states = data.state.to_list()
# guessed_states = []

# while len(guessed_states) < 50:
#     answer_state = screen.textinput(title = f"{len(guessed_states)}/50 States Correct", prompt = "What's is another state's name?").title()


#     if answer_state == "Exit":
#         missing_states = [state for state in all_states if state not in guessed_state]
#         new_data = pandas.DataFrame(missing_states)
#         new_data.to_csv("states_to_learn.csv")
#         break
#     
#      if answer_state in all_states:
#         guessed_states.append(answer_state)
#         t = turtle.Turtle()
#         t.hideturtle()
#         t.penup()
#         state_data = data[data.state == answer_state]
#         t.goto(int(state_data.x), int(state_data.y))
#         t.write(answer_state, font=("Arial", 20, "bold"))









# DAY - 26 (LIST n DICT COMPREHENSON AND NATO ALPHABET)
#List Comprehension
# numbers = [1, 2, 3]
# new_numbers = [n + 1 for n in numbers]

# #String as List
# name = 'Angela'
# letters_list = [letter for letter in name]

# #Range as list
# range_list = [num * 2 for num in range(1, 5)]

# #Conditional List Comprehension
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# short_names = [name for name in names if len(name) < 5 ]
# long_names = [name.upper() for name in names if len(name) > 5]

# #Conditional List Comprehension with different separate files
# with open("file1.txt") as file1:
#     first_file = file1.readlines()
# with open("file2.txt") as file2:
#     second_file = file2.readlines()

# result = [int(num) for num in first_file if num in second_file]

# print(result)

#Dictionary Comprehension
# import random
# names  = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# student_scores = {student:random.randint(10, 100) for student in names}
# print(student_scores)

# #Conditional Dictionary Comprehension
# passed_student = {student:score for (student, score) in student_scores.items() if score >= 60}
# print(passed_student)

#Dictionary Comprehension without using a Loop 1
# sentence = "What is the Air Speed Velocity of an Unladen Swallow"
# result = {word:len(word) for word in sentence.split()} 
# print(result)


#Dictionary Comprehension without using a Loop 2
# weather_c = {
#     "Monday" : 12, 
#     "Tuesday" : 14, 
#     "Wednesday" : 15, 
#     "Thursday" : 14, 
#     "Friday" : 21, 
#     "Saturday" : 22, 
#     "Sunday" : 24
# }

# weather_f = {days:temp_c * 9/5 + 32 for (days, temp_c) in weather_c.items()}
# print (weather_f)

#How to use a loop to iterate over a pandas DataFrame
# student_dict = {
#     "student" : ["Angela", "James", "Lily"],
#     "scores" : [56, 76, 98]
# }
#doing it normally
# for(key, value) in student_dict.items():
#     print(key)
#     print(value)

#using pandas
# import pandas 
# student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

#using pandas to loop through rows of a DataFrame
# for (index, row) in student_data_frame.iterrows():
#     print(row.student)


# NATO Alphabets
# import pandas

# data = pandas.read_csv("nato_phonetic_alphabet.csv")
# #TODO 1. Create a dictionary in this format:
# phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

# #TODO 2. Create a list of the phonetic code words from a word that the user inputs.

# def generate_phonetic():
#     word = input("Enter a word: ").upper()
#     try:
#         output_list = [phonetic_dict[letter] for letter in word]
#     except KeyError:
#         print("Sorry, only letters in the alphabet please")
#         generate_phonetic()
#     else:
#         print(output_list)

# generate_phonetic()









# DAY - 27 (GUIs AND TKINTER)
# import tkinter
#
# window = tkinter.Tk()
# window.title("My First GUI Program")
# window.minsize(500, 300)
# window.config(padx = 100, pady = 100)
#
# #Label
# my_label = tkinter.Label(text = "I am a Label", font=("Arial", 24, "normal"))
# my_label.grid(column = 0, row = 0)
# my_label.config(padx = 50, pady = 50)
#
# #Button on tkinter
# def button_clicked():
#     # my_label.config(text = "Button got clicked")
#
#     #To trigger the button to get the word in the text box
#     new_text = input.get()
#     my_label.config(text=new_text)
#
# button = tkinter.Button(text = "Click me", command = button_clicked)
# button.grid(row = 1, column = 1)
#
# #Entry on tkinter
# input = tkinter.Entry()
# input.grid(row = 2, column = 2)
#
# #New Button
# new_button = tkinter.Button(text = "New Button", command = button_clicked)
# new_button.grid(row = 0, column = 2)
#
#
# window.mainloop()



#Miles to Kilometer Converter Using Tkinter
# from tkinter import *

# window = Tk()
# window.title("Miles to Km Converter")
# window.config(padx = 20, pady = 20)

# def miles_to_km():
#     miles = float(miles_input.get())
#     km = round(miles * 1.609)
#     kilometer_result_label.config(text = f"{km}")


# miles_input = Entry(width = 10)
# miles_input.grid(column = 1, row = 0)

# miles_label = Label(text = "Miles", font = ("Arial", 10, "bold"))
# miles_label.grid(column = 2, row = 0)

# is_equal_label = Label(text = "is equal to")
# is_equal_label.grid(column = 0, row = 1)

# kilometer_result_label = Label(text = "0")
# kilometer_result_label.grid(column = 1, row = 1)

# kilometer_label = Label(text = "Km", font = ("Arial", 10, "bold"))
# kilometer_label.grid(column = 2, row = 1)

# calculate_button = Button(text="Calculate", command=miles_to_km)
# calculate_button.grid(column = 1, row = 2)


# window.mainloop()







# DAY 28 - DYNAMIC TYPING AND POMODORO GUI APPLICATION
# from tkinter import *
# import math
# # ---------------------------- CONSTANTS ------------------------------- #
# PINK = "#e2979c"
# RED = "#e7305b"
# GREEN = "#9bdeac"
# YELLOW = "#f7f5dd"
# FONT_NAME = "Courier"
# WORK_MIN = 25
# SHORT_BREAK_MIN = 5
# LONG_BREAK_MIN = 20
# reps = 0
# timer = None

# # ---------------------------- TIMER RESET ------------------------------- # 

# def reset_timer():
#     window.after_cancel(timer)
#     canvas.itemconfig(timer_text, text="00:00")
#     title_label.config(text="Timer", fg=GREEN)
#     check_marks.config(text="")
#     global reps
#     reps = 0

# # ---------------------------- TIMER MECHANISM ------------------------------- # 
# def start_timer():
#     global reps
#     reps += 1

#     work_sec = WORK_MIN * 60
#     short_break_sec = SHORT_BREAK_MIN * 60
#     long_break_sec = LONG_BREAK_MIN * 60

#     if reps % 8 == 0:
#         count_down(long_break_sec)
#         title_label.config(text="Long Break", fg=RED)
#     elif reps % 2 == 0:
#         count_down(short_break_sec)
#         title_label.config(text="Break", fg=PINK)
#     else:
#         count_down(work_sec)
#         title_label.config(text="Work", fg=GREEN)
# # ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
# def count_down(count):

#     count_min = math.floor(count / 60)
#     count_sec = count % 60
#     if count_sec < 10:
#         count_sec = f"0{count_sec}"

#     canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
#     if count > 0:
#         global timer
#         timer = window.after(1000, count_down, count - 1)
#     else:
#         start_timer()
#         marks = ""
#         work_sessions  = math.floor(reps / 2)
#         for _ in range(work_sessions):
#             marks += "✓"
#         check_marks.config(text=marks)

# # ---------------------------- UI SETUP ------------------------------- #
# window = Tk()
# window.title("My Pomodoro App")
# window.config(padx=100, pady=50, bg=YELLOW)

# title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40))
# title_label.grid(column=1, row=0)

# canvas = Canvas(width = 200, height = 224, bg=YELLOW, highlightthickness=0)
# tomato_img = PhotoImage(file="tomato.png")
# canvas.create_image(100, 112, image = tomato_img)
# timer_text = canvas.create_text(100, 132, text = "00:00", fill = "white", font= (FONT_NAME, 32, "bold"))
# canvas.grid(column=1, row=1)

# start_button = Button(text="Start", highlightthickness=0, command=start_timer)
# start_button.grid(column=0, row=2)

# reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
# reset_button.grid(column=2, row=2)

# check_marks = Label(fg=GREEN, bg=YELLOW)
# check_marks.grid(column=1, row=3)


# window.mainloop()










# DAY 29 - BUILDING A PASSWORD MANAGER GUI APP WITH TKINTER
# from tkinter import *
# from tkinter import messagebox
# from random import choice, randint, shuffle
# import pyperclip
# import json

# # ---------------------------- PASSWORD GENERATOR ------------------------------- #

# def generate_password():
#     letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#     numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#     symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#     password_letters = [choice(letters) for _ in range(randint(8, 10))]
#     password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
#     password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

#     password_list = password_letters + password_symbols + password_numbers
#     shuffle(password_list)

#     password = "".join(password_list)
#     password_input.insert(0, password)

#     pyperclip.copy(password)

# # ---------------------------- SAVE PASSWORD ------------------------------- #

# def save():

#     website = website_input.get()
#     email = email_input.get()
#     password = password_input.get()
#     new_data = {
#         website: {
#             "email" : email, 
#             "password" : password
#         }
#     }

#     if website == "" or email == "" or password == "":
#         messagebox.showerror(title="Error", message="Please don't leave any fields empty!")
#         return
#     else:
#         try:
#             with open("data.json", "r") as data_file:
#                 #Reading old data
#                 data = json.load(data_file)
#         except FileNotFoundError:
#             with open("data.json", "w") as data_file:
#                 json.dump(new_data, data_file, indent=4)
#         else:
#             #Updating old data with new data
#             data.update(new_data)

#             with open("data.json", "w") as data_file:
#                 #Saving updated data
#                 json.dump(data, data_file, indent=4)
#         finally:
#             website_input.delete(0, END)
#             password_input.delete(0, END)

# # ---------------------------- FIND PASSWORD ------------------------------- #

# def find_password():
#     website = website_input.get()
#     try:
#         with open("data.json") as data_file:
#             data = json.load(data_file)
#     except FileNotFoundError:
#         messagebox.showinfo(title="Error", message="No Data File Found")
#     else:
#         if website in data:
#             email = data[website]["email"]
#             password = data[website]["password"]
#             messagebox.showinfo(title=website, message=f"Email: {email} \n Password: {password}")
#         else:
#             messagebox.showinfo(title="Error", message=f"No details for {website} exists")

# # ---------------------------- UI SETUP ------------------------------- #

# windows = Tk()
# windows.title("Password Manager")
# windows.config(padx=50, pady=50)

# canvas = Canvas(width = 200, height = 200)
# lock_photo = PhotoImage(file="logo.png")
# canvas.create_image(100, 100, image=lock_photo)
# canvas.grid(row=0, column=1)

# #labels
# website_label = Label(text = "Website:")
# website_label.grid(row=1, column=0)

# email_label = Label(text = "Email/Username:")
# email_label.grid(row=2, column=0)

# password_label = Label(text = "Password:")
# password_label.grid(row=3, column=0)

# #Entries
# website_input = Entry(width = 34)
# website_input.grid(row=1, column=1)
# website_input.focus()

# email_input = Entry(width = 57)
# email_input.grid(row=2, column=1, columnspan=2)
# email_input.insert(0, "edoborbright2002@gmail.com")

# password_input = Entry(width = 34)
# password_input.grid(row=3, column=1)

# #Buttons
# search_button = Button(text="Search", width=18, command=find_password)
# search_button.grid(row=1, column=2)

# gen_pass = Button(text= "Generate Password", width=18, command=generate_password)
# gen_pass.grid(row=3, column=2)

# add_button = Button(text="Add", width=48, command=save)
# add_button.grid(row=4, column=1, columnspan=2)


# windows.mainloop()









# DAY 30 - ERRORS, EXCEPTIONS and JSON DATA
#FileNotFound
# with open("a_file.txt") as file:
#     file.read()

# #keyError
# a_dictionary = {"key" : "value"}
# value = a_dictionary["non_existent_key"]

# #IndexError
# fruit_list = ["apple", "banana", "orange"]
# fruit = fruit_list[3]

# #TypeError
# text = "abc"
# print(text + 5)


# #Catching Exceptions
# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key" : "value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()

# #To work with JSON Files
# import json
# #To Write to files
# json.dump

# #To Read files
# json.load

# #To Update files
# json.update










# DAY 31 - FLASH CARD APP, CAP STONE PROJECT
# from tkinter import *
# import pandas
# import random

# BACKGROUND_COLOR = "#B1DDC6"
# current_card = {}
# to_learn = {}

# try:
#     data = pandas.read_csv("data/words_to_learn.csv")
# except FileNotFoundError:
#     original_data = pandas.read_csv("data/french_words.csv")
#     to_learn = original_data.to_dict(orient="records")
# else:
#     to_learn = data.to_dict(orient="records")


# def next_card():
#     global current_card, flip_timer
#     window.after_cancel(flip_timer)
#     current_card = random.choice(to_learn)
#     canvas.itemconfig(card_title, text="French", fill="black")
#     canvas.itemconfig(card_word, text=current_card["French"], fill="black")
#     canvas.itemconfig(card_background, image=card_front_img)
#     flip_timer = window.after(3000, func=flip_card)


# def flip_card():
#     canvas.itemconfig(card_title, text="English", fill="white")
#     canvas.itemconfig(card_word, text=current_card["English"], fill="white")
#     canvas.itemconfig(card_background, image=card_back_img)

# def is_known():
#     to_learn.remove(current_card)
#     data = pandas.DataFrame(to_learn)
#     data.to_csv("data/words_to_learn.csv", index=False)

# window = Tk()
# window.title("Flashy")
# window.configure(padx=50, pady=50, bg=BACKGROUND_COLOR)

# flip_timer = window.after(3000, func=flip_card)

# canvas = Canvas(width=800, height=526)
# card_front_img = PhotoImage(file="images/card_front.png")
# card_back_img = PhotoImage(file="images/card_back.png")
# card_background = canvas.create_image(400, 263, image=card_front_img)
# card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
# card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
# canvas.configure(bg=BACKGROUND_COLOR, highlightthickness=0)
# canvas.grid(row=0, column=0, columnspan=2)

# cross_image = PhotoImage(file="images/wrong.png")
# unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
# unknown_button.grid(row=1, column=0)

# check_image = PhotoImage(file="images/right.png")
# known_button = Button(image=check_image, highlightthickness=0, command=is_known)
# known_button.grid(row=1, column=1)

# next_card()

# window.mainloop()









# # DAY 32 - SEND E-MAILS AND MANAGE DATETIME
# import smtplib

# my_email = "brightbetinfo@gmail.com"
# password = "dcoxnexocuqbttzt"


# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email, 
#         to_addrs="edoborbright2002@yahoo.com", 
#         msg="Subject:Hello\n\nThis is the body of my email"
#     )


# import datetime as dt

# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()

# date_of_birth = dt.datetime(year=1995, month=12, day=15, hour=4)
# print(date_of_birth)

#SENDING RANDOM QUOTES VIA EMAILS
# import smtplib
# import datetime as dt
# import random

# MY_EMAIL = "osazebright2002@gmail.com"
# MY_PASSWORD = "wgyseclerygkzcvr"

# now = dt.datetime.now()
# weekday = now.weekday
# if weekday == 3:
#     with open("quotes.txt") as quotes_file:
#         all_quotes = quotes_file.readlines
#         quotes = random.choice(all_quotes)
#         print(quotes)

#     with smtplib.SMPT("smpt.gmail.com") as connection:
#         connection.starttls()
#         connection.login(MY_EMAIL, MY_PASSWORD)
#         connection.sendmail(
#             from_addr=MY_EMAIL, 
#             to_addrs=MY_EMAIL, 
#             msg=f"Subject:MONDAY MOTIVATION\n\n{quotes}"
#         )
#         print(quotes)


#SENDING AUTOMATED HAPPY BIRTHDAYS VIA EMAIL
# from datetime import datetime
# import pandas
# import random
# import smtplib

# MY_EMAIL = "osazebright2002@gmail.com"
# MY_PASSWORD = "xexyuyzrujuuondc"

# today = datetime.now()
# today_tuple = (today.month, today.day)

# data = pandas.read_csv("birthdays.csv")
# birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
# if today_tuple in birthdays_dict:
#     birthday_person = birthdays_dict[today_tuple]
#     file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
#     with open(file_path) as letter_file:
#         contents = letter_file.read()
#         contents = contents.replace("[NAME]", birthday_person["name"])

#     with smtplib.SMTP("smtp.gmail.com") as connection:
#         connection.starttls()
#         connection.login(MY_EMAIL, MY_PASSWORD)
#         connection.sendmail(
#             from_addr=MY_EMAIL,
#             to_addrs=birthday_person["email"],
#             msg=f"Subject:Happy Birthday!\n\n{contents}"
#         )













#DAY 33 - API ENDPOINT, API PARAMETERS and ISS OVERHEAD NOTIFYER

# import requests

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()

# data = response.json()

# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]

# iss_position = [longitude, latitude]

# print(iss_position)



#KANYE QUOTES API 
# from tkinter import *
# import requests


# def get_quote():
#     response = requests.get(url="https://api.kanye.rest")
#     response.raise_for_status()
#     data = response.json()
#     quote = data["quote"]
#     canvas.itemconfig(quote_text, text=quote)


# window = Tk()
# window.title("Kanye Says...")
# window.config(padx=50, pady=50)

# canvas = Canvas(width=300, height=414)
# background_img = PhotoImage(file="background.png")
# canvas.create_image(150, 207, image=background_img)
# quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
# canvas.grid(row=0, column=0)

# kanye_img = PhotoImage(file="kanye.png")
# kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
# kanye_button.grid(row=1, column=0)


# window.mainloop()




#ISS NIGHT-SKY CHECKER
# import requests
# from datetime import datetime
# import smtplib
# import time

# MY_EMAIL = "osazebright2002@gmail.com"
# MY_PASSWORD = "xexyuyzrujuuondc"

# MY_LAT = 6.600574
# MY_LONG = 3.244364


# def is_iss_overhead():
#     response = requests.get(url="https://api.open-notify.org/iss-now.json")
#     response.raise_for_status()
#     data = response.json()

#     iss_latitude = float(data["iss_position"]["latitude"])
#     iss_longitude = float(data["iss_position"]["longitude"])

#     if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
#         return True


# def is_night():
#     parameters = {
#         "lat": MY_LAT,
#         "lng": MY_LONG,
#         "formatted": 0,
#     }

#     response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
#     response.raise_for_status()
#     data = response.json()

#     sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
#     sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

#     time_now = datetime.now().hour

#     if time_now >= sunset or time_now <= sunrise:
#         return True

# while True:
#     time.sleep(60)
#     if is_iss_overhead() and is_night():
#         connection = smtplib.SMTP("smtp.gmail.com")
#         connection.starttls()
#         connection.login(MY_EMAIL, MY_PASSWORD)
#         connection.sendmail(
#             from_addr = MY_EMAIL,
#             to_addrs = MY_EMAIL,
#             msg="Subject: LOOK UP!!!!\n\n The ISS is above you in the sky."
#         )














#DAY 34 - API x GUI PRACTICE MAKING A QUIZZER WITH TKINTER
# from question_model_quizzer import Question
# from data import question_data
# from quiz_brain_quizzer import QuizBrain
# from ui import QuizInterface

# question_bank = []
# for question in question_data:
#     question_text = question["question"]
#     question_answer = question["correct_answer"]
#     new_question = Question(question_text, question_answer)
#     question_bank.append(new_question)


# quiz = QuizBrain(question_bank)
# quiz_ui = QuizInterface(quiz)

# print("You've completed the quiz")
# print(f"Your final score was: {quiz.score}/{quiz.question_number}")












#DAY 35 - API KEYS, AUTHENTICATION, ENVIRONMENT VARIABLES AND SENDING SMS
# import requests

# OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
# api_key = "7c19a4646015a29bfec4e64b5105b1e5"

# weather_params = {
#     "lat" : 51.507351,
#     "lon" : -0.127758,
#     "appid" : api_key,
# }

# response = requests.get(OWM_Endpoint, params=weather_params)
# response.raise_for_status()
# weather_data = response.json()

# will_rain = False
# for hour_data in weather_data["list"]:
#     condition_code = hour_data["weather"][0]["id"]
#     if int(condition_code) < 700:
#         will_rain = True
# if will_rain:
#     print("Bring an Umbrella")












#DAY 36 - STILL ON APIs (BUILDING A STOCK NEWS MONITORING PROJECT)

# import requests

# STOCK_NAME = "TSLA"
# COMPANY_NAME = "Tesla Inc"

# STOCK_ENDPOINT = "https://www.alphavantage.co/query"
# NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

# STOCK_API_KEY = "4NTXFVM6H7U2CJI1"
# NEWS_API_KEY = ""

# ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# # When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# #Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
# stock_params = {
#     "function": "TIME_SERIES_DAILY",
#     "symbol": STOCK_NAME,
#     "apiKey": STOCK_API_KEY,
# }

# response = requests.get(STOCK_ENDPOINT, params=stock_params)
# data = response.json()["Weekly Adjusted Time Series"]
# data_list = [value for (key, value) in data.items()]
# yesterday_data = data_list[0]
# yesterday_closing_price = yesterday_data["4. close"]
# print(yesterday_closing_price)

# #Get the day before yesterday's closing stock price
# day_before_yesterday_data = data_list[1]
# day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
# print(day_before_yesterday_closing_price)

# #Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
# difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))
# print(difference)

# #Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
# diff_percent = (difference / float(yesterday_closing_price)) * 100
# print(diff_percent)

#     ## STEP 2: https://newsapi.org/ 
#     # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

# #Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

# if diff_percent > 5:
#     news_params = {
#         "qInTitle": COMPANY_NAME,
#         "symbol": STOCK_NAME,
#         "apiKey": STOCK_API_KEY,
#     }

#     news_response = requests.get(NEWS_ENDPOINT, params=news_params)
#     articles = news_response.json()["articles"]
#     print(articles)

# #Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation

#     three_articles = articles[:3]
#     print(three_articles)

#     ## STEP 3: Use twilio.com/docs/sms/quickstart/python
#     #to send a separate message with each article's title and description to your phone number. 

# #Create a new list of the first 3 article's headline and description using list comprehension.
#     formatted_articles = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]












#DAY 37 - ADVANCED AUTHENTICATION, POST, PUT AND DELETE REQUESTS
# import requests
# from datetime import datetime

# USERNAME = "dimpledbright"
# TOKEN = "coldstone2002"
# GRAPH_ID = "graph1"

# pixela_endpoint = "https://pixe.la./v1/users"

# user_params = {
#     "token": TOKEN,
#     "username": USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes"
# }

# # response = requests.post(url=pixela_endpoint, json=user_params)
# # print(response.text)

# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

# graph_config = {
#     "id": GRAPH_ID,
#     "name": "Cycling Graph",
#     "unit": "Km",
#     "type": "float",
#     "color": "ajisai",
# }

# headers = {
#     "X-USER-TOKEN": TOKEN,
# }

# # response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# # print(response.text)

# pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

# today = datetime.now()

# pixel_data = {
#     "date": today.strftime("%Y%m%d"),
#     "quantity": input("How many kilometers did you cycle today? => ")
# }

# response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
# print(response.text)

# #TO UPDATE or PUT AN ENDPOINT
# update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

# new_pixel_data = {
#     "quantity": "5.4",
# }

# # response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# # print(response.text)

# #TO DELETE AN ENDPOINT
# delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

# delete_pixel_data = {
#     "quantity": "5.4",
# }

# response = requests.delete(url=delete_endpoint, headers=headers, json=delete_pixel_data)
# print(response.text)














#DAY 38 - EXERCISE TRACKER CAPSTONE PROJECT
# import requests
# from datetime import datetime
# import os

# # Your personal data. Used by Nutritionix to calculate calories.
# GENDER = "male"
# WEIGHT_KG = 84
# HEIGHT_CM = 180
# AGE = 32

# # Nutritionix APP ID and API Key. Actual values are stored as environment variables.
# APP_ID = os.environ["ENV_NIX_APP_ID"]
# API_KEY = os.environ["ENV_NIX_API_KEY"]

# exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"


# exercise_text = input("Tell me which exercises you did: ")

# # Nutritionix API Call
# headers = {
#     "x-app-id": APP_ID,
#     "x-app-key": API_KEY,
# }

# parameters = {
#     "query": exercise_text,
#     "gender": GENDER,
#     "weight_kg": WEIGHT_KG,
#     "height_cm": HEIGHT_CM,
#     "age": AGE
# }

# response = requests.post(exercise_endpoint, json=parameters, headers=headers)
# result = response.json()
# print(f"Nutritionix API call: \n {result} \n")

# # Adding date and time
# today_date = datetime.now().strftime("%d/%m/%Y")
# now_time = datetime.now().strftime("%X")

# # Sheety Project API. Check your Google sheet name and Sheety endpoint
# GOOGLE_SHEET_NAME = "workout"
# sheet_endpoint = os.environ[
#     "ENV_SHEETY_ENDPOINT"]

# # Sheety API Call & Authentication
# for exercise in result["exercises"]:
#     sheet_inputs = {
#         GOOGLE_SHEET_NAME: {
#             "date": today_date,
#             "time": now_time,
#             "exercise": exercise["name"].title(),
#             "duration": exercise["duration_min"],
#             "calories": exercise["nf_calories"]
#         }
#     }

#     # Sheety Authentication Option 1: No Auth
#     """
#     sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)
#     """

#     # Sheety Authentication Option 2: Basic Auth
#     sheet_response = requests.post(
#         sheet_endpoint,
#         json=sheet_inputs,
#         auth=(
#             os.environ["ENV_SHEETY_USERNAME"],
#             os.environ["ENV_SHEETY_PASSWORD"],
#         )
#     )

#     # Sheety Authentication Option 3: Bearer Token
#     """
#     bearer_headers = {
#         "Authorization": f"Bearer {os.environ['ENV_SHEETY_TOKEN']}"
#     }
#     sheet_response = requests.post(
#         sheet_endpoint,
#         json=sheet_inputs,
#         headers=bearer_headers
#     )    
#     """
#     print(f"Sheety Response: \n {sheet_response.text}")
















#DAY 39 AND DAY 40 - CHEAP FLIGHT FINDER CAPSTONE PROJECT 
from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()
notification_manager = NotificationManager()

ORIGIN_CITY_IATA = "LON"

if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    if flight.price < destination["lowestPrice"]:
        notification_manager.send_sms(
            message=f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
        )







#AFTER THIS WE WENT TO CREATE A "WEBPAGE" TO LEARN HTML AND CSS FROM DAY 41 - DAY 44






#DAY 45 - WEBSCRAPING WITH BEAUTIFUL SOUP
#MAKING A SITE FOR MY TOP 100 MOVIES
# from bs4 import BeautifulSoup
# import requests

# URL = "https://www.empireonline.com/movies/features/best-movies-2026/"

# response = requests.get(URL)
# website_html = response.text

# soup = BeautifulSoup(website_html, "html.parser")

# all_movies = soup.find_all(name = "h3", class_ = "title")

# movie_titles = [movie.getText() for movie in all_movies]
# movies = movie_titles[::-1]

# with open("movies.txt", mode="w") as file:
#     for movie in movies:
#         file.write(f"{movie}\n")






#SCRAPING DATA FROM A SITE USING BEAUTIFUL SOUP
# from bs4 import BeautifulSoup
# import requests
#
# response = requests.get("https://news.ycombinator.com/news")
# yc_web_page = response.text
#
# soup = BeautifulSoup(yc_web_page, "html.parser")
# articles = soup.find_all(name="a", class_="storylink")
# article_links = []
# article_texts = []
# for article_tag in articles:
#     text = article_tag.getText()
#     article_texts.append(text)
#     link = article_tag.get("href")
#     article_links.append(link)
#
# article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all("span", class_ = "score")]
#
# largest_number = max(article_upvotes)
# largest_index = article_upvotes.index(largest_number)
#
# print(article_texts[largest_index])
# print(article_links[largest_index])



#LEARNING HOW TO SCRAP DATA USING BEAUTIFULSOUP
# with open("website.html", encoding="utf-8") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
#
# # print(soup.title)
#
# # print(soup.title.string)
#
# # print(soup.prettify())
#
# all_anchor_tags = soup.find_all(name = "a")
# print(all_anchor_tags)
#
# for tag in all_anchor_tags:
#     print(tag.getText())
#     print(tag.get("href"))
#
# heading = soup.find(name = "h1", id = "name")
#
# class_is_heading = soup.find_all(class_ = "heading")
# print(class_is_heading)
#
# h3_heading = soup.find_all("h3", class_ = "heading")
# print(h3_heading)
#
# name = soup.select_one("#name")
# print(name)
#
# headings = soup.select_one(".heading")
# print(headings)













#DAY 46 - 