balance = 1000
taka = 10000

def shopping(spent):
    # if we want to modify global variables then we need to use global keyword
    global balance ,taka
    balance -= spent
    taka -= spent
    print(balance, "taka", taka)

shopping(500)