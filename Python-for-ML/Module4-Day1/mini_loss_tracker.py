n = int(input())
ans = float(input())
s = 0.0
for i in range(1, n+1):
    x = float(input())
    s += x

s /= n
if ans >= s:
    print("PASS")
else:
    print("RETRY")
