import matplotlib.pyplot as plt

priority = dataset['Sheet4']

result = priority.groupby('pttype_name')['income'].sum()

ax1 = result.plot.barh(legend=True, color='magenta')
ax1.bar_label(ax1.containers[0], labels = list(result.astype(int)), fontsize = 10)
ax1.legend().texts[0].set_text('รายได้')


plt.ylabel('ประเภทสิทธิ์')
plt.xlabel('จำนวนเงิน (บาท)')
plt.title('รายงานการเบิกใช้สิทธิ์การรักษา')
