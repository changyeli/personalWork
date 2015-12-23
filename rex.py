import re
files = open("files.txt")
s = []
for line in files:
	line = line.rstrip()
	numbers = re.findall("([0-9]+)", line)
	numbers = map(int, numbers)
	s = s + numbers
print s
print reduce(lambda x,y:x+y, s)
files.close()