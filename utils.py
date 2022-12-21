
def read_textfile(filename):
	with open(filename) as f:
		lines = [line.strip() for line in f.readlines()]
		return lines

def raw_textfile(filename):
	with open(filename) as f:
		lines = [line.strip() for line in f.readlines()]
		return lines

