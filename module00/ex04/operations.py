import sys

if len(sys.argv) > 3:
	print("AssertionError: too many arguments")
	sys.exit(1)
if len(sys.argv) < 3:
	print("AssertionError: too few arguments")
	sys.exit(1)
try:
	num = int(sys.argv[1])
	num2 = int(sys.argv[2])
except ValueError:
	print("AssertionError: argument is not an integer")
	sys.exit(1)
print(f"Sum:        {num + num2}")
print(f"Difference: {num - num2}")
print(f"Product:    {num * num2}")
if num2 == 0:
	print("Quotient:   ERROR (division by zero)")
	print("Remainder:  ERROR (modulo by zero)")
else:
	print(f"Quotient:   {num / num2}")
	print(f"Remainder:  {num % num2}")