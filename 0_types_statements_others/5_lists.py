student_names = []
student_names = ["Mark", "Katarina", "Jessica"]

# Getting List Elements
student_names[0] == "Mark"
student_names[2] == "Jessica"
student_names[-1] == "Jessica"

# Changing List Elements
student_names[0] = "James"
student_names == ["James", "Katarina", "Jessica"]

# List Functions
student_names[3] = "Homer" # No can do!
student_names.append("Homer") # Add to the end
student_names == ["Mark", "Katarina", "Jessica", "Homer"]
"Mark" in student_names == True # Mark is still there!
len(student_names) == 4 # How many elements in the list
del student_names[2] # Jessica is no longer in the list:(
student_names = ["Mark", "Katarina", "Homer"]

# List Slicing
student_names = ["Mark", "Katarina", "Homer"]
student_names[1:] == ["Katarina", "Homer"]
student_names[1:-1] == ["Katarina"]
