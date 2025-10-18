s = input().split()

ans = max(s, key=lambda x: len(x) < 3)
print(ans)
