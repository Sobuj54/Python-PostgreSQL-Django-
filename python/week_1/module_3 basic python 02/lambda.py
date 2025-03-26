# lambda 

# def double (x):
#     return x*2

# above function can be written as lambda
double = lambda x : x*2
mul = lambda x,y : x*y

print(double(2))
print(mul(2,5))

nums = [1,2,3,45,6]
# map(function, iterable)
doubled_nums = map(lambda x: x*2, nums)
print(list(doubled_nums))

actors = [
    {"name": "shabana", "age": 65},
    {"name": "sabila", "age": 29},
    {"name": "tania", "age": 30},
    {"name": "laila", "age": 25},
]

juniors = filter(lambda actor : actor["age"] <= 30, actors)
print(list(juniors))