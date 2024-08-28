import sys

sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")

n = int(input())

rev = 0
temp = n

while temp != 0:
    ld = temp % 10
    rev = rev * 10 + ld
    temp = temp // 10
if rev == n:
    print("IS PALINDROME")
else:
    print("NOT PALINDROME")
