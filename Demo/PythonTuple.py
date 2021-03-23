# Tuple is () ordered | indexed | unchangeable | duplicates

my_tuple = ("apples", "oranges", "cherry")
print(my_tuple)

print(my_tuple[1])
print(my_tuple[-1])

print(my_tuple[0:3])

for fruits in my_tuple:
    print(fruits)
# tuple' object does not support item assignment
# my_tuple[1] = "Grapes"
# 'tuple' object doesn't support item deletion
# del my_tuple[1]

print(len(my_tuple))

my_tuple_2 =("apple", (1, 2, 3), ["Tokyo", "New Delhi"])
print(my_tuple_2)
print(my_tuple_2[2][1])
print(my_tuple_2[1][1])
my_tuple_2[2][1] = "New York"
print(my_tuple_2)

print("apple" in my_tuple_2)  # True
print("Cherry" in my_tuple_2) # false