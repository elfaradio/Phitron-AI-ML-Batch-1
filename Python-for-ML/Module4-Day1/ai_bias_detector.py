s = input().split()


c = s.count('A')
c1 = s.count('B')
# print(c, c1)

l = len(s)

A = (c/l)*100
B = (c1/l)*100

# print(A, B)
if A > 70 or B > 70:
    print("Biased Model")
else:
    print("Fair Model")
