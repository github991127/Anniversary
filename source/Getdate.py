# 将日期str转换为date类
from datetime import datetime, date


def getdate(input_text=''):
    if '-' in input_text:
        dt_object = datetime.strptime(input_text, '%Y-%m-%d').date()
    elif '月' in input_text:
        dt_object = datetime.strptime(input_text, '%Y年%m月%d日').date()
    elif len(input_text) == 8:
        year = int(input_text[0:4])
        month = int(input_text[4:6])
        day = int(input_text[6:8])
        dt_object = date(year, month, day)
    elif len(input_text) == 4:
        year = date.today().year
        month = int(input_text[0:2])
        day = int(input_text[2:4])
        dt_object = date(year, month, day)
    elif len(input_text) == 3:
        year = date.today().year
        month = int(input_text[0:1])
        day = int(input_text[1:3])
        dt_object = date(year, month, day)
    elif len(input_text) == 0:
        dt_object = date.today()
        # dt_object = date(2023, 5, 20)
    else:
        dt_object = date(1582, 10, 4)  # 儒略历最后一天，格里高里历下一日改为10月15日
    return dt_object


if __name__ == "__main__":
    x = getdate()
    print(x)
