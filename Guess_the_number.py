from random import randint


guess_number = randint(0,1000)

while True:
	user_guess = int(input("Enter your guess: "))
	if user_guess < guess_number:
		print("Too low, guess little higher\n")
	elif user_guess > guess_number:
		print("Too High, guess little lower\n")
	else:
		print("You guess it correctly.\n")
		break
