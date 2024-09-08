# coding:utf-8
# 输入日期，返回纪念日列表
from itertools import chain
from numpy import array
from Devotion import *


def dict_Anniversary():
    dict_commemoration = {1, 214, 314, 404, 520, 521, 1024, 1225, 1231}  # 特殊序号
    dict_centi = {}  # 整百
    dict_homo = {}  # 两位数以上，所有数字相同
    dict_step = {}  # 三位数以上，所有数字递增1或递减1
    dict_binary = {}  # 三位数以上，所有数字为01
    dict_palindrome = {}  # 三位数以上，回文数

    for i in range(100, 100001, 100):
        dict_centi[i] = None
    # print(dict_centi)

    for i in range(10, 100001):
        if len(set(str(i))) == 1:
            dict_homo[i] = None
    # print(dict_homo)

    for i in range(100, 100001):
        str_i = str(i)
        if all(int(str_i[j]) - int(str_i[j - 1]) == 1 for j in range(1, len(str_i))) or all(
                int(str_i[j]) - int(str_i[j - 1]) == -1 for j in range(1, len(str_i))):
            dict_step[i] = None
    # print(dict_step)

    for i in range(100, 100001):
        str_i = str(i)
        if all(c in "01" for c in str_i):
            dict_binary[i] = None
    # print(dict_binary)

    for i in range(100, 100001):
        str_i = str(i)
        if str_i == str_i[::-1]:
            dict_palindrome[i] = None
    # print(dict_palindrome)
    dict_all = dict.fromkeys(chain(dict_commemoration, dict_centi, dict_homo, dict_step, dict_binary, dict_palindrome))
    dict_all = dict(sorted(dict_all.items()))
    return dict_all


# 返回符合条件的日期列表，返回相隔年数列表
def CheckYear(x, Anniversary, Ann_column0):
    Ann_y = []
    list_y = []
    count = 0
    for i in Ann_column0:
        if x.year != i.year and x.month == i.month and x.day == i.day:
            Ann_y.append(Anniversary[count])
            list_y.append(x.year - i.year)
        count += 1
    return Ann_y, list_y


# 返回符合条件的日期列表，返回相隔月数列表
def CheckMonth(x, Anniversary, Ann_column0, dict_all):
    Ann_m = []
    list_m = []
    count = 0
    for i in Ann_column0:
        if x.day == i.day:
            delta_m = (x.year - i.year) * 12 + (x.month - i.month)
            if delta_m in dict_all:
                Ann_m.append(Anniversary[count])
                list_m.append(delta_m)
        count += 1
    return Ann_m, list_m


# 返回符合条件的日期列表，返回相隔日数列表
def CheckDay(x, Anniversary, Ann_column0, dict_all):
    Ann_d = []
    list_d = []
    count = 0
    for i in Ann_column0:
        delta_d = (x - i).days
        if delta_d in dict_all:
            Ann_d.append(Anniversary[count])
            list_d.append(delta_d)
        count += 1
    return Ann_d, list_d


# 判断是否为不存在10日：小科普
# 判断是否为错误日期（是则返回1582-10-4）：小笨蛋
# 判断是否属于生日前/中/后：对应语句
# 判断是否在相识日后：执行后续checkyear
def CheckFrist(x):
    if x == date(1582, 10, 4):
        str = ('小笨蛋输错了哦！')

    elif x > date(1582, 10, 4) and x < date(1582, 10, 15):
        str = (
            '这一天是不存在的哦！\n小科普：我们现在所使用的公历，是意大利医生兼哲学家Aloysius Lilius对儒略历加以改革而制成的一种历法——格里历。1582年，时任罗马教皇的格列高利十三世予以批准颁行，但是当年从儒略历更换为格里历时，儒略历的春分日（3月21日）与地球公转到春分点的实际时间已相差10天。因此，格里历开始实行时，将儒略历1582年10月4日星期四的次日，为格里历1582年10月15日星期五，即有10天被删除，但原星期的周期保持不变。')

    # elif x < date(1999, 11, 27):
    #     str = ('{0}年{1}月{2}日这一天的你们灵魂还未降生于世界呢，不过前世的你们或许这天擦肩而过哦！'
    #            .format(x.year, x.month, x.day))
    #
    # elif x < date(2023, 2, 25):
    #     str = ('{0}年{1}月{2}日这一天的你们还是两个孤独的灵魂呢，不过命运的引力正在吸引你们靠近哦！'
    #            .format(x.year, x.month, x.day))
    else:
        str = ('{0}年{1}月{2}日是'
               .format(x.year, x.month, x.day))
    return str


# 获取纪念日列表，遍历检查与输入日期的差值是否符合dict_all
def CheckYMD(x):
    Anniversary = array(list_Anniversary)
    Ann_column0 = Anniversary[..., 0]
    dict_all = dict_Anniversary()
    Ann_y, list_y = CheckYear(x, Anniversary, Ann_column0)
    Ann_m, list_m = CheckMonth(x, Anniversary, Ann_column0, dict_all)
    Ann_d, list_d = CheckDay(x, Anniversary, Ann_column0, dict_all)
    return Ann_y, list_y, Ann_m, list_m, Ann_d, list_d


if __name__ == "__main__":

    x = date.today()
    # x = date(1999, 11, 27)
    # x = date(1582, 10, 5)
    print(CheckFrist(x))
    if x >= date(2023, 2, 25):
        Ann_y, list_y, Ann_m, list_m, Ann_d, list_d = CheckYMD(x)
        # 判断是否三列表为空，质数日
        if list_y == list_m == list_d == []:
            print('💖质数纪念日\n{0}年{1}月{2}日这一天竟然像质数一样巧妙避开了所有节日因子，快去庆祝一下吧！'
                  .format(x.year, x.month, x.day))
        # 按年月日顺序，日期由新到旧顺序输出纪念日
        else:
            for a, b in zip(Ann_y, list_y):
                print('💖{1}{0}周年纪念日\n{2}年{3}月{4}日这一天，{5}'
                      .format(b, a[1], a[0].year, a[0].month, a[0].day, a[2]))
                # print(a, b)

            for a, b in zip(Ann_m, list_m):
                print('💖{1}{0}个月纪念日\n{2}年{3}月{4}日这一天，{5}'
                      .format(b, a[1], a[0].year, a[0].month, a[0].day, a[2]))

            for a, b in zip(Ann_d, list_d):
                print('💖{1}{0}天纪念日\n{2}年{3}月{4}日这一天，{5}'
                      .format(b, a[1], a[0].year, a[0].month, a[0].day, a[2]))
# 测试用例
# 0
# 1582-10-4
# 1582-10-5
# 1999-1-1
# 1999-11-27
# 1999-12-1
# 2023-2-25
# 0226
# 20240311
