numbers = [2,3,49999,5,6,6,7,223,45,75,8,5,97,3200,5222,37,8,23,3,5,66,4,2,4,6,74,846,85,6,56,3,2,43,83,58,368,57,386,4,3,7,64]

def functionQuadSearch(numbers):
	greater = 0;

	for i in numbers:
		temp = i
		for j in numbers:

			if j>i:
				if j>greater:
					greater = j

	return greater

def functionLinearSearch(numbers):
	greater = 0
	for i in numbers:
		if i < greater:
			greater = i
	return greater 


print(functionQuadSearch(numbers))
print(functionLinearSearch(numbers))
