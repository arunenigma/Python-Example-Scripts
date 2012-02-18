import string
import sys
class roman:
    def __init__(self,y):
        if y < 1:
            raise ValueError
        self.rlist = []
        ms = y / 1000
        tmp = y % 1000
        if ms > 0:
            self.rlist.append("M" * ms)
        ds = tmp / 500
        tmp = tmp % 500
        if ds > 0:
            self.rlist.append("D" * ds)
        cs = tmp / 100
        tmp = tmp % 100
        if cs > 0:
            self.rlist.append("C" * cs)
        ls = tmp / 50
        tmp = tmp % 50
        if ls > 0:
            self.rlist.append("L" * ls)
        xs = tmp / 10
        tmp = tmp % 10
        if xs > 0:
            self.rlist.append("X" * xs)
        vs = tmp / 5
        tmp = tmp % 5
        if vs > 0:
            self.rlist.append("V" * vs)
        js = tmp
        if js > 0:
            self.rlist.append("I" * js)
	def ryear(self):
		s = ""
		for i in self.rlist:
			s = s + i
		print s
		#return s
	#print s

if __name__ == "__main__":
	if len(sys.argv) > 1:
		yr = string.atoi(sys.argv[1])
	else:
		yr = 1999
	x = roman(yr)
	ryear()
	#print x.ryear()
	#x.ryear()
           