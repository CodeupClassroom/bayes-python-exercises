data_types = [
    "bool"
    "int"
    "list"
    "string"
    "float"
    "dictionary"
    "tuple"
    "set"
    "function"
    "None"
    "class"
]

# list of lists
x = [[1, 2], [3, 4], [5, 6]]
print(x)
print(type(x))
print(type(x[0]))

# tuple of tuples -> immutable
x= ((1, 2), (3, 4))
print(x)
print(type(x))
print(type(x[0]))

# string are immutable
fruit = "banana"
print(fruit[0]) # points to the first character
fruit[0] = "B" # we cannot reassign pieces of a string because strings are immutable 

# list of dictionaries are super common


applications_where_python_is_used_heavily = [
    "Popular spaces/applications for Python"
    "Life Sciences + Hard sciences"
    "Data Science (ML, Deep Learning, Computer vision)"
    "Cyberdefense & systems hardening"
    "Systems automation"
    "Dev-Ops (intersection of programming and infrastructure) - software defined infrastructure"
    "Robotics"
    "Edge computing (IOT)"
    "Web Development"
    "Building APIs + services"
]

for application in applications_where_python_is_used_heavily:
    print(applications_where_python_is_used_heavily)

