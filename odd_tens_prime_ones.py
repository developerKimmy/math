# 기본 
import math

min_value = 10
max_value = 99

def find_odd_tens():
    odd_tens = []
    for i in range(min_value, max_value+1):
        if i % 10 == 0:
            tens = i // 10
            if tens % 2 != 0:
                odd_tens.append(i)
    return odd_tens

def find_prime_ones():
    prime_ones = []

    primes = [True] * 11
    primes[0] = primes[1] = False

    for i in range(2, 11):
        if primes[i]:
            for j in range(i*2, 11, i):
                primes[j] = False
    prime_ones = [i for i in range(1, 10) if primes[i]]
    return prime_ones

# 함수 호출 추가
find_odd_tens()
find_prime_ones()

print(f"홀수 십의자리 수: {find_odd_tens()}")
print(f"소수 일의자리 수: {find_prime_ones()}")
print(f"십의 자리의 수는 홀수이고, 일의 자리의 수는 소수인 자연수의 개수: {len(find_odd_tens()) * len(find_prime_ones())}")