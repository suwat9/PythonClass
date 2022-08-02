import docx2txt

# extract text
text = docx2txt.process("/content/suwat-รายชื่อนักศึกษา65.docx")

print(text)
print(text.split(','))
