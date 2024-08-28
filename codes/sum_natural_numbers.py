import sys

sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")

n = int(input())
print(int(n*(n+1)//2))