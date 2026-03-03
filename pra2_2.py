"""In a steel plant, the quality of steel is graded according to the following conditions:
(i) Hardness must be greater than 50
(ii) Carbon content must be less than 0.7
(iii) Tensile strength must be greater than 5600
The grades are as follows:
Grade is 10 if all three conditions are met
Grade is 9 if conditions (i) and (ii) are met
Grade is 8 if conditions (ii) and (iii) are met
Grade is 7 if conditions (i) and (iii) are met
Grade is 6 if only one condition is met
Grade is 5 if none of the conditions are met
Construct a program, which will require the user to give values of hardness, carbon content and tensile strength of
the steel under consideration and output the grade of the steel."""

Hardness=float(input("Enter Hardness of steel: "))
Carbon=float(input("Enter Carbon content of steel: "))
Tensile=float(input("Enter Tensile streangth of steel: "))

if ((Hardness>50) and (Carbon<0.7) and (Tensile>5600)):
    print("Grade 10")
elif ((Hardness>50) and (Carbon<0.7)):
    print("Grade 9")
elif ((Carbon<0.7) and (Tensile>5600)):
    print("Grade 8")
elif ((Hardness>50) and (Tensile>5600)):
    print("Grade 7")
elif ((Hardness>50) or (Carbon<0.7) or (Tensile>5600)):
    print("Grade 6")
else:
    print("Grade 5")