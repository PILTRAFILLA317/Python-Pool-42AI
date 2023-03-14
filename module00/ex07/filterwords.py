import string
import sys

if len(sys.argv) != 3:
	print("ERROR")
	sys.exit(1)
try:
	num = int(sys.argv[2])
except ValueError:
	print("ERROR")
	sys.exit(1)
try:
	num = str(sys.argv[1])
except ValueError:
	print("ERROR")
	sys.exit(1)
final = sys.argv[1].translate(str.maketrans("", "", string.punctuation))
sep = final.split(" ")
printr = []
for x in sep:
	if len(x) >= int(sys.argv[2]):
		printr.append(x)
print(printr)