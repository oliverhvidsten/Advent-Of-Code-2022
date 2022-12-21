import sys
sys.path.append('../')
import utils

def part1and2(size):
	lines = utils.read_textfile('day6.txt')
	line = lines[0]

	i = 0
	while i < len(line) - 3:
		marker = line[i:i+size]
		found = True
		for letter in marker:
			occurances = marker.count(letter)
			if occurances > 1:
				found = False
				duplicate = letter
				break
		if found:
			answer = i + size
			break
		else:
			i += marker.find(duplicate) + 1
	return answer

answer = part1and2(4)
print('Part 1 Result: ' + str(answer))
answer = part1and2(14)
print('Part 2 Result: ' + str(answer))


