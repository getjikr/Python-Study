# # Project Euler Problem 3: Largest Prime Factor
# # 링크: https://projecteuler.net/problem=3
# # 문제: 600851475143의 가장 큰 소인수 구하기

#아래의 코드에서 불필요한 전체 순회 방식을 제거하고 소인수분해 효율을 개선함.
#소인수분해의 수학적 원리를 활용해 구현하였다.

def max_prime_factor(num):
    d = 2
    temp = num
    while d ** 2 <= num:
        if temp % d == 0:
            temp //= d
        else:
            d += 1
    return temp