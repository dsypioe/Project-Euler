# Problem 3 : Largest prime factor

# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?


def factors(n):
	factors = [x for x in range(n) if n % x == 0]

def problem3(n):
	primes = [x for x in range (n) if isPrime(n) == True]