import matplotlib.pyplot  as plt
ward848587 = df[df['code'].isin([84,85,87])]

plt.figure(figsize=(5,3))
axs = plt.axes()

barvalue = axs.barh(ward848587['code'],ward848587['admit'],color='orange')
axs.set_yticks(ward848587['code'])
axs.set_yticklabels(['ศัลยกรรมชาย','ศัลยกรรมหญิง','หอผู้ป่วยหนักศัลยกรรม'])
axs.bar_label(barvalue)
plt.title('ข้อมูลเตียงตึกศัลยกรรม')
