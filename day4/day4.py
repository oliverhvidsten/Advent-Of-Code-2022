import sys
sys.path.append('../')
import utils

lines = utils.read_textfile('day4.txt')

for i in range(len(lines)):
	elves = lines[i].split(',')
	for j in range(2):
		elves[j] = elves[j].split('-')
		elves[j][0] = int(elves[j][0])
		elves[j][1] = int(elves[j][1])
	lines[i] = elves

def part1(lines):
	counter = 0
	for line in lines:
		if (line[0][0] <= line[1][0]) and (line[0][1] >= line[1][1]):
			counter += 1
		elif (line[0][0] >= line[1][0]) and (line[0][1] <= line[1][1]):
			counter += 1

	print('Part 1 Result: ' + str(counter))

def part2(lines):
	counter = 0
	for line in lines:
		if (line[0][0] <= line[1][0]) and (line[0][1] >= line[1][0]):
			counter += 1
		elif (line[0][0] <= line[1][1]) and (line[0][1] >= line[1][1]):
			counter += 1
		elif (line[0][0] >= line[1][0]) and (line[0][1] <= line[1][1]):
			counter += 1
	print('Part 2 Result: ' + str(counter))


part1(lines)
part2(lines)
