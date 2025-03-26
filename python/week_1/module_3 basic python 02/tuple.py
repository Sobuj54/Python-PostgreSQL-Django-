# tuples are immutable by default
# if tuple contains immutables then that can not be changed
# but if tuple has mutable like list then that can be changed

def multiply(a,b):
    x = a*b
    y = a**b
    return x,y   #this will be returned as tuple

print(multiply(10,5))

things = "charger", "phone", "house", "car", "cat"
print(type(things))
print("slice tuple: ", things[1:4])
print("reverse tuple: ",things[ : : -1])
print("access tuple by index: ", things[4])
print("access tuple by index: ", things[-4])

# check if something exists in tuple
if "cat" in things:
    print("exists")

for item in things:
    print(item)

# things[0] = "toy"  this is not possible..this case tuple is immutable
print("tuple length: ", len(things))

# tuples itself is immutable but mutable data type in tuple can be changed
mega = ([1,5,4], [5,9,7])
# here i am changing list inside the tuple
mega[0][1] = 10   #the result is ([1, 10, 4], [5, 9, 7])
print(mega)