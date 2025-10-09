# a = map(int, input().split())
# print(a)
# a = list(map(int, input().split()))
# print(a)

a = input().split()
# print(a)

s = 0

# print((len(a)/2)-1)
for i in a:
    s += int(i)


s /= len(a)

# print(type(s))

if s < 85:
    print("Dark Image")
elif s <= 170:
    print("Normal Image")
else:
    print("Bright Image")
