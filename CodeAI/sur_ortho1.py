import matplotlib.pyplot  as plt
ward848587 = df[df['code'].isin([84,85,87])]

rows = 2
cols = 1

plt.figure(figsize=(5,3))
axs = plt.subplot(rows,cols, 1)

barvalue = axs.barh(ward848587['code'],ward848587['admit'],color='orange')
axs.set_yticks(ward848587['code'])
axs.set_yticklabels(['ศัลยกรรมชาย','ศัลยกรรมหญิง','หอผู้ป่วยหนักศัลยกรรม'])
axs.bar_label(barvalue)
plt.title('ข้อมูลเตียงตึกศัลยกรรม')
plt.xlabel('จำนวนเตียง')

ward6263 = df[df['code'].isin([62,63])]
plt.figure(figsize=(5,3))
axs2 = plt.subplot(rows,cols, 2)

barvalue2 = axs2.barh(ward6263['code'],ward6263['admit'],color='b')
axs2.set_yticks(ward6263['code'])
axs2.set_yticklabels(['ศัลยกรรมกระดูกชาย','ศัลยกรรมกระดูกหญิง'])
axs2.bar_label(barvalue2)
plt.title('ข้อมูลเตียงตึกออร์โธปิดิกส์')
plt.xlabel('จำนวนเตียง')
