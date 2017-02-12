import os
import random
while True:
	#Menu
	print "1: Convert: Base 2 --> Base 10"
	print "2: Convert: Base 10 --> Base 2"
	print "\n3: Practice: Base 2 --> Base 10"
	print "4: Practice: Base 10 --> Base 2"
	rawChoice = raw_input("Choose(1-4): ")

	#Main
	try:
		choice = int(rawChoice)
		if choice >= 1 and choice <= 4:
			#Convert: Base 2 --> Base 10
			if choice == 1:
				try:
					rawNumber = raw_input("Enter a binary number to convert to decimal: ")
					number = int(rawNumber,2)
					print "Decimal number: %d" %number
				except ValueError:
					print "Invalid Base 2 Character!"
			#Convert: Base 10 --> Base 2
			elif choice == 2:
				try:
					rawNumber = raw_input ("Enter a decimal number to convert to binary: ")
					number = int(rawNumber)
					rawBin = bin(number)
					bin = str(rawBin)[2:]
					print "Binary number: ",bin
				except ValueError:
					print "Invalid Base 10 Character!"
			#Practice: Base 2 --> Base 10
			elif choice == 3:
				randomBin = str(bin(random.randint(1,120)))[2:]
				print "Base 2 number: ",randomBin
				try:
					rawGuess = raw_input("Base 10 number: ")
					guess = int(rawGuess)
					if (int(randomBin,2) == guess):
						print "\nCorrect!"
					else:
						print "\nWrong! Answer is: ",int(randomBin,2)
				except ValueError:
					print "\nInvalid Base 10 Character! Answer is: ",int(randomBin,2)
			#Practice: Base 10 --> Base 2	
			elif choice == 4:
				randomDec = random.randint(1,120)
				print "Base 10 number: ",randomDec
				try:
					rawGuess = raw_input("Base 2 number: ")
					guess = str(int(rawGuess,2))
					randomBin = str(bin(randomDec))[2:]
					if guess == randomBin:
						print "\nCorrect!"
					else:
						print "\nWrong! Answer is: ",randomBin
				except ValueError:
					print "\nInvalid Base 2 Character! Answer is: ",randomBin
			#Wrong menu choice
			else:
				print "Invalid number! Enter a number from 1 to 4"
	#Wrong menu character	
	except ValueError:
		print "Invalid character!"

	raw_input("\nPress ENTER to restart.")
	os.system("cls")
