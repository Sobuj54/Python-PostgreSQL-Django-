# default arguments
# here a and b are given default values of 0
def sum(a = 0, b = 0):
    print(a+b)

# only one arg is sent but it won't be a problem because of default arg
sum(10)


# kargs or variable length argument
# * creates a tuple
def total(a,b,*args):
    print(a,b,args)
    # accessing values of args
    for val in args:
        print(val)

total(10,20,30,40,50)