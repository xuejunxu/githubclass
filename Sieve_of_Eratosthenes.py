"""
One of the first examples of an algorithm was the Sieve of Eratosthenes. 
This algorithm computes all prime numbers up to a specified bound. 
The provided code below implements all but the innermost loop for this algorithm in Python. 
Review the linked Wikipedia page and complete this code.
"""

#refer to the wikipedia link to implement the algorithm
#https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

def compute_primes(bound):
    """
    Return a list of the prime numbers in range(2, bound)
    """
    
    answer = list(range(2, bound))
    not_prime_numbers=[]
    for divisor in range(2, bound):
    	#print("divisor:",divisor) print out to test program
    	for int_i in range(2,int(bound**0.5)):
    		if (answer[divisor-2] in range(int_i**2,bound,int_i)) \
    		and (answer[divisor-2] not in not_prime_numbers):
    			not_prime_numbers.append(answer[divisor-2])
    for num in not_prime_numbers:
    	remove=answer.index(int(num))
    	answer.pop(remove)

        # Remove appropriate multiples of divisor from answer


    return answer

print(len(compute_primes(200)))
print(len(compute_primes(2000)))
print(compute_primes(200))
