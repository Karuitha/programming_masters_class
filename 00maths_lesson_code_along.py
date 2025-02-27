# Arithmetic operations
# function()
print(5 + 6)
print(7 - 3)
print(9 * 2)
print(10 / 2)

# Exponentiation
print(2 ** 3)

# Modulus
print(10 % 3)

# Floor division
print(10 // 3)
print(-10 // 3)

# String concatenation
print("Hello" + " " + "World!")


# Atomic data structures in Python
# 1. float
# Can have fractions
type(3.14)

# 2. int
type(2)



# 3. str
type("hello")
print("I'm an adult!")

# 4. bool
type(True)
type(False)

# The concept of a variable and variable assignment
# variable name cannot start with number
# variable name cannot start with special characters
# variable name cannot contain spaces
# Let variable names be meaningful
# Assignment operator (=)
my_year_of_birth = 1990
print(my_year_of_birth)

2025 - my_year_of_birth

# Equality (==)
50 == 50
45 > 50
45 >= 50

# Height (cm)
height_in_cm = 180
height_in_meters = height_in_cm / 100

# Weight (kg)
weight_in_kg = 70

# BMI calculation
# BEDMAS
bmi = weight_in_kg / (height_in_meters ** 2)
print(bmi)

# My Names 
my_name = "John Karuitha"
print(my_name)

my_lucky_number = 5

my_float = 3.14

admitted = False

# Comparison operations
# == (equality)
# >=
# <= 
# >
# <

# Logical operations
# and
# or
# not

True or False
True and False
False and False
not True and not False

# String concatenation
# Combine 2 texts together
first_name = "Yvonne"
print(first_name)
surname = "Muturi"
print(surname)

print(first_name + " " + surname)


first_number = "1"
type(first_number)
second_number = "2"

print(first_number + second_number)


# Type conversions
third_number = "3"
type(third_number)
third_number = int(third_number)
type(third_number)

temperature = "False"
temperature = bool(temperature)
print(temperature)
type(temperature)

# Functions and Methods in Python
## Common functions 
## The print() function
help(print)


## The input() function
## The input function always returns a string
help(input)
my_password = input("Please enter your password: ")
print(my_password)

# Age of a person
current_year = 2025
type(current_year)
year_of_birth = input("Please enter year of birth: ")
type(year_of_birth)
print(year_of_birth)
age = current_year - int(year_of_birth)
print(age)

## The len() function
my_name = "Murimi"
print(len(my_name))


## The range() function
## Alaways excludes last number
help(range)

for i in range(1, 11, 2):
    print(i)





## The int(), float(), str(), and bool() functions


## The type() function



## There are many more functions 

# Methods in Python
## Functions specific to objects
## String methods
my_name = "John Karuitha"
my_name.upper()
my_name.lower()
my_name.count("a")
my_name.replace("a", "o")
print(my_name)



## Int methods
my_age = 37
my_age.is_integer()


## Float methods
my_weight = 65.7
my_weight.is_integer()

## Boolean methods
is_student = True
is_student.conjugate()




# Complex data types 
# Lists
## Ordered and mutable
## Can hold several data types
my_numbers = [1, 20, 3, 4, 5, 6, 17]
my_names = ["Patel", "Jane", "Diane"]
my_bools = [True, False, False]
my_list = ["Karuitha", True, 1, 5]

my_numbers.clear()
my_numbers.reverse()
print(my_numbers)
my_numbers.clear()

# Tuples


# Sets


# Dictionaries


# Loops and conditionals
## Conditionals
## if ....elif ....else




## For loops




## While loops



## Nested loops




## Creating functions 








## Modules in Python
## Numpy



## Pandas



## Matplotlib




## Seaborn




## There are thousands of modules




# Exception handling




# unit tests and the pytest module









