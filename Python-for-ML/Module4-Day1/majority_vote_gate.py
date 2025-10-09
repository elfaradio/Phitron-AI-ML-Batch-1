n = int(input())

c = 0

for i in range(1, n+1):
    s = input()
    if (s == "YES"):
        c += 1

n -= c

if (c >= n):
    print("ACCEPT")
else:
    print("REJECT")
