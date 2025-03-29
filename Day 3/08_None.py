a = None
while a == None:
    value = input("value").lower()
    if value == "quit" or value == "exit":
        break
    elif value:
        print("Your no:" +value)
        