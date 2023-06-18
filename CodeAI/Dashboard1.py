#ในการอ่านไฟล์จาก Google Drive ต้องเปลี่ยน link ด้านหลัง google.com
#ให้เป็น uc?id=<fileID>
# https://docs.google.com/spreadsheets/d/1mNF8AhJHqB0dsGvlCsOTtwyRU9DOlvwE/edit?usp=sharing&ouid=101951013568012492682&rtpof=true&sd=true
!gdown -O test1.xlsx 1mNF8AhJHqB0dsGvlCsOTtwyRU9DOlvwE

#-----------------------------------------------------------------
import pandas as pd

global dataset
dataset = pd.read_excel('test1.xlsx',None)

print(list(dataset.keys()))

df = dataset['sum_admit']
df['availablepercent']=df['available']/df['bedcount']
df[df['availablepercent']<0] = 0
print(df)

ward6869 = df[df['code'].isin([68,69])]
print(ward6869)

ward6 = df[df['code'].astype(str).str[:1]=='6']
print(ward6)

wardN1 = df[df['code'].astype(str).str[-1]=='1']
wardN1
#-----------------------------------------------------------------

