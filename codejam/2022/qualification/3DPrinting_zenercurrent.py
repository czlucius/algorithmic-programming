"""
https://codingcompetitions.withgoogle.com/codejam/round/0000000000876ff1/0000000000a4672b
"""

T = int(input())

for i in range(T):
    C, M, Y, K = [], [], [], []

    for _ in range(3):
        c, m, y, k = list(map(int, input().split(" ")))
        C.append(c)
        M.append(m)
        Y.append(y)
        K.append(k)

    _min = [min(C), min(M), min(Y), min(K)]
    _min_v = sum(_min)
    if _min_v == 1000000:
        print(f"Case #{i + 1}:", " ".join(map(str, _min)))
        continue
    elif _min_v < 1000000:
        print(f"Case #{i + 1}: IMPOSSIBLE")
        continue

    diff = _min_v - 1000000
    for _i, c in enumerate(_min):
        if diff == 0:
            break
        if diff >= c:
            _min[_i] = 0
            diff -= c
        else:
            _min[_i] -= diff
            diff = 0

    print(f"Case #{i + 1}:", " ".join(map(str, _min)))
