def steps(x, y):
	print(y)
	if x == y:
		return 0
	if x > y:
		return x - y
	if x<=0 and y>0:
		return -1
	if y > x and x > 0:
		if y % 2  == 1:
			return 1 + steps(x, y+1)
		else:
			return 1 + steps(x, y/2)

print("Step: ", str(int(steps(6,26))))