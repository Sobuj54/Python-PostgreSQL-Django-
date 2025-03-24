num = 0

while num < 10:
    num += 1
    if num % 2 is not 0:
        continue
    print(num)
    if num is 7:
        break