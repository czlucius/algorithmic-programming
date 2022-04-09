"""
https://codingcompetitions.withgoogle.com/codejam/round/0000000000876ff1/0000000000a4621b
"""

N = int(input())

for i in range(N):
    print(f"Case #{i + 1}:")

    R, C = input().split(" ")
    print(".." + "-".join(list("+" * int(C))))
    print(".." + ".".join(list("|" * int(C))))

    for _ in range(int(R) - 1):
        print("-".join(list("+" * (int(C) + 1))))
        print(".".join(list("|" * (int(C) + 1))))

    print("-".join(list("+" * (int(C) + 1))))
