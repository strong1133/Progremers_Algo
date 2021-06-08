# 2021-06-08 1강_실습: 리스트원소 두개의 합을 구하라!
#

def solution(x):
    ans = x[0] + x[-1]
    return ans


x = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(solution(x))
