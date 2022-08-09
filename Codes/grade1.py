# Import pandas
import pandas as pd

# Load the xlsx file
excel_data = pd.read_excel('grade.xlsx')
# Read the values of the file in the dataframe
data = pd.DataFrame(excel_data, columns=['subject', 'credit', 'grade'])
# Print the content
print("The content of the file is:\n", data)
