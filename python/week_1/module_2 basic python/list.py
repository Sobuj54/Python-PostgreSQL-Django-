# list is similar as array

# index =   0  1  2  3  4  5   forward indexing
numbers = [10,20,30,40,50,60]
# index =  -6 -5 -4 -3 -2 -1   backward indexing

print("forward index: ",numbers[0], "  backward index: ",numbers[-6])


# list[start index : end index] 
# gives a list from start index to just before end index(end index is exclusive)
print(numbers[1:5])
# output: [20, 30, 40, 50]

# in negative indexing
print(numbers[-4:-1])
# output :  [30, 40, 50]

# list[first index : last index : steps]
print(numbers[1:5:2])
print("all list shallow copy: ", numbers[:])
print("first few items: ", numbers[:4])
print("from start index to last: ", numbers[1:])
print("reverse: ", numbers[ : : -1])

