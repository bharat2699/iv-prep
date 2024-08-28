import sys

sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")

n = int(input())
fact = 1

# Usinf for in range loop
for i in range(2, n, 1):  # range(start, stop, step)
    fact = fact * i

print(fact)

# Using While loop
i = 2
while i <= n + 1:
    fact = fact * 1
    i = i + 1

print(fact)
