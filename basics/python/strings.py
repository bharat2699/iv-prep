# strings are Immutable

"""
Accessing string elements
"""
str_1 = "hello"
# str_1[2] = "h" # Throws error
print(str_1[2])  # l -> array like indexing

"""
Slicing string
"""
sub_str_1 = str_1[0:3]  # [start with element(default 0):number of elements]
print(sub_str_1)  # hel

"""
Length of the string
"""
length_str_1 = len(str_1)
print(length_str_1)  # 5

"""
Negative Slicing
"""
print(str_1[-1:-3])  # this is equivalent to str_1[len(str_1)-1:len(str_1)-3]
# dosen't print anything because str_1[4:2] makes no sense

print(str_1[0:-3])  # he => str_1[0:2]
print(str_1[0:-2])  # hel similar to str_1[0:3]


"""
Strings Method
"""
str_2 = "BhArAT"
# make title case
print(str_2.title())  # Bharat

# make lower case
print(str_2.lower())  # bharat

# make upper case
print(str_2.upper())  # BHARAT

# make sting capitalize by only converting ONLY first element of the string to upper case
str_no_cap = "luffy will be the King of Pirates"
print(str_no_cap.capitalize())  # Luffy will be the king of pirates

"""
Removing trailing characters using rstrip()
"""
str_3 = "What the Fuck, is this??????????????????"
print(str_3.rstrip("?"))  # What the Fuck, is this

"""
Replacing a word in string
"""
print(str_3.replace("Fuck", "Duck"))  # What the Duck, is this??????????????????

"""
Splitting a string into array, split("<<separator>>")
"""
print(str_3.split(" "))  # ['What', 'the', 'Fuck,', 'is', 'this??????????????????']
print(len(str_3.split(" ")))  # 5

"""
Count occurrence of certain element in a string using count("<<element>>") 
"""
str_4 = "Bharat is King of Pirates"
print(str_4.count("a"))  # 3

"""

"""
