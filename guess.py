from random import randint
def guess():
	num = randint(1,100)
	print num
	guess_num = input("Guess the number, you have 5 chances:")
	trial = 0
	while(trial < 4):
		trial += 1
		if guess_num == num:
			print "Bull eye, great guess "
			print "Congratulations you got it in {0} guesses".format(trial)
			break
		elif guess_num > num:
			guess_num = input("Guess is high , Try Again : ")
		else:
			guess_num = input("Guess is low, Try Again : ")
	else:
		if guess_num == num:
			print "Bull eye, great guess "
			print "Congratulations you got it in 5 guesses"
		else:
			print "Lost all chances, The number is {}".format(num)
		

if __name__ == '__main__':
	guess()