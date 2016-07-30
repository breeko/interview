from math import sqrt

def find_primes(n):
    """ finds primes up to n """
    
    primes = []
    
    for num in range(1,n,2):
        for prime in primes:
            if num % prime == 0:
                continue
        primes.append(num)
    return primes

def find_primes2(n):
    """ finds primes up to n """
    candidates = [True for _ in range(n)]
    candidates[0] = False
    
    prime = 2
    
    while (prime < sqrt(n)):
        cross_off(candidates,prime)
        prime = get_next_prime(candidates)

def cross_off(candidates, prime):
    while (prime < len(candidates):
        candidates[prime] = False
        prime += prime

def get_next_prime(candidates, prime):
    candidate_num = prime + 1
    while (candidate_num < len(candidates) or candidates[candidate_num] == False):
        candidate_num += 1
    return candidate_num
    
        
            

def is_prime(n):
    """ Returns whether a number is a prime """
    if n % 2 == 0:
        return False
    
    while divisor < sqrt(n):
        if n % divisor == 0:
            return False
        divisor += 2
    return True

