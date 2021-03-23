# Set is {} unordered | unindexed | No duplicates

my_set = {"Chalk", "Duster", "Board"}
print(my_set)

# TypeError: 'set' object is not subscriptable
# print(my_set[1])

for x in my_set:
    print(x)

print("Chalk" in my_set) # True

my_set.add("Pen")
print(my_set)

my_set.update(["Pencil", "Eraser"])
print(my_set)

print(len(my_set))

my_set.remove("Pencil")
print(my_set)

my_set_2 = {"apples", 1, 2, 3, ('a', 'b')}
print(my_set_2)

my_list= [1, 2, 3]
print(my_list)
my_set_3 = set(my_list)
print(my_list)
print(my_set_3)

# Perform Mathematical calulcation such as UNION | Intersection | DIFF | Symmetric Diff
print("Below are results from example of Mathematical Calculations")
print("------------------------------------------------------------------------------------")
A = {"A", "B", 1, 2, 3}
B = {"B", "C", 3, 4, 5}

print(A.union(B))
print(A | B)
print(B.union(A))
print(A.intersection(B))
print(A & B)
print(B.intersection(A))
print(A.difference(B))
print(A - B)
print(B.difference(A))
print(A.symmetric_difference(B))
print(A ^ B)
print(B.symmetric_difference(A))