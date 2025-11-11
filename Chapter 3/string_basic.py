# String: A sequence of characters used to represent text data enclosed by single or double quotes or triple quotes for multi-line strings.
# String is immutable, meaning once created, its content cannot be changed.

str1='Hello'  
str2="Soma"
str3='''Python Course by Soma di.'''  

print(str1)
print(str2)     
print(str3)

# String Concatenation
print(str1 + " " + str2)  

# length of string
print("number of latters in string 2 is :",len(str2))

# String Indexing
print(str1[0])  # H

# string immutability
# str1[0]='B'  # This will raise an error