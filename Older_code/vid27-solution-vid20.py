# Q. make user to guess a number by giving them hint as your number is lesser or greater than given nunber.you have to use following thing-
#   no. of guess= 9
#   no. of guesses left
#	no. of guesses took to finishes 
#	if loose print game over!


n=24
numofguess=1
print("THIS IS A NUMBER GUESSING GAME :)\n\n\n")
print("you have total 9 guesses..")
while(numofguess<=9):
	num= int(input("guess the number\n"))
	if num<24:
		print("WRONG ONE!,try greater number\n")
	elif num>24:
		print("WRONG ONE!,try lesser number\n")
	else:
		print("WOOH!! YOU WON..")
		print("you have taken",numofguess,"number of guesses to finish")
	print(9-numofguess,"guesses you have left!!")
	numofguess= numofguess + 1
	
if numofguess>9:
	print("you loose...\n GAME OVER")

