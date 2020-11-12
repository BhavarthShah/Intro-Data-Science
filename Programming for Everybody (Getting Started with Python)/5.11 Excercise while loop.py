while True:
    x = input("Enter a number: ")
    for k in x:
        if x == "done":
            print(k)
            break
    try:
        x = int(x)
    except:
        print("Invalid Input")

