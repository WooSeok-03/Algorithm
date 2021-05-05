N = num = int(input())
count = 0

while True:
	a = N // 10
	b = N % 10
	c = a + b
	N = int(str(b) + str(c%10))
	count += 1
	
	if N == num:
		break

print(count)