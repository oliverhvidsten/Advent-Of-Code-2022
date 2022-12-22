import numpy as np
import sys
sys.path.append('../')
import utils

global forest
global visibleDirections

lines = utils.read_textfile('day8.txt')
for i in range(len(lines)):
	lines[i] = list(lines[i])

forest = np.array(lines, dtype = int)
visibleDirections = np.zeros_like(forest)

def lookEverywhere(i,j):
	vertical = forest[:,j]
	horizontal = forest[i,:]
	shrouded = [False, False, False, False]
	for x in range(len(vertical)):
		if x < i and vertical[x] >= forest[i,j]:
			shrouded[0] = True
		elif x > i and vertical[x] >= forest[i,j]:
			shrouded[1] = True
	for y in range(len(horizontal)):
		if y < j and horizontal[y] >= forest[i,j]:
			shrouded[2] = True
		elif y > j and horizontal[y] >= forest[i,j]:
			shrouded[3] = True

	if all(shrouded):
		visibleDirections[i,j] = 1

def onEdge(i,j):
	if i == 0 or i == forest.shape[0] - 1:
		return True
	elif j == 0 or j == forest.shape[1] - 1:
		return True
	else:
		return False

def calculateQuality(i,j):
	views = [0,0,0,0]
	# go left
	x = j - 1
	while x >= 0:
		views[0] += 1
		if forest[i,x] >= forest[i,j]:
			break
		x -= 1

	# go right
	x = j + 1
	while x < forest.shape[1]:
		views[1] += 1
		if forest[i,x] >= forest[i,j]:
			break
		x += 1

	# go up
	x = i - 1
	while x >= 0:
		views[2] += 1
		if forest[x,j] >= forest[i,j]:
			break
		x -= 1

	# go down
	x = i + 1
	while x < forest.shape[0]:
		views[3] += 1
		if forest[x,j] >= forest[i,j]:
			break
		x += 1
	return np.prod(views)




def part1():
	for i in range(forest.shape[0]):
		for j in range(forest.shape[1]):
			if not onEdge(i,j):
				lookEverywhere(i,j)
	answer = visibleDirections.sum()
	answer = (visibleDirections.shape[0] * visibleDirections.shape[1]) - answer
	print('Part 1 Result: ' + str(answer))

def part2():
	highestScore = 0
	for i in range(forest.shape[0]):
		for j in range(forest.shape[1]):
			if not onEdge(i,j):
				answer = calculateQuality(i,j)
				if answer > highestScore:
					highestScore = answer
	print('Part 2 Result: ' + str(highestScore))




part1()
part2()