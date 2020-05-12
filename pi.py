#        Yasin Enes Polat       #
# PI WORKS TECHNICAL ASSIGNMENT #
# Program takes i.txt as input  #

class Depth:
#This class is for keeping numbers' list of each depth level on pyramid.
	def __init__ (self, a, d):
		self.nums = a.copy()
		self.depth = d

	def getA (self):
		return self.nums


f = open('i.txt', 'r')

ds = []			#Each list consisting numbers of each depth-level.
maxval = 0		#Maximum value
maxarr = []		#Maximum number's list
primes = []		#All prime numbers in given pyramid

#Reading numbers from input file line by line, creating Depth object and adding it to ds list.
i = 0
for x in f: 
	s = x.split(' ')
	s = list(map(int, s))
	dpt = Depth(s, i)
	ds.append(dpt)
	i += 1
f.close()

#Checks if given number is prime or not.
def checkPrime (num):
	if num > 1:
	# check for factors
		for i in range(2,num):
			if (num % i) == 0:
				return 0
		
		if num not in primes:
			primes.append(num)
		return 1
       
	# if input number is less than
	# or equal to 1, it is not prime
	else:
		return 0

#Returns sum of all elements in given list.
def total (arr):
	total = 0
	j = 0
	for i in arr:
		total += arr[j]
		j += 1
	return total

#This function recursively traces paths root to bottom of pyramid then checks if resulting array is max array or not.
def traverse (d, i, index, ar):
	global maxarr, maxval
	if d >= len(ds) or len(ar) >= len(ds):
		if total(ar) > maxval :
			maxval = total(ar)
			maxarr = ar.copy()
		return
	depthobj = ds[d]
	a = depthobj.getA()
	if checkPrime(a[i]) != 1 :
		b = ar.copy()
		b.insert(index, a[i])
		traverse(d + 1, i, index + 1, b)
	if checkPrime(a[i+1]) != 1 :
		c = ar.copy()
		c.insert(index, a[i+1])
		traverse(d + 1, i + 1, index + 1, c)

array2 = []
array2.insert(0, ds[0].getA()[0])
traverse(1, 0, 1, array2)
print('Array including numbers that gives max result; \n', maxarr)
print('Array including prime numbers exists in pyramid; \n', primes)
print('Max -> ', maxval)