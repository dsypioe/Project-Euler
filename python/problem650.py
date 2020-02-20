# probelm 650: 

# let B(n) be the product of binomeal coefficients. (all of the
# values of the binomeal expansion, multiplied)

# function binom takes n, and k and returns the list of
# all the binomial coefficients of n and k in the set 0 <= t <= k
def binom(n, k):
  expansion = [[0 for x in range(k+1)] for x in range(n+1)]
    
  # calculate the value of Binomial Coefficient in bottom up manner
  for i in range(n+1):
    for j in range(min(i, k) + 1):
      # Base cases
      if j == 0 or j == i:
        expansion[i][j] = 1
	
      else:
        expansion[i][j] = expansion[i-1][j-1] + expansion [i-1][j]
  return expansion[k]
 
 
def getDivisors(n):
    return [x for x in range(1, n+1) if (n/x).is_integer() == True]
  
def productOfList(lst):
  # Multiply elements one by one
  product = 1
  for x in lst:
    product = product * x 
  return product
 
def problem650(n):
    prodofBinomList = productOfList(binom(n,n))
    
    sum = sum(getDivisors(sum))
    
    print(sum)