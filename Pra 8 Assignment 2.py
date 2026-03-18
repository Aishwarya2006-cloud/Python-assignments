"""Develop an application using file handling to copy the contents of python script into another without including the comments Ask the user about the source and destination file names. Print the content of the both the files"""

source = input("Enter source file name: ")
dest = input("Enter destination file name: ")
f1 = open(source, "r")
f2 = open(dest, "w")
for line in f1:
    if not line.strip().startswith("#"):   
        f2.write(line)

f1.close()
f2.close()
print()
print("\nSource File Content:\n")
print(open(source).read())

print("\nDestination File Content:\n")
print(open(dest).read())