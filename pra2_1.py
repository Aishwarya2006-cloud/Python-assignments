# A)Develop a Python program that takes a voltage (V) and resistance (R) as inputs from the user and calculates the
# current (I) using Ohm’s Law.

# B)Modify the above program to display the nature of current:
# If current<0.5 A, print “Low current”
# If 0.5 A ≤ current ≤ 2 A, print “Normal current”
# If current >2 A, print “High current


v=int(input("Enter Voltage(V): "))
r=int(input("Enter Resistance(R): "))

#V=IR
I=v/r
print("Value of Current(I): ",I)



v=int(input("Enter Voltage(V): "))
v=int(input("Enter Resistance(R): "))

I=v/r

if (0.5>I):
    print("Low Current")
elif(0.5>=I and I<=2):
    print("Normal Current")
else:
    print("High Current")