N = int(input())

for i in range(N):
	score = 0
	extra_score = 1
	ox_list = list(str(input()))
	for j in ox_list:
		if j == 'O':
			score += extra_score
			extra_score += 1
		else:
			extra_score = 1
	print(score)