student_names = ["James", "Katrina", "Jessica", "Mark", "Bort", "Frank Grimes", "Max Power"]

for name in student_names:
    if name == "Mark":
        print("Found him!"  + name)
        break
    print("Currently testing " + name)

for name in student_names:
    if name == "Bort":
        continue # Continue onto the next iteration directly
        print("Found him!"  + name)
    print("Currently testing " + name)
