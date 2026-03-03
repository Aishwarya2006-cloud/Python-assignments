# Construct a program to store the following details of a Vendor of a Shop.
# a) Name of vendor
# b) Year of association
# c) Contact number
# d) eMail ID
# Read the details of monthly purchases from Vendor and generate a Annual Purchase/Billing report.

Name=input("Enter Vendor Name: ")
Year=input("Enter Year of Association: ")
Contact=input("Enter Contact Number: ")
Email=input("Enter eMail ID: ")

months=["January","February","March","April","May","June","July","August","September","October","November","December"]
total = 0
for month in months:
    print("For %s month:" %month)
    amount = float(input("Enter monthly purchase amount: "))
    total = total + amount

print("\nANNUAL PURCHASE REPORT")
print("Vendor Name:", Name)
print("Year of Association:", Year)
print("Contact Number:", Contact)
print("Email ID:", Email)
print("Total Annual Purchase:", total)