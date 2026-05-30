# Project Euler Problem 1: Multiples of 3 or 5
# 링크: https://projecteuler.net/problem=1
# 문제: 1000 미만의 정수 중 3 또는 5의 배수인 값들의 합

#파이썬의 제너레이터 표현식을 활용해 보았다.

sum(i for i in range(1000) if i % 3 == 0 or i % 5 == 0)