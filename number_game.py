import random
r = random.randint(1, 100)
while True:
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