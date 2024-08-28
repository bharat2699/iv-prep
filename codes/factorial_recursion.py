import sys

sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")

n = int(input())


def fact_rec(n):
    if n == 0:
        return 1
    print(n * fact_rec(n - 1))
    return n * fact_rec(n - 1)


print(fact_rec(n))
