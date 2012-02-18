from numpy import *
import pylab

x = [0, 0];

A = [ [.5, 0], [0, .5] ];
b1 = [0, 0];
b2 = [.5, 0];
b3 = [.25, sqrt(3)/4];

pylab.ion() # animation on

#Note the comma after line. This is placed here because plot returns a list of lines that are drawn.
line, = pylab.plot(x[0],x[1],'m.',markersize=6) 
pylab.axis([0,1,0,1])

data1 = []
data2 = []
iter = 0

while True:
 r = fix(random.rand()*3)
 if r==0:
  x = dot(A,x)+b1
 if r==1:
  x = dot(A,x)+b2
 if r==2:
  x = dot(A,x)+b3
 data1.append(x[0]) 
 data2.append(x[1])
 line.set_xdata(data1)  # update the data
 line.set_ydata(data2)
 pylab.draw() # draw the points again
 iter += 1
 print iter