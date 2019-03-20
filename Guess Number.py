import random
MyName = input('Enter your Name: ')
computer_guess = random.randint(0,20)
Guesses_Taken = 0
while Guesses_Taken < 6:
    Guesses_Taken += 1
    human_guess = int(input('Guess the number I am thinking of: '))
    if human_guess <= 20:
        if computer_guess < human_guess:
            print ('Your guess is higher than the number I am thinking of.Try again!')
        if computer_guess > human_guess:
            print('Your guess is lower than the number I am thinking of. Try Again!')
        if computer_guess == human_guess:
            break
    else:
        print ('Guess a number in the region of 0 and 20')
if computer_guess == human_guess:
    computer_guess = str(computer_guess)
    Guesses_Taken = str(Guesses_Taken)
    print ('You guessed right '+ MyName +'. The number is '+ computer_guess +' in '+ Guesses_Taken +' guesses.')
else:
    computer_guess = str(computer_guess)
    print('No' +MyName+', The number I was thinking of is ' +computer_guess+'. Try to beat me next time!')