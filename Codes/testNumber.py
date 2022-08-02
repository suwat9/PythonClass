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

from datetime import datetime, timedelta,time

    
d = datetime.today() + timedelta(days=2)
print(d)

yearofBirth = 2546-543
dayofBirth = datetime(yearofBirth,10,5)

print(dayofBirth)
print("Age : ",datetime.now().year-dayofBirth.year)

studyTime = datetime(2022,8,2,hour=8,minute=30,second=00)
print(studyTime)

time_change = timedelta(minutes=30)
finish = studyTime + time_change

dayofweek = ['จันทร์','อังคาร','พุธ','พฤหัสฯ','ศุกร์','เสาร์','อาทิตย์']
#Return the day of the week as an integer, where Monday is 0 and Sunday is 6.
daywk = studyTime.weekday()
monthstr = ['','มกราคม','กุมภาพันธ์','มีนาคม','เมษายน','พฤษภาคม','มิถุนายน','กรกฎาคม','สิงหาคม',
            'กันยายน','ตุลาคม','พฤศจิกายน','ธันวาคม']
monthNo = studyTime.month
yearthai = studyTime.year + 543

print(dayofweek[daywk]+finish.strftime(' %d '+monthstr[monthNo]+' '+str(yearthai)+' %H-%M-%S'))
