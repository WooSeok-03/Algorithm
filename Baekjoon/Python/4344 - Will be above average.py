C = int(input())

for i in range(C):
	count = 0
	arr = list(map(int, input().split()))
	average = sum(arr[1:]) / arr[0]
	
	for score in arr[1:]:
		if score > average:
				count += 1
	result = count / arr[0] * 100
	print("{:.3f}%".format(result))