import sys
from string import punctuation

def text_analyzer(*args):
	"""
	This function counts the number of upper characters, lower characters,
	punctuation and spaces in a given text.
	"""
	if len(args) < 1 or args[0] == 'None':
		text = input("What is the text to analyze?\n")
	else:
		text = args[0]
	if not isinstance(text, str):
		print("AssertionError: argument is not a string")
		return
	up = low = pm = sp = 0;
	for char in text:
		if char == ' ':
			sp += 1;
		elif char in punctuation:
			pm += 1;
		else:
			if char.isupper():
				up += 1;
			else:
				low += 1;
	print(f"{up} upper letter(s)")
	print(f"{low} lower letter(s)")
	print(f"{pm} punctuation mark(s)")
	print(f"{sp} space(s)")

if __name__ == "__main__":
	if len(sys.argv) > 2:
		print("AssertionError: more than one argument are provided.")
		sys.exit(1)
	elif len(sys.argv) == 2:
		text_analyzer(sys.argv[1])
	else:
		text_analyzer()
