# Project Euler Problem 5: Smallest Multiple
# 링크: https://projecteuler.net/problem=5
# 문제: 1에서 20까지의 모든 정수로 나누어 떨어지는 가장 작은 자연수 구하기

def gcd(a,b):
    while b > 0:
        a,b = b, a%b
    return a

def lcm(a,b):
    return int((a*b)/gcd(a,b))

temp = 1
num = 2
while num < 21:
    temp = lcm(temp,num)
    num += 1

print(temp)