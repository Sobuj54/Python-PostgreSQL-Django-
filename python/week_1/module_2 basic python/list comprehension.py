nums = [10,15,20,26,33,48]
odd = []

for num in nums:
    if num % 2 != 0:
        odd.append(num)

print(odd)

# another way of doing the same code in one line
odds = [num for num in nums if num % 2 != 0]
print(odds)