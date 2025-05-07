import pandas

data_excel = ''
data_sheet = '' 


data_frames = pandas.read_excel(data_excel, engine='openpyxl', sheet_name=data_sheet, header=None)

data_frames.to_csv('./KOCAK4.csv', sep='|', header=False, index=False)

