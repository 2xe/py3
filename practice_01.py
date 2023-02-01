import random

def roll_dice(times, cheat):
	
	score = 0 

	for x in range(10):
		random_int = random.randint(1,6)
		score += random_int

		if (cheat == 1):
			score += 5
		pass
	
	print(cheat)
	
	return

roll_dice(10)