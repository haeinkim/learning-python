student = {
    "name": "Mark",
    "student_id": 15163,
    "feedback": None
}

# KeyError:
try:
    last_name = student["last_name"]
except KeyError:
    print("Error finding last_name")

print("This code executes!")

# TypeError and Exception:
student["last_name"] = "Kowalski"

try:
    last_name = student["last_name"]
    numbered_last_name = 3 + last_name
except KeyError:
    print("Error finding last_name")
except TypeError:
    print("I can't add these two together!")
except Exception:
    print("Unkown error")

print("This code executes!")

# Exception is not a good idea:
try:
    last_name = student["last_name"]
    numbered_last_name = 3 + last_name
except KeyError:
    print("Error finding last_name")
except TypeError as error:
    print("I can't add these two together!")
    print(error)

print("This code executes!")