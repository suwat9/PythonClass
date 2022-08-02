s = 'สุวัฒน์'

print(s)
print(s[0])
print(s[4])

print(s[::-1])
print(s[:2])
print(s[-2:])

lastname = 'เตชะ'

fullname = s + ' ' + lastname

print(fullname)

split1 = list(fullname)
print(split1)

print(fullname.split())

for i in split1:
  print(i)

text= "Orange,Apple,Grapes,WaterMelon,Kiwi"
print(text.split(','))
