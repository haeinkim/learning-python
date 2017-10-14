'Hello World' == "Hello World" == """Hello Wolrd"""
"hello".capitalize() == "Hello"
"hello".replace("e", "a") == "hello"
"hello".isalpha() == True
"123".isdigit() == True # Useful when converting to int
"some, csv, values".split(",") == ["some", "csv", "values"]

# String Format Function
name = "PythonBo"
machine = "HAL"
"Nice to meet you {0}. I am {1}".format(name, machine)
f"Nice to meet you {name}. I am {machine}"
