# list --> []
# tuple --> ()
# set --> {}
# set is unique collection of items

nums = [10,20,30,40,50, 50]
print("list : ", nums)  # [10,20,30,40,50,50]

nums_set = set(nums)
print("set : ",nums_set) # {40, 10, 50, 20, 30}

nums_set.add(100)
print("after add: ",nums_set)

nums_set.remove(50)
print("after remove: ",nums_set)

for num in nums_set:
    print(num)

if 50 in nums_set:
    print("exists")
else:
    print("doesn't exist")

A = {1,3,5, 10}
B = {1,2,3,5,7,8}
print("set intersection: " ,A & B)  # output: {1,3,5}  intersection
print("set union: ", A | B)  #output  {1, 2, 3, 5, 7, 8, 10} union