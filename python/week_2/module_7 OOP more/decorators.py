def do_something(func):
    def inside(*args, **kwargs):
        print("doing something before")
        func(*args, **kwargs)
        print("doing something after")
    return  inside

@do_something  # custom decorator
def add(a:int, b:int):
    print(a*b)

add(10, 20)

# do_something(add)()  the same thing is done above using decorator