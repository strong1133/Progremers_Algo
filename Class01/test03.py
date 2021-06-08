# 2021-06-08 2강_실습-2: 리스트에서 원소 찾아 내기

def solution(L, x):
    if x in L:
        return [i for i, y in enumerate(L) if y == x]
    else:
        return[-1]


L = [2, 3, 4, 9, 8, 5, 8, 10]
x = 8
print(solution(L, x))
