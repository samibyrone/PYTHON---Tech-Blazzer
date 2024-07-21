from random import randint

random_number = randint(1, 10)
	
guess = 0
stop = " "
counter = 0

print(f" Welcome You Warmly To Your Guessing Game, All You Have To Do Is Guess The Number Right And You Become Our Champion!!!! ")
print()

while (guess != random_number):
	counter +1
	
	guess = int(input(f' Guess a number between 1 and 1000: '))

	if guess < random_number:
		print(' Sorry, guess again. Too low. ')

	elif guess > random_number:
		print(' Sorry, guess again. Too high. ')

	elif guess == random_number:
		print(f' Yay, Congrats. You Have Guessed {random_number} To Be the Right Number Correctly!!! ' )\

	stop = print(f' Congratulations, Would you like to play again? Kindly enter YES or NO ')

	print('\n You played the Game {counter} times')
	