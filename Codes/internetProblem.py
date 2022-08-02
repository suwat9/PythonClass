charge = 15
hours = int(input('จำนวนชั่วโมงที่ใช้บริการอินเทอร์เน็ตคาเฟ '))
member = 100
discount = 0.9

Aprice = hours * charge
Bprice = (hours * charge * discount) + member

print('ค่าใช้บริการของ A จำนวน ',hours, ' ชั่วโมง คิดเป็นเงิน ',Aprice, ' บาท')
print('ค่าใช้บริการของ B จำนวน ',hours, ' ชั่วโมง คิดเป็นเงิน ',Bprice, ' บาท')
if Aprice > Bprice:
  print('สรุป A เสียค่าใช้จ่ายมากกว่า B')
else:
  print('สรุป B เสียค่าใช้จ่ายมากกว่า A')
