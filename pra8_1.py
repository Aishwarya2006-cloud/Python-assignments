"""Perform the following File Handling Operations
a) Construct a program that reads a text file and writes its contents into a new text file with the same content,
but in uppercase."""

f1 = open("input.txt", "r")
data = f1.read()
f1.close()

f2 = open("output.txt", "w")
f2.write(data.upper())
f2.close()

print("Content copied in uppercase.")