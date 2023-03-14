from sys import argv


is_first = True
for argv in argv[1:]:
	if not is_first:
		print(' ', end='')
	print(argv[::-1].swapcase(), end='')
	is_first = False