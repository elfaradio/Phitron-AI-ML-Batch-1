'''Problem:
 Write a Python program to:
Create a text file named data.txt


Write “Learning Python is fun!” into it.


Read the file and print its content.
'''


# with open('./Python-for-ML/Module7.5/data.txt', 'w') as f:
#     f.write("Learning Python is fun!")

with open('./Python-for-ML/Module7.5/data.txt', 'r') as f:
    ans = f.read()
    print(ans)
