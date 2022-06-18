dayfactor=0.01
dayup=1.0
for i in range(365):
    if i%7 in [6,0]:
        dayup*=(1-dayfactor)
    else:
        dayup*=(1+dayfactor)
print("{:.2f}".format(dayup))
    
