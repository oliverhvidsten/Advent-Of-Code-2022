import sys
sys.path.append('../')
import utils

lines = utils.read_textfile('day5_instructions.txt')
stackRows = utils.raw_textfile('day5_stacks.txt')


def buildStacks(stackRows):
	stackRows = [row.split() for row in stackRows]

	stacks = []
	i = len(stackRows) - 1
	while i >= 0:
		if i == len(stackRows) - 1:
			for j in range(len(stackRows[i])):
				if stackRows[i][j] == '...':
					stacks.append([])
				else: 
					stacks.append([stackRows[i][j]])

		else:
			for j in range(len(stackRows[i])):
				if not(stackRows[i][j] == '...'):
					stacks[j].append(stackRows[i][j])
		i -= 1
	return stacks

def processInstructions(lines):
	for i in range(len(lines)):
		instruct = lines[i].split()
		instruct = [int(instruct[1]), int(instruct[3]), int(instruct[5])]
		lines[i] = instruct
	return lines


def part1(instructions, stacks):
	for instruction in instructions:
		for i in range(instruction[0]):
			crate = stacks[instruction[1] - 1].pop()
			stacks[instruction[2] - 1].append(crate)

	string = []
	for stack in stacks:
		string.append(stack[-1])
	string = ''.join(string)
	string = string.replace('[', '')
	string = string.replace(']', '')


	print('Part 1 Result: ' + string)

def part2(instructions, stacks):
	for instruction in instructions:

		crates = stacks[instruction[1] - 1][(-1*instruction[0]):]
		stacks[instruction[1] - 1][(-1*instruction[0]):] = []
		for crate in crates:
			stacks[instruction[2] - 1].append(crate)

	string = []
	for stack in stacks:
		string.append(stack[-1])
	string = ''.join(string)
	string = string.replace('[', '')
	string = string.replace(']', '')


	print('Part 2 Result: ' + string)



stacks = buildStacks(stackRows)
instructions = processInstructions(lines)
part1(instructions, stacks)

stacks = buildStacks(stackRows)
part2(instructions, stacks)
