s = input().strip()
# print(s
# )

mp = {}

for i in s:
    mp[i] = mp.get(i, 0)+1


# print(mp)
for i in sorted(mp):
    print(i, ":", mp[i])
