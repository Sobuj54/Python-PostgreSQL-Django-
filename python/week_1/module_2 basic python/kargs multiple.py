def con(first, mid, last):
    return f"{first} {mid} {last}"

full = con("md","sobuj","ahmed")
print(full)

# i can also not maintain the args order
full = con(last="ahmed", first="md", mid="sobuj")
print(full)

# kargs or key arguments
# ** creates a dictionary or object(key value pair)
def full_name(first,last, **kargs):
    print(kargs)
    for key,val in kargs.items():
        print(f"key: {key}  val: {val}")

full_name(first="so", last="bu", title="student", age=50)


# return multiple values
def a_lot(a,b):
    sum = a+b
    mul = a*b
    div = a//b
    # return [sum,mul,div] or,
    return sum,mul,div

many = a_lot(100,5)
print(many)