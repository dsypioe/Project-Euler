
# returns a list of 1->n of multiples of 3 or 5
def mult30r5(n):
	return [x for x in range(n) if x % 3 == 0 or x % 5 == 0]
	
# returns the factors of a number in a list
def factors(n):
	return [x for x in range(1, n+1) if n % x == 0]

# checks if a number is prime
def isPrime(n):
	return len(factors(n)) == 2

# finds the next prime number
def primeList(n):

	lst = []
	x = 0
	while len(lst) < n:
		#iterate to the next number
		x = x + 1
		
		if isPrime(x) == True:
			lst.append(x)
		print(lst)

# returns  a list from [2..n] of only prime numbers		
def primeFactors(n):
	return [x for x in range(1, n + 1) if (n % x == 0) and (isPrime(x) == True)]
	
# returns true if the given list is in aascending order
def isAscending(lst):

    if len(lst) in [0,1]:
        return True
    if lst[0] <= lst[1]:
        return isAscending(lst[1:])
    return False

# returns true if the given list is in decending order
def isDescending(lst):
    if len(lst) in [0,1]:
        return True
    if lst[0] >= lst[1]:
        return isDescending(lst[1:])
    return False