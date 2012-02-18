import time
import random as r
rate = 0.2
w = [r.uniform(0,1),r.uniform(0,1)]
inp = [0.0,0.0]
test = [[0.0,0.0,0.0]]
test+= [[0.0,1.0,1.0]]
test+= [[1.0,0.0,1.0]]
test+= [[1.0,1.0,1.0]]

def out(midThresh):
	global inp,w
	s = inp[0] * w[0] + inp[1] * w[1]
	if s > midThresh:
		return 1.0
	else:
		return 0.0
def display(o,real):
	if o == real:
		print str(o)+'should be'+str(real)+'***'
	else:
		print str(o)+'should be'+str(real)
while 1:
	for i in range(len(test)):
		inp[0]=test[i][0]
		inp[1]=test[i][1]
		o=out(2)
		w[0]+=rate*(test[i][2]-o)
		display(out,test[i][2])
		o=out(2)
		w[1]+=rate*(test[i][2]-o)
		display(out,test[i][2])


