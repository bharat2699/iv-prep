import sys

sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")

n = int(input())


def easy_method(n):
    return len(str(n))


print("By easy method: ", easy_method(n))


def mathematical_method(n):
    res = 0
    while n > 0:
        n = n // 10
        res = res + 1
    return res


print("By Maths method: ", mathematical_method(n))
