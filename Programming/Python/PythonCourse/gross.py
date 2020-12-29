def computepay(h, r):
    
    pay = 0

    if h <= 40:
        pay = h*r
    else:
        pay = 40*r
        extra_hours = h-40
        pay = pay+(extra_hours*r*1.5)
    return pay


hrs = float(input("Enter Hours:"))
rate = float(input("Enter the Rate:"))
p = computepay(hrs, rate)
print("Pay", p)
