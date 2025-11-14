marks=[99,100,90,95]
print("Maximum marks:",max(marks))
print("Minimum marks:",min(marks))

# modify list marks
marks[2]=98
print("Modified marks list:",marks)

# slicing
print("Sliced marks list (index 1 to 2):",marks[1:3])

# sort marks
marks.sort()
print("Sorted marks list:",marks)

# reverse marks
marks.reverse()
print("Reversed marks list:",marks)

# append new marks
marks.append(85)
print("Appended marks list:",marks)

# insert marks at index 2
marks.insert(2, 92)
print("Marks list after insertion:",marks)

# remove marks 100
marks.remove(100)
print("Marks list after removing 100:",marks)

# pop last element
last_mark = marks.pop()
print("Popped last mark:", last_mark)
print("Marks list after popping last element:",marks)

