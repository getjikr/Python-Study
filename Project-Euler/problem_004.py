# Project Euler Problem 4: Largest Palindrome Product
# 링크: https://projecteuler.net/problem=4
# 문제: 세 자리 수를 곱해 만들 수 있는 가장 큰 대칭수(Palindrome) 구하기

# 100부터 999까지 모든 수를 이중으로 곱하다 보면 중복 연산이 너무 많아진다는 문제가 있었다.
# 이를 해결하기 위해 반복문을 999부터 99까지 역순으로 실행되도록 수정하였고, j는 i부터 시작하게 하여 중복 계산을 방지했다.
# 또한 역순으로 곱해나가기 때문에, 곱한 값이 이미 구한 최대 대칭수보다 작아지면 
# 안쪽 반복문을 즉시 탈출하게 설정하여 불필요한 연산을 줄였다.

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