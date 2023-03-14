kata = (19,42,21)

print(f"The {len(kata)} numbers are: ", end="")
for i, value in enumerate(kata):
	print(value, end='')
	print(' ,', end='') if i < len(kata) - 1 else print('')