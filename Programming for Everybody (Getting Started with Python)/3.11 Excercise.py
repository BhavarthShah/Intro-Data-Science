x = input('Enter a score between 0.0 and 1.0: ')
try:
    x = float(x)
except:
    x = -1
if (x > 1.0):
    print("Over limit")
elif (x >= 0.9):
    print("A")
elif (x >= 0.8):
    print("B")
elif (x >= 0.7):
    print("C")
elif (x >= 0.6):
    print("D")
elif (x < 0.6 and x >= 0):
    print("F")
else:
    print("bad scoree")
    
