def choice_to_number(choice):
	my_race={'Usain':1, 'Me':2, 'Qazi':3}
	return my_race[choice]
def number_to_choice(number):
    return{1:'Usain', 2:'Me', 3:'Qazi'}
def test_choice_to_number():
	assert choice_to_number('Usain') == 1
	assert choice_to_number('Me') == 2
	assert choice_to_number('Qazi') == 3
def test_number_to_choice():
	assert number_to_choice('1') == Usain
	assert number_to_choice('2') == Me
	assert number_to_choice('3') == Qazi
def test_all():
	try:
		test_choice_to_number()
		test_number_to_choice()
	except AssertionError:
		print('Incorrect: Do Not Give Up') 
	else:
		print("Correct:Code Successful")
test_all()