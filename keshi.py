# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '科室UI.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QStringListModel, QObject
q=[]
Sum=1
class Ui_Dialog(QObject):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(627, 561)
        self.listView = QtWidgets.QListView(Dialog)
        self.listView.setGeometry(QtCore.QRect(350, 130, 211, 361))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.listView.setFont(font)
        self.listView.setObjectName("listView")
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(50, 130, 241, 361))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(16)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_2.addWidget(self.lineEdit)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.gridLayout.setHorizontalSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(16)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 2, 0, 1, 1)
        self.pushButton_19 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(16)
        self.pushButton_19.setFont(font)
        self.pushButton_19.setObjectName("pushButton_19")
        self.gridLayout.addWidget(self.pushButton_19, 0, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(16)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 1, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(170, 16, 261, 81))
        font = QtGui.QFont()
        font.setFamily("禹卫书法云墨简体")
        font.setPointSize(39)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(300, 130, 20, 361))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")

        self.retranslateUi(Dialog)
        self.pushButton_3.clicked['bool'].connect(Dialog.accept)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "就诊科室@laolao"))
        self.label_2.setText(_translate("Dialog", "输入病历号"))
        self.pushButton_3.setText(_translate("Dialog", "退出"))
        self.pushButton_19.setText(_translate("Dialog", "排队"))
        self.pushButton_2.setText(_translate("Dialog", "就诊"))
        self.label.setText(_translate("Dialog", "当前科室"))

        # self.get_this_queue(self.label.text())
        self.set_Signals_and_slots()
        self.my_style()

    def my_style(self):
        stye_set='''
        QPushButton{color:white}
        QPushButton{background-color:#5c6646}
        QPushButton{border:2px}
        QPushButton{border-radius:10px}
        QPushButton{padding:2px 4px}
        QPushButton:hover{color:#ffaa00}
        '''
        self.pushButton_3.setStyleSheet(stye_set)
        self.pushButton_2.setStyleSheet(stye_set)
        self.pushButton_19.setStyleSheet(stye_set)
        stye_set2='''
        QLineEdit{border-radius:10px}
        QLineEdit{padding:2px 4px}
        QLineEdit{background-color:rgb(180, 180, 180)}
        '''
        self.lineEdit.setStyleSheet(stye_set2)
        stye_set3='''
        QListView{background-color:rgb(180, 180, 180)}
        QListView{border-radius:10px}
        QListView{padding:2px 4px}
        '''
        self.listView.setStyleSheet(stye_set3)

    def set_Signals_and_slots(self):

        self.pushButton_19.clicked.connect(lambda :self.line_up(self.lineEdit.text())) #排队
        self.pushButton_2.clicked.connect(self.line_out)

    def see_people(self):
        global q
        list_model = QStringListModel()
        nq=[]
        index=1
        for i in q:
            nq.append("第{}号：{}".format(index,i))
            index+=1
        list_model.setStringList(nq)
        self.listView.setModel(list_model)


    def change_title(self,name):
        self.label.setText(name)

    def line_up(self,Username):
        global q
        global Sum
        q.append(self.label.text()+"-"+Username)
        Sum=Sum+1
        self.lineEdit.clear()
        self.see_people()

    def line_out(self):
        global q
        global Sum
        Sum=Sum-1
        if len(q)!=0:
            q.pop(0)
        self.see_people()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QDialog()
    ui = Ui_Dialog()
    # 向主窗口添加控件
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
