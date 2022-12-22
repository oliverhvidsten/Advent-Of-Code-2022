import sys
sys.path.append('../')
import utils

lines = utils.read_textfile('day10.txt')


def updateClockCycle():
	global clockCycle
	global registerValue

	global p1_answer
	global p2_list
	global p2_answer

	if (clockCycle % 40) >= registerValue -1 and (clockCycle % 40) <= registerValue + 1:
		p2_list.append('#')
	else:
		p2_list.append('.')
	clockCycle += 1

	if clockCycle in [20, 60, 100, 140, 180, 220]:
		p1_answer += (registerValue * clockCycle)

	if (clockCycle % 40) == 0:
		p2_answer.append(''.join(p2_list))
		p2_list = []


def runProgram():

	global clockCycle
	global registerValue

	global p1_answer
	global p2_list
	global p2_answer

	clockCycle = 0
	registerValue = 1

	p1_answer = 0
	p2_list = []
	p2_answer = []

	for line in lines:
		line = line.split()
		if line[0] == 'addx':
			updateClockCycle()
			updateClockCycle()
			registerValue += int(line[1])
		else:
			updateClockCycle()

	print('Part 1 Result: ' + str(p1_answer))
	print('Part 2 Result: ')
	for row in p2_answer:
		print(row)


runProgram()