# 문제
# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 절댓값이 1,000,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.

# 출력
# 첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.

import sys

# input() 함수 대신 sys.stdin.readline을 사용하도록 덮어쓰기
input = sys.stdin.readline

N = int(input())
num = []

# 데이터 입력
for _ in range(N):
    num.append(int(input()))

# 데이터 정렬
sorted_numbers = sorted(num)

# 출력 속도 최적화: 결과를 문자열로 변환하고 줄바꿈(\n)으로 이어붙여 한 번에 출력
print('\n'.join(map(str, sorted_numbers)))