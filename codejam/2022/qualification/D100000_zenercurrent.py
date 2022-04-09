"""
https://codingcompetitions.withgoogle.com/codejam/round/0000000000876ff1/0000000000a46471
"""

T = int(input())

for i in range(T):
    N = int(input())
    S = list(map(int, input().split(" ")))

    S.sort()
    _p = 0
    for d in S:
        if d > _p:
            _p += 1

    print(f"Case #{i + 1}: {_p}")
