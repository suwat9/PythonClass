# Import pandas
import pandas as pd

# Load the xlsx file
excel_data = pd.read_excel('grade.xlsx')
# Read the values of the file in the dataframe
data = pd.DataFrame(excel_data, columns=['subject', 'credit', 'grade'])
# Print the content
#print("The content of the file is:\n", data.subject[0],data.credit[0],data.grade[0])

gradeAverage = 0
creditSum = 0

for i in range(0,3):
  gradeAverage = gradeAverage + (data.credit[i]*data.grade[i])
  creditSum = creditSum + data.credit[i]

print('เกรดเฉลี่ย : '+str(gradeAverage / creditSum))
