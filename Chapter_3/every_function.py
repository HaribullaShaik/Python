rivers = []
rivers.append("Nile")
rivers.append("Amazon")
rivers.append("Yangtze")
# all the rivers are added to the list
print(rivers)
# inserting rivers at specific positions
rivers.insert(0, "Mississippi")
rivers.insert(2, "Danube")
# prints the list after inserting the rivers
print(rivers)
# removing rivers from the list
rivers.remove("Amazon")
print(rivers)
rivers.pop()
#prints the list after removing the last river
print(rivers)
rivers.append("Ganges")
print(rivers)
# sorting the list of rivers
rivers.sort()
print(rivers)
# length of the list of rivers
length_of_rivers = len(rivers)
print(f"Number of rivers in the list: {length_of_rivers}")
# using the sorted() function to sort the list of rivers without modifying the original list
sorted(rivers)
print(f"Sorted list of rivers: {sorted(rivers)}")
print(f"Original list of rivers: {rivers}")
sorted(rivers, reverse=True)
print(f"Reverse sorted list of rivers: {sorted(rivers, reverse=True)}")
print(f"Original list of rivers again: {rivers}")
rivers.reverse()
print(f"Reversed list of rivers: {rivers}")
rivers.reverse()
print(f"Original list of rivers again: {rivers}")
rivers.sort()
print(f"Sorted list of rivers: {rivers}")
rivers.sort(reverse=True)
print(f"Reverse sorted list of rivers: {rivers}")