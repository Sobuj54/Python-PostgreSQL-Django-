name = 'john\'s doe'  #needs \ as escape character
name1 = "john's wick"
name2 = """
    ami eid er suti te
    bari jamu
"""

print(name)
print(name1)
print(name2)

for idx,char in enumerate(name):
    print(f"index:{idx}  and char:{char}")

print("string reverse: ",name1[ : : -1])
print("string slice: ", name1[1 : 4])

# string is immutable
# name[0] = 't'  is not possible

# check is something exists in string
if 'ick' in name1:
    print("exists")
else:
    print("doesn't exist")