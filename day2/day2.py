import sys
sys.path.append('../')
import utils

lines = utils.read_textfile('day2.txt')

def part1(lines):
	answer = {
	'A': {'X': 4, 'Y': 8, 'Z': 3}, 
	'B': {'X': 1, 'Y': 5, 'Z': 9}, 
	'C': {'X': 7, 'Y': 2, 'Z': 6}
	}

	total = 0
	for line in lines:
		total += answer[line[0]][line[2]]

	print('Part 1 Result: ' + str(total))


def part2(lines):
	answer = {
	'A': {'X': 3, 'Y': 4, 'Z': 8}, 
	'B': {'X': 1, 'Y': 5, 'Z': 9}, 
	'C': {'X': 2, 'Y': 6, 'Z': 7}
	}

	total = 0
	for line in lines:
		total += answer[line[0]][line[2]]

	print('Part 2 Result: ' + str(total))

part1(lines)
part2(lines)