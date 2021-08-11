import random
x = input('start: ')
y = input('end: ')
x = int(x)
y = int(y)
r = random.randint(x, y)
time = 0
while True:
	time += 1 # time = time + 1
	q = input('Number: ')
	q = int(q)
	if q == r:
		print('correct!!!')
		print('u have guessed', time, 'time')
		break
	else:
		print('wrong')
		if r > q:
			print('your ans is smaller than the correct ans')
		elif q > r:
			print('your ans is bigger than the correct ans')
		print('u have guessed', time, 'time')
