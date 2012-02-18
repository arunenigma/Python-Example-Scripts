from sys import argv
script, filename = argv

print 'We are gonna erase file %r' % filename
print 'if u don want that hit CTRL C(^C)'
print 'if u want to erase hit ENTER KEY'
raw_input('?')

print 'Opening the file...'
target = open(filename,'w')

print 'truncating file ! alvida'
target.truncate()

line1=raw_input('line 1')
line2=raw_input('line 2')
line3=raw_input('line 3')

target.write(line1)
target.write('\n')
target.write(line2)
target.write('\n')
target.write(line3)
target.write('\n')



print 'Done babe hamsa'
target.close()
