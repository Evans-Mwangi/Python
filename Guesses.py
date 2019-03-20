import random
human_guess = int(input"Guess the number I am thinking of: ")
computer_guess = random.randomInt
Guesses_Taken = 0
while Guesses_Taken <= 6:
	if computer_guess < human_guess:
		Guesses_Taken += 1
		print ('Your guess is higher than the number I am thinking of.')
	if computer_guess > human_guess:
		Guesses_Taken += 1
		print('Your guess is lower than the number I am thinking of.')
	if computer_guess == human_guess:
		Guesses_Taken += 1
		break
if computer_guess == human_guess:
	computer_guess = str(computer_guess)
	Guesses_Taken = str(Guesses_Taken)
	print ('You guessed right. The number is '+ computer_guess +' in '+ Guesses_Taken 'guesses.')