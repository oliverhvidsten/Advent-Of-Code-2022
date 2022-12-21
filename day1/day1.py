import sys
sys.path.append('../')
import utils

line_list = utils.read_textfile('day1.txt')
elves = []
totSum = 0

for ele in line_list:
	if ele == '':
		elves.append(totSum)
		totSum = 0
	else:
		totSum += int(ele)
elves.append(totSum)

def day1p1(elves):
	print('Part 1 Result: ' + str(max(elves)))

def day1p2(elves):
	elves.sort(reverse = True)
	total = sum(elves[0:3])
	print('Part 2 Results: ' + str(total))


day1p1(elves)
day1p2(elves)
