#@title Default title text
fish = input('จำนวนปลาซาร์ดีน  ')
tomato = input('จำนวนมะเขือเทศ  ')
fish = int(fish)
tomato = int(tomato)

f_can = int(fish / 3)
t_can = int(tomato / 2)

if (f_can < t_can):
  result = f_can
else:
  result = t_can

print('ผลิตปลากระป๋องได้ ', result, ' กระป๋อง')
print('ปลาซาร์ดีนเหลือ ',fish - (result*3), ' ตัว')
print('มะเขือเทศเหลือ ',tomato - (result*2), ' ผล')
