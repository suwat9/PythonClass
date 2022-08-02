number = 7
digit1 = 0xA3
digit2 = 0o17
digit3 = 0b101111
print(number, digit1,digit2,digit3)

print(bin(20))
print(oct(20))
print(hex(20))

floating = 7.2858
f1 = 7/100
f2 = 7e-06

print(f1,'{:f}'.format(f2))

from datetime import datetime, timedelta
    
d = datetime.today() + timedelta(days=2)
print(d)

yearofBirth = 2546-543
dayofBirth = datetime(yearofBirth,10,5)

print(dayofBirth)
print("Age : ",datetime.now().year-dayofBirth.year)
