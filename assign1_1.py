# Construct a python program to store the information of an employee such as name, employee ID, department and generate
# the salary as per the following conditions:
# (i) DA is 92% of Basic Salary
# (ii) HRA is 58% of Basic Salary
# (iii) TA is 30% of Basic Salary
# (iv) LIC is deducted: Rs. 500 every month.

Name = input("Enter Employee Name: ")
ID = input("Enter Employee ID: ")
Dept = input("Enter Department: ")
BS = float(input("Enter Basic Salary: "))

DA = 0.92 * BS    
HRA = 0.58 * BS     
TA = 0.30 * BS     
LIC = 500                     

SFL = BS + DA + HRA + TA
SAL = SFL - LIC

print("Name:", Name)
print("Employee ID:", ID)
print("Department:", Dept)
print("Basic Salary: Rs.", BS)
print("DA (92%): Rs.", DA)
print("HRA (58%): Rs.", HRA)
print("TA (30%): Rs.", TA)
print("LIC Deduction: Rs.", LIC)
print("Salary before LIC deduction: Rs.", SFL)
print("Salary after LIC deduction: Rs.", SAL)

        