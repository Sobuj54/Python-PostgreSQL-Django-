nums = [10,20,30,40,50,50,60]
# list.append(value) 
nums.append(70)
print("list after append: ", nums)

# list.insert(index, value)
nums.insert(0,1)
print("list after insertion: ",nums)

# list.extend(iterable): Adds all elements from another iterable (like list, tuple) to the list.
nums.extend([80,90,100])
print("list after extend: ",nums)

# list.remove(x): Removes the first occurrence of x in the list.
if 1 in nums:
    nums.remove(1)
print("list after remove: ",nums)

# list.pop(index): Removes and returns the element at index. If index is not given, removes the last element.
last = nums.pop()
print("list after pop: ",last, nums)
last = nums.pop(0)
print("list after pop with index: ",last, nums)

# list.index(x): Returns the index of the first occurrence of x.
if 30 in nums:
    idx = nums.index(30)
    print("index of the value is: ",idx)

# list.count(x): Returns the number of times x appears in the list.
cnt = nums.count(50)
print("count of a value: ",cnt)

# list.sort(): Sorts the list in ascending order.
nums.sort()
print("sorted in ascending order: ", nums)

# lst.sort(reverse=True) Sorts the list in descending order.
nums.sort(reverse=True)
print("sorted in descending order: ",nums)

# list.reverse(): Reverses the order of elements in the list.
nums.reverse()
print("reverse the list: ",nums)

# list.copy(): Creates a shallow copy of the list.
new_nums = nums.copy()
print("copied list: ",new_nums)

