def decode(encoded, first):
	arr = []
	arr.append(first)
	i = 0
	for each in encoded:
		arr.append(arr[i]^each)
		i += 1
	return arr