import random
import sys

def main():
	i = 4
	lines = []
	for line in sys.stdin:
		lines.append(line.rstrip('\n'))
	value = int(lines[0])
	while i > 0:
		i = i - 1
		if value % 3 == 0:
			value = value / 3
		elif ((value % 2) == 0):
			value = value / 2
		else:
			value = value - 1
	print(int(value))

if __name__ == "__main__":
	main()
