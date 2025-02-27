# Functions 
def add_number(a = 4, b = 5):
    return(a + b)


print(add_number(50, 20))

# Grades students results ----
def grader(mark):
    if mark >= 70:
        return("A")
    elif mark >= 60:
        return("B")
    elif mark >= 50:
        return("C")
    elif mark >= 40:
        return("D")
    else:
        return("Fail")
    
print(grader(35))

results = [23, 45, 60, 12, 75, 60, 55]

for i in results:
    grader(i)

# List comprehension ----
[grader(i) for i in results]

# A function that takes numbers and adds them up
def adder(*numbers):
    total = 0
    for number in numbers:
        total = total + number
    return(total)

print(adder(1, 2, 3, 10))

# A function that takes numbers and multiplies them up
def multiplier(*numbers):
    total = 1
    for number in numbers:
        total = total * number
    return(total)

print(multiplier(1, 2, 3))

########################################
# Dictionaries ----
# Key value pairs 
{"name": "Owen", "Age": 15, "country": "Kenya", "county": "Vihiga"}
student = dict(name = "Owen", Age = 15, country = "Kenya", county = "Vihiga")
student.keys()
student.values()
student.get("Weight", "Not found")
student["Age"]

student["height"] = 76

for key,value in student.items():
    print(key, value)

# Exceptions (Errors)----
def divider(a, b):
    try:
        return(a / b)
    except ZeroDivisionError:
        print("Cannot divide by zero")

divider(a = 5, b = 0)

# Import the modules ----
import pandas as pd

pd.read_excel("Programmes Review Board - data template.xlsx")
# pandas
# matplotlib
# seaborn
# numpy
# pip install numpy 
