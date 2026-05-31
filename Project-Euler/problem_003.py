# # Project Euler Problem 3: Largest Prime Factor
# # 링크: https://projecteuler.net/problem=3
# # 문제: 600851475143의 가장 큰 소인수 구하기

def is_prime(a):
    for i in range(2,a):
        if a % i == 0:
            return False
    return True

def max_prime_factor(a):
    for i in range(a,1,-1):
        if a % i == 0 and is_prime(i):
            return i
    return 1

print(max_prime_factor(600851475143))