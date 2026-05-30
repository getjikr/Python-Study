# Project Euler Problem 2: Even Fibonacci Numbers
# 링크: https://projecteuler.net/problem=2
# 문제: 피보나치 수열에서 400백만이 넘지 않는 짝수들의 합

# 초기 접근: while 조건문에서 (n1 + n2)를 미리 계산하여 범위를 제어하려고 했다.
# 문제점: 반복문 내부에서 n2가 400만을 초과하도록 업데이트된 후, 
#        조건 검사 없이 곧바로 짝수 판단(n2 % 2 == 0)을 수행하여 범위 밖의 숫자가 합산되는 버그가 발생했다.
# 해결책: 현재 조사 중인 항(n1) 자체를 while 조건문의 기준으로 삼고, 
#        안전하게 400만 이하임이 검증된 값만 짝수 검사를 하도록 순서를 변경하여 논리적 오류를 해결했다.
#        이를 통해 조건문의 경계값(Boundary Value)을 다룰 때는 연산과 검사의 순서가 매우 중요하다는 점을 배웠다.

n1 = 0
n2 = 1
result = 0
while n1 <= 4000000:
    if n1 % 2 == 0:
        result += n1
    n1, n2 = n2, n1 + n2

if __name__ == "__main__":
    print(result)