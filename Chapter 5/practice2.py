# you are given a list of programming language:
#["python","java","c++","python","c","java"
# convert it into a set and print how many unique languages Soma knows

programmingList= ["python","java","c++","python","c","java"]
programmingSet= set(programmingList)

print(programmingSet)
print(f"Soma knows {len(programmingSet)} different languages")