money = input("give me some money: ")
print("you gave me: ",money)
taka = input("give me taka: ")
print("taka: ", taka)

# input values are string by default
# that is why we need typecasting
total = int(money) + int(taka)  
print("total: ",total)
