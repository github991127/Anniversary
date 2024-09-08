# 读取Devotion.xls，返回list_Anniversary列表
from datetime import date
from numpy import stack
from xlrd import open_workbook, xldate

file_path = 'Devotion.xls'
data = open_workbook(file_path)
table = data.sheet_by_name('Sheet1')
excel_date = table.col_values(0)[1:]
data = []
for i in excel_date:  # 将excel的int日期转换为data格式
    dt = xldate.xldate_as_datetime(i, 0)
    data.append(dt.date())
festival = table.col_values(1)[1:]
memory = table.col_values(2)[1:]

list_Anniversary = stack((data, festival, memory), 1)
# print(list_Anniversary)
