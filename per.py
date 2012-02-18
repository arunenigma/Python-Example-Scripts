def fact(n):
	if(n <= 1): 
		return 1
	else:
		return n*fact(n-1)

def GeneratePermutation(n, k, i):
	numberSet = range(1, n+1)
	permutation = []
	elementsLeft = n
	while(len(permutation) < k):
		permutation += [numberSet[i % elementsLeft]]
		numberSet.remove(numberSet[i % elementsLeft])
		i /= elementsLeft
		elementsLeft -= 1
	return permutation

def GenerateAllPermutations(n, k):
	permutationCount = fact(n) / fact(n-k)
	i = 0
	while i < permutationCount:
		print GeneratePermutation(n, k, i)
		i += 1
	return permutationCount

print "Permutations for 6 P 3"
print GenerateAllPermutations(6, 3), "permutations generated!"