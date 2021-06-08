# 2021-06-08 2강_실습-1: 정렬된 리스트에 원소 삽입
#

def solution(L, x):
    for i in range(int(len(L))):
        if x < L[i]:
            L.insert(i, x)
            return L
    else:
        L.append(x)
        return L


L = [2, 3, 4, 5, 9, 10]
x = 8
print(solution(L, x))
