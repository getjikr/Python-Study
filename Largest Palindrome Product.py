# Project Euler Problem 4: Largest Palindrome Product
# 링크: https://projecteuler.net/problem=4
# 문제: 세 자리 수를 곱해 만들 수 있는 가장 큰 대칭수(Palindrome) 구하기

def is_palindrome(a:int):
    return str(a) == str(a)[::-1]

result = 0
for i in range(999, 99, -1):
    for j in range(i, 99, -1):  # 중복을 줄이기 위해 i 부터 시작
        product = i*j
        if product <= result:
            break
        if is_palindrome(product):
            result = product

if __name__ == "__main__":
    print(result)