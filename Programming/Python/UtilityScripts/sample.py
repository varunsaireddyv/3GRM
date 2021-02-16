hrs = input("Enter Hours:")

h = float(hrs)

rate = input("Enter the Rate:")

r = float(rate)

pay=0

if h <= 40 :
    pay=h*r
    print(pay)

else :
    pay=40*r
    extra_hours=h-40
    pay=pay+(extra_hours*r*1.5)
    
    print(pay)