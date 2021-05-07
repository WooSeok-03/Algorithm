alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet = list(alphabet)
S = str(input())
answer = []

for i in alphabet:
	answer.append(str(S.find(i)))
	
print(" ".join(answer))