x = input("Enter score:")
x = float(x)
if x > 1.0:
    print("Error")
elif x < 0.0:
    print("Error")
elif x >= 0.9:
    print("A")
elif x >= 0.8:
    print("B")
elif x >= 0.7:
    print("C")
elif x >= 0.6:
    print("d")
elif x < 0.6:
    print("F")
else:
    print("Error")
