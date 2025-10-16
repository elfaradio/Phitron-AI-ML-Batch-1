'''

Problem:
Given two sets of friends from two people, find the mutual friends, unique friends of each, and the total number of unique friends.
Example Input:
a_friends = {"Rahim", "Karim", "Sakib", "Jamal"}
b_friends = {"Sakib", "Jamal", "Rafiq", "Nadim"}

Expected Output:
Mutual friends: {'Sakib', 'Jamal'}
Unique to A: {'Rahim', 'Karim'}
Unique to B: {'Rafiq', 'Nadim'}
Total unique friends: 6


'''

a_friends = {"Rahim", "Karim", "Sakib", "Jamal"}
b_friends = {"Sakib", "Jamal", "Rafiq", "Nadim"}

print(a_friends.intersection(b_friends))
print(a_friends-b_friends)
print(b_friends-a_friends)
print(len(a_friends.union(b_friends)))
