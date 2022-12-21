import sys
sys.path.append('../')
import utils

lines = utils.read_textfile('day7.txt')
head = utils.Directory('/',None)

def buildDirectoryPaths(head, lines):
	currentPlace = head

	i = 0
	while i < len(lines):
		line = lines[i].split()

		if line[1] == 'cd':
			if line[2] == '..':
				currentPlace = currentPlace.parent
			elif line[2] =='/':
				currentPlace = head
			else:
				if not (line[2] in currentPlace.content.keys()):
					currentPlace.addDirectory(line[2], currentPlace)
				currentPlace = currentPlace.content[line[2]]

			i += 1

		elif line[1] == 'ls':
			i += 1
			contents = lines[i].split()
			while contents[0] != '$' and i < len(lines):
				if contents[0].isnumeric():
					currentPlace.addFile(contents[1], int(contents[0]))
				else:
					if not (contents[1] in currentPlace.content.keys()):
						currentPlace.addDirectory(contents[1], currentPlace)
				i += 1
				if i < len(lines):
					contents = lines[i].split()

def bfs(head):
	allSizes = []
	queue = list()
	explored = [head]
	queue.append(head)

	while queue:
		value = queue.pop(0)
		allSizes.append(value.size)
		for fileDir in value.content.values():
			if isinstance(fileDir, utils.Directory):
				if not fileDir in explored:
					explored.append(fileDir)
					queue.append(fileDir)
	return allSizes


def part1(allSizes):
	answer = [i for i in allSizes if i < 100000]
	print('Part 1 Result: ' + str(sum(answer)))


def part2(allSizes):
	total = 70000000
	total_needed = 30000000
	used = allSizes[0]
	available = total - used
	extra_needed = total_needed - available

	possible = [i for i in allSizes if i >= extra_needed]
	print('Part 2 Result: ' + str(min(possible)))


buildDirectoryPaths(head, lines)
head.calculateSize()
allSizes = bfs(head)
part1(allSizes)
part2(allSizes)


