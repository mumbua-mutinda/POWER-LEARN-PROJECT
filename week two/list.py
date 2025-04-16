##Creation of my list
my_list = []
##Appending of numbers to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
## inserting 15 to the second position in the list
my_list.insert(1, 15)
##extending the list
my_list.extend([50, 60, 70])
##removing the last element in the list
del my_list[-1]
## list in ascending order
my_list.sort()
##index of 30
index_of_30 = my_list.index(30)
print("Index of 30:", index_of_30)
