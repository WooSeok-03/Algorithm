H, M = map(int, input().split())

if M >= 45:
	M -= 45
else:
	H -= 1
	if H < 0: H += 24
	M -= 45
	M += 60
	
print(H, M)