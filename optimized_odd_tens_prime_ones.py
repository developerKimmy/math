import math

min_value = 10
max_value = 99
BASE = 10

def find_odd_tens(min_value = 10, max_value = 99, BASE = 10):
    odd_tens = []
    start = ((min_value - 1) // BASE + 1) * BASE
    # start = math.ceil(min_value / BASE) * BASE
    
    for i in range(start, max_value + 1, BASE):
        tens = i // 10
        if tens % 2 != 0:
            odd_tens.append(i)
    
    return [i for i in range(start, max_value + 1, BASE) if (i // 10) % 2 != 0]
   # return odd_tens


def find_prime_ones(number = 10):
    prime_ones = []
    primes = [True] * (number + 1)
    primes[0] = primes[1] = False
    
    for i in range(2, int(math.sqrt(number)) + 1):
        if primes[i]:
            for j in range(i*i, number + 1, i):
                primes[j] = False
    prime_ones = [i for i in range(1, number) if primes[i]]
    return prime_ones

print(find_odd_tens(min_value, max_value, BASE))
print(find_prime_ones(BASE))
print(len(find_odd_tens(min_value, max_value, BASE)) * len(find_prime_ones(BASE)))
