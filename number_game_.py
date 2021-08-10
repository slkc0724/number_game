import random
x = input('Range (1-?): ')
x = int(x)
r = random.randint(1, x)
time = 0
while True:
	time = time + 1
	q = input('Number: ')
	q = int(q)
	if q == r:
		print('correct!!!')
		break
	else:
		print('wrong')
		if r > q:
			print('your ans is smaller than the correct ans')
		elif q > r:
			print('your ans is bigger than the correct ans')
		print('u have guessed', time, 'time')