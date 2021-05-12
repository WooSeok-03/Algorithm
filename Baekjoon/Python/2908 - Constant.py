A, B = map(str, input().split())

A = ''.join(reversed(A))
B = ''.join(reversed(B))

if A > B:
	print(int(A))
else:
	print(int(B))
	
# reversed()는 문자열을 뒤집어 준다. (list로 반환된다.)