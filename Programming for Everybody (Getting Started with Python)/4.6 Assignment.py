def computepay(hrs,rate):
    hrs = input("Enter Hours:")
    rate = input("Enter Rate Per Hour:")
    hrs = float(hrs)
    rate = float(rate)
    if hrs > 40:
        hr = hrs - 40
        gross = (hr*rate*1.5)
        gross1 = (40*rate)
        pay1 = gross + gross1
    else:
        pay2 = (hrs*rate)
print("Pay",computepay(hrs,rate))
