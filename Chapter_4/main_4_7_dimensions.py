# tuples don't need the parentheses; it just makes them look neater
# a tuple with a single element must contain a trailing comma

dimensions = (200, 50)
print("Original dimensions: ")
for dimension in dimensions:
    print(dimension)
dimensions = (400, 100)
print("\nModified dimensions: ")
for dimension in dimensions:
    print(dimension)