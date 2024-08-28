import sys

sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")

a = int(input())
b = int(input())

while a != b:
	if a > b