s = input()

s = s.split()

if s.count("happy") or s.count("joy") or s.count("smile"):
    print("Happy Mood")
elif s.count("sad") or s.count("cry") or s.count("angry"):
    print("Sad Mood")
else:
    print("Neutral Mood")
