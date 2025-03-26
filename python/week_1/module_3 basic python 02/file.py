# .csv  comma separated values
# txt text file

with open("message.txt","w") as file:
    file.write("hello world!")

with open("message.txt","a") as file:
    file.write("hello world!")

with open("message.txt","r") as file:
    text = file.read()
    print(text)

