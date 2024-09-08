from PySide2.QtWidgets import QApplication, QWidget
from PySide2.QtUiTools import QUiLoader
from PySide2.QtGui import QIcon
from datetime import date

from list_themes import *
import Daycheck
import Getdate


class Stats:
    def __init__(self):
        # 从ui文件中加载UI定义,从UI定义中动态创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了.比如 self.ui.button , self.ui.textEdit
        self.ui = QUiLoader().load('Anniversary.ui')
        self.ui.pushButton.clicked.connect(self.handleCalc)
        self.ui.textEdit.returnPressed.connect(self.handleCalc)  # 单行文本框回车消息

    def handleCalc(self):  # ENTER按钮，将输入内容通过Getdate转换为data类，传给Daycheck计算
        self.ui.textBrowser.clear()
        input_text = self.ui.textEdit.text()

        x = Getdate.getdate(input_text)
        self.ui.textBrowser.append(Daycheck.CheckFrist(x))
        if x >= date(2023, 2, 25):
            Ann_y, list_y, Ann_m, list_m, Ann_d, list_d = Daycheck.CheckYMD(x)
            self.ui.textBrowser.append(None)
            # 判断是否三列表为空，质数日
            if list_y == list_m == list_d == []:
                self.ui.textBrowser.append('💖质数纪念日\n{0}年{1}月{2}日这一天竟然像质数一样巧妙避开了所有节日因子，快去庆祝一下吧！'
                                           .format(x.year, x.month, x.day))
            # 按年月日顺序，日期由新到旧顺序输出纪念日
            else:
                for a, b in zip(Ann_y, list_y):
                    self.ui.textBrowser.append('💖{1} {0}周年纪念日\n{2}年{3}月{4}日这一天，{5}'
                                               .format(b, a[1], a[0].year, a[0].month, a[0].day, a[2]))
                    self.ui.textBrowser.append(None)

                for a, b in zip(Ann_m, list_m):
                    self.ui.textBrowser.append('💖{1} {0}个月纪念日\n{2}年{3}月{4}日这一天，{5}'
                                               .format(b, a[1], a[0].year, a[0].month, a[0].day, a[2]))
                    self.ui.textBrowser.append(None)

                for a, b in zip(Ann_d, list_d):
                    self.ui.textBrowser.append('💖{1} {0}天纪念日\n{2}年{3}月{4}日这一天，{5}'
                                               .format(b, a[1], a[0].year, a[0].month, a[0].day, a[2]))
                    self.ui.textBrowser.append(None)


if __name__ == '__main__':
    app = QApplication([])
    app.setWindowIcon(QIcon('image.png'))
    apply_stylesheet(app, theme[28], extra=extra, invert_secondary=True)  # 默认dark-False
    w = QWidget()
    w.setWindowIcon(QIcon('image.png'))
    stats = Stats()
    stats.ui.show()
    app.exec_()
