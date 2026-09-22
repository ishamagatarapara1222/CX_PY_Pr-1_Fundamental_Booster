# Fundamental Booster

print("\n----- Welcome to Fundamental Booster Program. -----\n")

print("\n----- Information Collector -----\n")

print("\n")

name = input("Enter you Name: ")
age_str = input("Enter you Age: ")
height_str = input("Enter you Height in Meter: ")
fav_str = input("Enter you Favroute Number: ")

print("\n")

# Calculation, Converter and Arithmetic

age = int(age_str)
height = float(height_str)
fav = float(fav_str)
a = 2026
b = a - age
height_cm = height * 100
sum_value = age + fav
product_value = age * fav
heights = int(height)
ages = float(age)
age_str = str(age)

# Processing

print("\n----- Processing -----\n")

print(f"Your name is {name} | Type: {type(name)} |ID: {id(name)}")
print(f"Your age is {age} |Type: {type(age)} |ID: {id(age)}")
print(f"Your height is {height_str} |Type: {type(height_str)} |ID: {id(height_str)}")
print(f"Your favroute number is {fav} |Type: {type(fav)} |ID: {id(fav)}")
print(f"Your Born year as per your age is {b} |Type: {type(b)} |ID: {id(b)}")
print(f"Your Height in integer {heights} |Type: {type(heights)} |ID: {id(heights)}")
print(f"Your age in string {age_str} |Type: {type(age_str)} |ID: {id(age_str)}")
print(f"Your age in float {ages} |Type: {type(ages)} |ID: {id(ages)}")


# Display Opeartion

print("\n----- Display Operation -----\n")



print("Calculated Result")
print(f"Your height in centimeter is {height_cm} cm")
print(f"Sum of your age and favroute number is {sum_value}")
print(f"Multiplication of your age and favroute is {product_value}")



# String Concatination


print("\n----- String Concatination -----\n")




greeting = "Hello " + name + "!"
print(f"\n{greeting} Type: {type(greeting)} ID : {id(greeting)}")

print("\n")

# Summary Table


print("\n----- Summary Table -----\n")


print("\n")

print(f"\n {'name':<20}  {str(type(name)):<25} {id(name):<15}")
print(f"\n {'age':<20}  {str(type(age)):<25} {id(age):<15}")
print(f"\n {'height':<20}  {str(type(height)):<25} {id(height):<15}")
print(f"\n {'favroute':<20}  {str(type(fav_str)):<25} {id(fav_str):<15}")

print("\n")

# Closing Message


print("\n----- Closing Message -----\n")


print("\n")

print("Thank you using Personal Data collector \n")
print("you've been successfully explore -_- \n")
print("print() and input() function\n")
print("String, int, float, dat  types\n")
print("Arrithmetic operators ( + , * , / , - )\n")
print("type and id() built-in function\n")
print("string concatination\n")
print("Type casting\n")