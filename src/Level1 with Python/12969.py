import sys

a, b = map(int, sys.stdin.readline().split())
for i in range (b):
    for j in range (a):
        sys.stdout.write("*")
    sys.stdout.write("\n")