win_number = 8
trials = 3
i = 1
while i <= trials:
	value = int(input('Guess: '))
	i+= 1
	if value ==win_number:
		print("Wow, You Won!")
		break
else:
	print("You lost, try next time")
	

	