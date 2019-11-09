# The opening question should ask the salary and the Name
print("Enter your name here:", )
while (True):
    Name = input()
    if not any(i.isdigit() for i in Name):
        break
    else:
        print("Name cannot contain any numbers. Enter your name:", )

print("Your annual salary:", )
while (True):
    Salary = input()
    if Salary.isdigit():
        break
    else:
        print("Salary must be a number. Your annual salary:", )

Q1 = "Do you recieve an income tested benefit ?"
Q2 = "Is this tax code for the income tested benefit? "
Q3 = "Is this tax code for the main or highest source of income? "
Q4 = "Are you NZ tax resident? "
Q5 = "Are you or your employee’s partner entitled to Working for Families Tax Credits?"
Q6 = "Do you have a NZ student loan? "

Tax_Code1 = "M"
Tax_Code2 = "ME SL"
Tax_Code3 = "ME"
Tax_Code4 = "M SL"
Tax_Code5 = "M"

A1 = input(Q1)
if A1 == "yes":
    A2 = input(Q2)
    if A2 == "yes":
        print(Name, "your TaxCode is ", Tax_Code1)
    elif A2 == "no":
        print("Sorry, but we can not find the right Tax code for you.")

elif A1 == "no":
    A3 = input(Q3)
    if A3 == "no":
        print("Sorry, but we can not find the right Tax code for you.")
    elif A3 =="yes":
        A4 = input(Q4)
        if A4 == "yes":
            A5 = input(Q5)
            if A5 == "no":
                A6 = input(Q6)
                if A6 == "yes":
                    print(Name, " Your TaxCode is", Tax_Code2, ".")
                elif A6 == "no":
                    print(Name, "your TaxCode is ", Tax_Code3, ".")
            elif A5 == "yes":
                A6 = input(Q6)
                if A6 == "yes":
                    print(Name, " your TaxCode is", Tax_Code4, ".")
                if A6 == "no":
                    print(Name, "your TaxCode is", Tax_Code5, ".")
        elif A4 == "no":
            A6 = input(Q6)
            if A6 == "yes":
                print(Name, "your TaxCode is ", Tax_Code4, ".")
            elif A6 == "no":
                print(Name, "Your TaxCode is ", Tax_Code5, ".")

print("Thank you for answering the questions.")













