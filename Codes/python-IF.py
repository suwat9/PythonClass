from traitlets.traitlets import default
dayOfWeek = 7
dayOfWeek = dayOfWeek % 7   #หารเอาเศษ

if (dayOfWeek==0):
  print('อาทิตย์')
elif (dayOfWeek==1):
  print('จันทร์')
elif (dayOfWeek==2):
  print('อังคาร')
elif (dayOfWeek==3):
  print('พุธ')
elif (dayOfWeek==4):
  print('พฤหัสฯ')
elif (dayOfWeek==5):
  print('ศุกร์')
elif (dayOfWeek==6):
  print('เสาร์')
#else:
#  print('ไม่รู้วันอะไร')

def numbers_to_weekDay(argument):
    switcher = {
        0: "อาทิตย์",
        1: "จันทร์",
        2: "อังคาร",
        3: "พุธ",
        4: "พฤหัสฯ",
        5: "ศุกร์",
        6: "เสาร์"
    } 
    return switcher.get(argument, "ไม่รู้วันอะไร")

print(numbers_to_weekDay(7))


def numbers_to_month(m):
  switcher = {
      0: "January",
      1: "February",
      2: "March",
      3: "April",
      4: "May",
      5: "June",
      6: "July",
      7: "August",
      8: "September",
      9: "October",
      10: "November",
      11: "December"
  }
  return switcher.get(m, "unknow")

print(numbers_to_month(36 % 12))
