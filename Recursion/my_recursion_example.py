def writeNumbers(aNumber):
	print(aNumber)
	if aNumber > 0:
		writeNumbers(aNumber - 1)
	else:
		return
