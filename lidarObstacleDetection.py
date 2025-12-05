distance=[50,40,30,20,10]
for d in distance:
	if d < 10:
		print("Stop! obstacle too close:",d)
		break
	print("Distance:",d)
