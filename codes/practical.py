import sys

sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")

num = int(input())
temp = num


def palindrome(temp, num, rev=0):
    while temp != 0:
        ld = temp % 10
        rev = rev * 10 + ld
        temp = temp // 10
    return rev == num


print(palindrome(temp, num))
