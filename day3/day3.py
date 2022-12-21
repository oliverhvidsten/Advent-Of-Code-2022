import sys
sys.path.append('../')
import utils

lines = utils.read_textfile('day3.txt')

def part1(lines):
	lines = lines.copy()
	for i in range(len(lines)):
		line = lines[i]
		half = int(len(line)/2)
		lines[i] = [line[:half], line[half:]]

	total = 0
	for line in lines:
		first = line[0]
		second = line[1]
		for letter in first:
			if letter in second:
				if letter.islower():
					total += ord(letter) - 96
				else:
					total += ord(letter) - 64 + 26
				break
	print('Part 1 Result: ' + str(total))

def part2(lines):
	x = 0
	newList = []
	while (x+2) < len(lines):
		newList.append([lines[x], lines[x+1], lines[x+2]])
		x = x+3

	total = 0
	for lines in newList:
		line = lines[0]
		for letter in line:
			if (letter in lines[1]) and (letter in lines[2]):
				if letter.islower():
					total += ord(letter) - 96
				else:
					total += ord(letter) - 64 + 26
				break
	print('Part 1 Result: ' + str(total))

part1(lines)
part2(lines)