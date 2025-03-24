numbers = [1,2,3,4,5,6]
sum = 0

for num in numbers:
    print(num)
    sum += num

print("total: ",sum)

# iterating string
text = "ami sobuj"

for char in text:
    print(char)

# range(1,10)
for i in range(1,10):
    print(i)

# enumerate provides index and values of an array
for idx,val in enumerate(numbers):
    print(f"index: {idx} value {val}")