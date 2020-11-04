hrs = input("Enter Hours:")
hrs = float(hrs)
if hrs>40:
    hours = hrs - 40
    rate = input("Enter Rate Per hour:")
    rate = float(rate)
    gross = (rate*1.5)
    hrs = 40
pay = (gross*hours + rate*hrs)
print(pay)
