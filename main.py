def sortedSquaredArray(array):
	newarray = [x*x for x in array]
	newarray.sort()
	return newarray

if __name__ == "__main__":
	arr = [1, 2, 3, 5, 6, 8]
	out = sortedSquaredArray(arr)
	print(arr)
