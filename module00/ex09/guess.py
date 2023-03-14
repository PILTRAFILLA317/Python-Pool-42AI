import random

rand_num = random.randint(1, 99)

tries = 0
guessed = False

print("This is an interactive guessing game")
print("You have to enter a number between 1 and 99 to find out the secret number")
print("Type 'exit'to end the game.\nGood luck!\n")
while not guessed:
	inpt = input("What's your guess between 1 and 99?\n>> ")
	if inpt == 'exit':
		print("Goodbye!")
		exit(0)
	try:
		num = int(inpt)
	except ValueError:
		print("That's not a number.")
		continue
	if num < 1 or num > 99:
		print('Please enter a number between 1 and 99')
		continue
	tries += 1
	if num == rand_num:
		guessed = True
		if rand_num == 42:
			print("The answer to the ultimate question of life, the universe and everything is 42")
		if tries == 1:
			print("Congratulations! You got it on your first try!")
		else:
			print("Congratulations, you've got it!")
			print(f"You won in' {tries} attemps!")
	elif num < rand_num:
		print('Too low!')
	else:
		print('Too high!')