import numpy as np
import sys
sys.path.append('../')
import utils
import time

lines = utils.read_textfile('day9.txt')

def tailInRange():
	distance = np.sqrt((headLocation[0] - tailLocation[0])**2 + (headLocation[1] - tailLocation[1])**2)
	if distance <= np.sqrt(2):
		return True
	else:
		return False

def part1():
	global headLocation
	global tailLocation

	startingPoint = (0,0)
	headLocation = startingPoint
	tailLocation = startingPoint

	visitedSet = {startingPoint}

	for line in lines:
		# update head location
		line = line.split()
		for x in range(int(line[1])):
			if line[0] == 'U':
				headLocation = (headLocation[0], headLocation[1] + 1)
			elif line[0] == 'D':
				headLocation = (headLocation[0], headLocation[1] - 1)
			elif line[0] == 'L':
				headLocation = (headLocation[0] - 1, headLocation[1])
			else:
				headLocation = (headLocation[0] + 1, headLocation[1])

			# update tail location (if necessary)
			if not tailInRange():
				if line[0] == 'U':
					tailLocation = (headLocation[0], headLocation[1] - 1)
				elif line[0] == 'D':
					tailLocation = (headLocation[0], headLocation[1] + 1)
				elif line[0] == 'L':
					tailLocation = (headLocation[0] + 1, headLocation[1])
				else:
					tailLocation = (headLocation[0] - 1, headLocation[1])
				visitedSet.add(tailLocation)


	print('Part 1 Result: ' + str(len(visitedSet)))

##################################


def inRange(rel_head, rel_tail):
	distance = np.sqrt((rel_head[0] - rel_tail[0])**2 + (rel_head[1] - rel_tail[1])**2)
	if distance <= np.sqrt(2):
		return True
	else:
		return False

def findOverlap(rel_head, rel_tail):
	options = {
	(rel_head[0] + 1, rel_head[1]),
	(rel_head[0] - 1, rel_head[1]),
	(rel_head[0], rel_head[1] + 1),
	(rel_head[0], rel_head[1] - 1)
	}
	options2 = {
	(rel_head[0] + 1, rel_head[1] + 1),
	(rel_head[0] - 1, rel_head[1] - 1),
	(rel_head[0] + 1, rel_head[1] - 1),
	(rel_head[0] - 1, rel_head[1] + 1)
	}

	for option in [options, options2]:
		for i in range(3):
			for j in range(3):
				if i == 1 and j == 1:
					continue
				if (rel_tail[0] - 1 + i, rel_tail[1] - 1 + j) in option:
					return (rel_tail[0] - 1 + i, rel_tail[1] - 1 + j)


def part2():
	startingLocation = (0,0)
	locationList = []
	visitedSet = {startingLocation}
	for x in range(10):
		locationList.append(startingLocation)

	for line in lines:
		# update head location
		line = line.split()
		for x in range(int(line[1])):
			if line[0] == 'U':
				locationList[0] = (locationList[0][0], locationList[0][1] + 1)
			elif line[0] == 'D':
				locationList[0] = (locationList[0][0], locationList[0][1] - 1)
			elif line[0] == 'L':
				locationList[0] = (locationList[0][0] - 1, locationList[0][1])
			else:
				locationList[0] = (locationList[0][0] + 1, locationList[0][1])

		# update rest of rope (if necessary)
			for y in range(len(locationList) - 1):
				if not inRange(locationList[y], locationList[y + 1]):
					locationList[y+1] = findOverlap(locationList[y], locationList[y + 1])
			visitedSet.add(locationList[-1])
	print('Part 2 Result: ' + str(len(visitedSet)))


part1()
part2()






