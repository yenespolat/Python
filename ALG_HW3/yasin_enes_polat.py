#Yasin Enes Polat 150117015 | CSE2046 HW-3
import math, sys, time

class City:

	def __init__ (self, id, x, y):
		self.id = id
		self.x = x
		self.y = y
		self.added = 0

class Node:

	def __init__ (self, dist, id):
		self.dist = dist
		self.id = id

cities = []

start_time = time.time()

def delSpace ( l ): # This function deletes redundant blank spaces in input.txt file 
    i = 0
    while i < len(l):
        if l[i] == '':
            del l[i]
        else:
            i = i+1

def main ( input ):
    f = open(input, 'r')
    for x in f:
        s = x.split(' ')
        delSpace(s)
        s = list(map(int, s))
        c = City(s[0], s[1], s[2])
        cities.append(c)
    f.close()

main(sys.argv[1])

adj = []

def calc_dist (c1, c2):
	return round(math.sqrt(pow(c1.x - c2.x, 2) + pow(c1.y - c2.y, 2)))

def fill_adj (): # This function fills adjacency matrix, first finds distances between ith and 0th to len(cities)th cities and sorts that array.
	for i in range(len(cities)):
		city1 = cities[i]
		unsorted = []
		for j in range(len(cities)):
			if i == j:
				continue
			else:
				city2 = cities[j]
				n = Node(calc_dist(city1, city2), j)
				unsorted.append(n)

		unsorted.sort(key = lambda x: x.dist)
		adj.append(unsorted)

fill_adj()

def find_nearest ( i ):
	liste = adj[i]
	idx = 0
	
	for j in range(len(liste)):
		if cities[liste[j].id].added != 1:
			idx = j
			break
	
	length = liste[idx].dist
	cities[liste[j].id].added = 1
	return cities[liste[j].id], length

def nearest_neighbor ( c1 ):
	tour = []
	tlen = 0
	
	tour.append(c1)
	c1.added = 1
	for i in range(len(cities) - 1):
		c2, length = find_nearest(c1.id)
		tour.append(c2)
		c1 = tour[i+1]
		tlen = tlen + length

	tlen = tlen

	return tour, tlen

def reset ():
	for i in range(len(cities)):
		cities[i].added = 0

bestlen = 9999999
best_tour = []
for i in range(len(cities)):
	t, l = nearest_neighbor(cities[i])
	t.append(cities[i])
	if l < bestlen :
		bestlen = l
		best_tour = []
		best_tour = t.copy()
	reset()

print(bestlen)

f = open('out.txt', 'w')

f.write(str(bestlen) + '\n')

for i in range(len(best_tour)):
	f.write(str(best_tour[i].id) + '\n')

f.close()

print(time.time() - start_time)



