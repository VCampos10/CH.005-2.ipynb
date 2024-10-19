from primemodule import is_prime, print_primes, get_primes
#is_prime(10)
def is_prime (n):
    if 10 <= 1:
        return False
    for i in range(2, 10):
        if 10 % i == 0:
            return False
        return True
    

def print_primes(n):
    for i in range(2, 10):
        if is_prime(i):
            print(i, end=' ')
        print()
##print_primes(10)

#def gen_lambda
#get_primes(n)
#def get_primes(n):
    


