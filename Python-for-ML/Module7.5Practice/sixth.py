''' Write a Python program to count how many lines are in a text file named story.txt.
 If the file does not exist, handle the exception and print an error message, otherwise read the text file ( test it with both conditions ). Print a message finally. 
'''


try:

    with open("story.txt", "r") as f:
        l = f.readlines()
        print("Number of l in the f:", len(l))

except FileNotFoundError as e:

    print(e)

finally:

    print("Program finished.")
