import time


def ft_progress(listy):
	start_time = time.time()
	iter_num = 0
	porcet = 0
	eta = 0
	for iter_num in listy:
		iter_num += 1
		if iter_num > 1:
			eta = (len(listy) - iter_num) * (iter_num / (current_time - start_time)) / 10000
		current_time = time.time()
		visual_num = iter_num / len(listy) * 30
		porcet = iter_num / len(listy) * 100
		print(f'\rETA: {eta:.2f}', ' ',
		f'[{int(porcet)}%]',
		'[','=' * int(visual_num), '>' if porcet < 100 else '',
		' ' * int(30 - visual_num), ']', ' ', iter_num,'/',len(listy), ' ',
		'| elapsed time ', f'{(current_time - start_time):.2f}',
		sep='',end='',flush=True)
		yield iter_num 



if __name__ == "__main__":
	listy = range(1000)
	ret = 0
	for elem in ft_progress(listy):
		ret += (elem + 3) % 5
		time.sleep(0.01)
	print("\n...")
	print(ret)
