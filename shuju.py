'''
@Time : 2020/9/15 3:06
@Author : laolao
@FileName: 数据.py
'''
import datetime
import sys
import time

from PyQt5.QtWidgets import *

from keshi import *


class Collect(QMainWindow):
    def __init__(self, ):
        super(QMainWindow, self).__init__()
        self.number = 0
        self.setWindowTitle("停止排队@laolao")

        w = QWidget()
        self.setCentralWidget(w)

        self.topFiller = QWidget()
        self.topFiller.setMinimumSize(250, 2000)

        self.set_iteam()
        # 创建一个滚动条
        self.scroll = QScrollArea()
        self.scroll.setWidget(self.topFiller)

        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.scroll)
        w.setLayout(self.vbox)
        self.setStyleSheet("color:rgb(255,255,255)")
        self.statusBar().showMessage("今天时间：{}".format(datetime.datetime.now().date()))
        self.resize(300, 500)

    def set_iteam(self):
        print(q)
        tag=1
        for i in q:
            self.lable = QLabel(self.topFiller)
            self.lable.setText(i)
            self.lable.move(10, tag * 20)
            tag+=1


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainwindow = Collect()
    mainwindow.show()
    sys.exit(app.exec_())