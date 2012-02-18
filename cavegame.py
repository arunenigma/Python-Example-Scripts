import random
import time
def displayIntro():
	print 'You are on a planet full of dragons. In front of you,'	print 'you see two caves. In one cave, the dragon is friendly'	print 'and will share his treasure with you. The other dragon'	print 'is greedy and hungry, and will eat you onsight.'	print ''
def chooseCave():
	cave = ''
	while cave !='1' and cave !='2':
		cave = raw_input('Which cave do u want to get into?')
	return cave


def checkCave(chosenCave):
	print 'You approach the cave...'	time.sleep(2)	print 'It is dark and spooky...'	time.sleep(2)
	print 'A large dragon jumps out in front of you! He opens his jaws and...'	print ''	time.sleep(2)
	friendlyCave = random.randint(1, 2)
	if chosenCave == str(friendlyCave):
		print 'Gives you his treasure!'
	else:
		print 'Gobbles u down'

playAgain = 'yes'
while playAgain == 'yes' or playAgain =='y':
	displayIntro()
	caveNumber=chooseCave()
	checkCave(caveNumber)
	playAgain = raw_input('Do u want to play again? (y or n)')




