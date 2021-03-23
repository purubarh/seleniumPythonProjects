# List is [] ordered | indexed | changeable | duplicates

my_list = ["Tokyo", "London", "New York"]
print(my_list)
print(my_list[0])
print(my_list[2])

my_list[2] = "New Delhi"
print(my_list)

for city in my_list:
    print(city)

print(len(my_list))

my_list.append("Boston")
my_list.insert(4, "Kolkata")
print(my_list)

my_list.reverse()
print(my_list)

my_list_2 = ["apple", [1, 2, 3], [30, 40],['a', 'b', 'c']]
print(my_list_2[1][2])
print(my_list_2[3][0])
