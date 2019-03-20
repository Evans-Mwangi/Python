import random
import simplegui

Computer_Score = 0
Human_Score=0
human_choice = ""
Computer_choice = ""

#Functions to be filled
def choice_to_number(choice):
    if choice == 'rock':
        return 0
    elif choice == 'paper':
        return 1
    elif choice == 'scissors':
        return 2
    else:
        print ('Invalid Input')
    
def number_to_choice(choice):
    if number == 1:
        return 'rock'
    elif number == 2:
        return 'paper'
    elif number == 3:
        return 'scissors'
    else:
        print ('Invalid Input')
    
def random_computer_choice():
    MyList = ['rock', 'paper', 'scissors']
    random.choice(MyList)
    
def choice_result(human_choice, computer_choice):
    global Human_Score
    global Computer_Score
    if human_choice == 'rock' and computer_choice == 'paper':
        Computer_Score += 1
    elif human_choice == 'rock' and computer_choice == 'scissors':
        Human_Score += 1
    elif human_choice == 'paper' and computer_choice == 'scissors':
        Computer_Score += 1
    elif human_choice == 'paper' and computer_choice == 'rock':
        Human_Score += 1
    elif human_choice == 'scissors' and computer_choice == 'rock':
        Computer_Score += 1
    elif human_choice == 'scissors' and computer_choice == 'paper':
        Human_Score += 1
    else:
        print ('Please Play According To The Rules (Why do you have to be such a rebel?)')

#Test Code
def test_choice_to_number():
    assert choice_to_number('rock') == 0
    assert choice_to_number('paper') == 1
    assert choice_to_number('scissors') == 2
    
def test_number_to_choice():
    assert number_to_choice(0) == 'rock'
    assert number_to_choice(1) == 'paper'
    assert number_to_choice(2) == 'scissors'

def test_all():
    test_choice_to_number()
    test_number_to_choice()

test_all()

#Mouse Click on Rock handler
def rock():
    global human_choice, computer_choice
    global Human_Score, Computer_Score

    human_choice = 'rock'
    computer_choice = random_computer_choice()
    choice_result(computer_choice, human_choice)
    
#Mouse Click on Paper handler
def paper():
    global human_choice, computer_choice
    global Human_Score, Computer_Score

    human_choice = 'paper'
    computer_choice = random_computer_choice()
    choice_result(computer_choice, human_choice)
    
#Mouse Click on Scissors handler
def scissors():
    global human_choice, computer_choice
    global Human_Score, Computer_Score

    human_choice = 'scissors'
    computer_choice = random_computer_choice()
    choice_result(computer_choice, human_choice)

#Handler to draw on Canvas
def draw(canvas):
    try:
        #Draw Choices
        canvas.draw_text("You: " + human_choice, [10,40], 48, "Green")
        canvas.draw_text("Comp: " + computer_choice, [10,80], 48, "Red")

        #Draw Scores
        canvas.draw_text("Human Score: " + str(Human_Score), [10,150], 30, "Green")
        canvas.draw_text("Comp Score: " + str(Computer_Score), [10,190], 30, "Red")
    except TypeError:
        pass
#Code For GUIFrame Creator and assign callbacks
def play_rps():
    frame = simplegui.create_frame("Home", 300, 200)
    frame.add_button("Rock", rock)
    frame.add_button("Paper", paper)
    frame.add_button("Scissors", scissors)
    frame.set_draw_handler(draw)

    #Start Frame Animation
    frame.start()

play_rps()
"""
[0,1,2]
[r,p,s]

rock vs scissors
(rock - scissors)%3 == 1
(0-2)%3 ==1
(-2) %3 == 1
1 == 1
rock wins

paper vs scissors
(paper - scissors)%3 == 1
(1-2)%3 ==1
2 == 1
scissors wins

paper vs rocks
(paper - rocks)%3 == 1
(1-0)%3 ==1
1%3 == 1
1 == 1
paper wins
"""