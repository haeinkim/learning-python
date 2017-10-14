number = 5
if number == 5:
    print("Number is 5")
else:
    print("Number is NOT 5")

# Truthy and Falsey Values
number = 5
if number:
    print("Number is defined and truthy")

text = "Python"
if text:
    print("Text is defined and truthy")

# Boolean and None
python_course = True
if python_course: # Not python_course == True
    print("This will execute")
aliens_found = None
if aliens_found:
    print("This will NOT execute")

# Not if
number = 5
if number != 5:
    print("This will not execute")

python_course = True
if not python_course:
    print("This will NOT execute")

# Multiple if conditions
number = 3
python_course = True
if number == 3 and python_course:
    print("This will execute")

if number == 17 or python_course:
    print("This will also execute")

# Ternary if statements
a = 1
b = 2
"bigger" if a > b else "smaller"

