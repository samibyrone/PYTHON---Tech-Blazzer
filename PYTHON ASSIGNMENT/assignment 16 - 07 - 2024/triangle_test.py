
for triangle in range(20, 1, -1):
	for angle in range(triangle, 0, -1):
		print(angle, end = ' ')
	print()

sign = 1
while sign <= 10:
	print(sign * '5')
	sign = sign + 1


for num in range(5):
	for sum in range(10, 1):
		print(num, end = ' ')


#for sign in range(1, 11):
#	print(f "{sign * '*'} {'*' * (10 - sign): > 10} {'*' * (sign + 1) + '*' (10 - sign) : > 10}")




for i in range(1, 11):
	print(f "{i * '*' : > 10} {'*' * (10 - i) : > 10})
#	print(f "{i * '*': > 10} {'*' (10 - i): > 10}")