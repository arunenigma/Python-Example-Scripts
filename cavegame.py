import random
import time
def displayIntro():
	print 'You are on a planet full of dragons. In front of you,'
def chooseCave():
	cave = ''
	while cave !='1' and cave !='2':
		cave = raw_input('Which cave do u want to get into?')
	return cave


def checkCave(chosenCave):
	print 'You approach the cave...'
	print 'A large dragon jumps out in front of you! He opens his jaws and...'

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



