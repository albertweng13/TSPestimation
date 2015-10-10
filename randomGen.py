from random import randint

randomnum = 8
edgeweights = 10
print randomnum

adjmatrix = []
for i in range(0, randomnum):
	temp = []
	for j in range(0, randomnum):
		if i == j:
			temp.append(0)
		else:
			temp.append(randint(0,edgeweights))
	adjmatrix.append(temp)

def diamondMaker(matrix,node1,node2,node3,node4,node5,node6,node7,node8):

	def helper(matrix,nodex,nodey):
		for i in range(0,randomnum):
			if i == nodex:
				continue
			if i == nodey:
				matrix[nodex][nodey] = randint(0,(edgeweights/2))
			else:
				matrix[nodex][i] = randint((edgeweights/2)+1, edgeweights)

	helper(matrix, node1, node2)
	helper(matrix, node2, node3)
	helper(matrix, node3, node4)
	helper(matrix, node4, node5)
	helper(matrix, node5, node6)
	helper(matrix, node6, node7)
	helper(matrix, node7, node8)


#diamondMaker(adjmatrix, 0, 1, 2, 3, 4, 5, 6, 7)

#Making it symmetrical
for i in range(0,randomnum):
	for j in range(0, randomnum):
		adjmatrix[j][i] = adjmatrix[i][j]


#Printing The matrix
for i in range(0, randomnum):
	line = ""
	for j in range(0, len(adjmatrix[i])):
		line = line + str(adjmatrix[i][j]) + " "
	line = line.rstrip()
	print line




rb = []
redcount = 0
bluecount = 0
for i in range(0,randomnum):
	rb.append("hi")

for i in range(0, randomnum):
	random = randint(1,2)
	if random == 1:
		if redcount<randomnum/2:
			redcount += 1
			rb[i] = "R"
		else:
			bluecount += 1
			rb[i] = "B"
	else:
		if bluecount<randomnum/2:
			bluecount += 1
			rb[i] = "B"
		else:
			redcount += 1
			rb[i] = "R"

rbout = ""
for i in range(0, randomnum):
	rbout = rbout + str(rb[i])
#print rb
print rbout
print redcount
print bluecount

