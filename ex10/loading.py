import time


# def ft_progress(listy):
# 	start_time = time.time()
# 	iter_time = 0
# 	for i in listy:
# 		if 

if __name__ == "__main__":
	listy = range(1000)
	ret = 0
	for elem in ft_progress(listy):
		ret += (elem + 3) % 5
		time.sleep(0.01)
	print()
	print(ret)