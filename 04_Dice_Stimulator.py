from random import randint

while True:
	roll_the_dice = randint(1,6)

	def print_dice(dice):
		if dice ==1:
			print("  ---------------")
			print(" | ","   ","   ","   "," | ") 
			print(" | ","   "," • ","   "," | ")
			print(" | ","   ","   ","   "," | ")
			print("  ---------------")
		
		elif dice == 2:
			print("  ---------------")
			print(" | "," • ","   ","   "," | ")
			print(" | ","   ","   ","   "," | ")
			print(" | ","   ","   "," • "," | ")
			print("  ---------------")
		
		elif dice == 3:
			print("  ---------------")
			print(" | "," • ","   ","   "," | ")
			print(" | ","   "," • ","   "," | ")
			print(" | ","   ","   "," • "," | ")
			print("  ---------------")
		
		elif dice == 4:
			print("  ---------------")
			print(" | "," • ","   "," • "," | ")
			print(" | ","   ","   ","   "," | ")
			print(" | "," • ","   "," • "," | ")
			print("  ---------------")
		elif dice == 5:
			print("  ---------------")
			print(" | "," • ","   "," • "," | ")
			print(" | ","   "," • ","   "," | ")
			print(" | "," • ","   "," • "," | ")
			print("  ---------------")
		else:
			print("  ---------------")
			print(" | "," • ","   "," • "," | ")
			print(" | "," • ","   "," • "," | ")
			print(" | "," • ","   "," • "," | ")
			print("  ---------------")
		
	print_dice(roll_the_dice)
	
	stop_stimulator = input ("""Do you want to stop the Dice Stimulator ?
If you want to stop type 'yes' otherwise just press enter: """).lower()
	if stop_stimulator == "yes":
		break
	else:
		print ("\n")
	
