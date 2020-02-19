# Problem 3 : Largest prime factor

# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

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
		
def primeFactors(n):
	return [x for x in range(1, n + 1) if (n % x == 0) and (isPrime(x) == True)]
	

# solves the problem
def problem3(n):
	return max(primeFactors(n))
	