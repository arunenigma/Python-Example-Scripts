import random
guessesTaken = 0
#print 'Hello! What is your name? '
myName = raw_input('Hello! What is your name? ')
number = random.randint(1,30)
print 'Well! %s, I am thinking of a number between 1 and 30.' % (myName)
while guessesTaken < 6:
	guess = int(raw_input('Take a guess CHAMP ;>'))
	guessesTaken +=1
	
	if guess < number:
		print 'ur no is low..try again'
	if guess > number:
		print 'no is high..try again..'
	if guess == number:
		print 'bingo man !!'
		break
if guess == number:
	guessTaken = str(guessesTaken)
	print 'Great Job.. u r a champ man ! %s ' %guessesTaken, 'guesses to crack the magic !'
if guess!= number:
	number = str(number)
	print 'SORRY! THE NUMBER IS %s' %number