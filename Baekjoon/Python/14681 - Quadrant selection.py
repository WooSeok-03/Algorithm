x = int(input())
y = int(input())

if x > 0 and y > 0:		# The First Quadrant
	print("1")
elif x < 0 and y > 0:	# The Second Quadrant
	print("2")
elif x < 0 and y < 0:	# The Third Quadrant
	print("3")
elif x > 0 and y < 0:	# The Fourth Quadrant
	print("4")