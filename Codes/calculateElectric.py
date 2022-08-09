# Import pandas
import pandas as pd

# Load the xlsx file
excel_data = pd.read_excel('rateElectric.xlsx')
# Read the values of the file in the dataframe
data = pd.DataFrame(excel_data, columns=['หน่วยที่ใช้', 'ราคาต่อหน่วย'])

print(data.head())

useUnit = 30
totalPrice = 0
nextRate = 1
while (useUnit > data['หน่วยที่ใช้'][nextRate] ):
  #print(data['หน่วยที่ใช้'][nextRate])
  totalPrice = totalPrice +( (data['หน่วยที่ใช้'][nextRate]-data['หน่วยที่ใช้'][nextRate-1]) * data['ราคาต่อหน่วย'][nextRate-1])
  nextRate = nextRate + 1

if (useUnit <= data['หน่วยที่ใช้'][nextRate]):
  totalPrice = totalPrice + ( ( useUnit - data['หน่วยที่ใช้'][nextRate-1] + 1) * data['ราคาต่อหน่วย'][nextRate-1])

#81.3165
print(totalPrice)
