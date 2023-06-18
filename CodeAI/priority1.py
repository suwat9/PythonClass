priority = dataset['Sheet4']

name = priority['pttype_name'].unique()

priority.groupby('pttype_name')['income'].sum()
