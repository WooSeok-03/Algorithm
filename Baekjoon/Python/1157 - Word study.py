alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet = list(alphabet)
s = list(str(input()).upper())
answer = []

for i in alphabet:
	answer.append(s.count(i))

m = max(answer)
max_count = answer.count(m)
if max_count == 1:
	res = answer.index(m)
	print(alphabet[res])
else:
	print("?")
