from collections import Counter
import sys

sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")

input_str = input()
s, t = str.split(input_str, ",")

print(s)
print(t)


def isAnagram(s: str, t: str):
    return Counter(s) == Counter(t)


print(isAnagram(s, t))
