#############################################################################
''' Question ONE
PART A: write a Python program that takes two inputs from the user (integers) and performs the
following:
    Add the two numbers. (5 marks)
    Subtract the second number from the first. (5 marks)
    Multiply the two numbers. (5 marks)
PART B: Create a function to divide the first number by the second and handle cases where
the second number is zero. (10 marks)'''

# Part A (Add and subtract)
first_number = input("Enter first number: ")
second_number = input("Enter second number: ")

## Convert the inputs to numbers 
first_number = float(first_number)
second_number = float(second_number)

## Add the numbers 
print(first_number + second_number)

## Multiply numbers 
print(first_number * second_number)

# PART B: Creating a function with error catching ability
# We start a function with the def keyword
def divider(number1, number2):
    try:
        return number1 / number2
    except ZeroDivisionError:
        print("Cannot divide by Zero")
        return(None)

print(divider(12, 0)) # You can play with the values here


#############################################################################
'''Question TWO
Write a Python program that takes a user’s age as input and:
    If the user is 18 years or older, print “You are an adult.”
    If the user is between 13 and 17, print “You are a teenager.”
    If the user is under 13, print “You are a child.” (15 marks
'''

age = 16 # You can change this value to see how program behaves

if age >= 18:
    print("You are an adult")
elif age >= 13 or age <= 17:
    print("You are a teenager")
else:
    print("You are a child")

#############################################################################
'''Question THREE
PART A: Write a Python program that prints the first 10 even numbers using a loop. (5 marks)
PART B: Modify the program to ask the user for a number ‘n’ and print the first ‘n’ even numbers.
(10 marks)
'''

# PART A
for i in range(21):
    if i % 2 == 0:
        print(i)

# PART B
my_range = input("Enter the range of numbers to be checked: ")

my_range = int(my_range) + 1 # Remember input function returns strings
# I add one because range function omits the last value
# Solution A
for i in range(my_range):
    if i % 2 == 0:
        print(i)

# Solution B
for i in range(my_range):
    if i % 2 != 0:
        continue
    print(i)

#############################################################################
'''Question FOUR
PART A: Create a list of 5 different products and their prices (use a list of tuples or a dictionary).
(5 marks)
PART B: Write a program to print out the most expensive product from the list. (10 marks)
'''

# Solution A: List of tuples
my_list = [("Eggs", 800), ("Milk", 200), ("Meat", 600)]

prices = []
for i in my_list:
    prices.append(i[1])

maximum = max(prices)
maximum

max_index = prices.index(maximum)

print("The most expensive good is " + my_list[max_index][0] + " and sells for " + str(my_list[max_index][1]))

# Solution 2: The dictionaries approach
my_dict = {"Eggs": 800, "Milk": 200, "Meat": 600}

max(my_dict, key=my_dict.get)


#############################################################################
'''Question FIVE
Write a Python program that takes a sentence as input and:
PART A: Converts the sentence to all uppercase. (5 marks)
PART B: Counts the number of vowels in the sentence. (10 marks)
'''

# PART A
sentence = input("Enter your sentence: ")
sentence.upper()

# PART B
vowels = ['a', 'e', 'i', 'o', 'u'] # list of vowels

counter = 0 # Start your counting of vowels at zero
for letter in sentence.lower():
    if letter in vowels:
        counter += 1 #Also written as counter = counter + 1

print(counter)

print(f"Your sentence has {counter} vowels.")


#############################################################################
'''QUESTION SIX
Write a Python program that writes a list of items to a text file, then reads the file and
prints its content to the console. (15 marks)
'''
# List of items to write to the file
items = ["Apples", "Bananas", "Cherries", "Dates", "Elderberries"]

# Write the list of items to a text file
with open("items.txt", "w") as file:
    for item in items:
        file.write(item + "\n")

# Read the file and print its content to the console
with open("items.txt", "r") as file:
    content = file.read()
    print("File contents:")
    print(content)

'''
### Explanation:
1. **Writing to the file**: 
   - Opens a file named `"items.txt"` in write mode (`"w"`).
   - Iterates over each item in the list and writes it to the file with a newline (`"\n"`).
2. **Reading from the file**:
   - Opens the same file in read mode (`"r"`).
   - Reads the entire content of the file and prints it to the console.
This program creates a file, writes each item on a new line, and then reads and displays the file content.
'''
