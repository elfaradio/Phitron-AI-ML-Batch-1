s = input().split()

a = ["ai", "data", "model", "learn", "train", "neural"]

c = 0

# ans = [c += 1 x for x in s if x in a]
# print(ans)

for i in s:
    if i in a:
        c += 1
if c >= 2:
    print("AI Detected")
else:
    print("Not AI Related")
