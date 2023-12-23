import sys

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt, QPropertyAnimation, QRect, QEasingCurve
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QMainWindow, QApplication, QDesktopWidget
import pymysql

import adoptPage
from login_widget import Ui_MainWindow
from register import Ui_RegisterWindow
from Lib.pet_item import Pet_Item
from BubbleTips import BubbleLabel
class MyMainForm(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.start_x = None
        self.start_y = None
        self.anim=None
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowFlags(Qt.FramelessWindowHint)  # 设置窗口标志：隐藏窗口边框
        self.lineEdit.setAttribute(QtCore.Qt.WA_MacShowFocusRect, 0)
        self.lineEdit_2.setAttribute(QtCore.Qt.WA_MacShowFocusRect, 0)
        self.resize(652,312)  # 主窗大小
        self.e = 1
        # 按ESC键开关
        self.pushButton_3.clicked.connect(lambda :self.open_register_page())
        self.pushButton_2.clicked.connect(lambda :self.login())
        self._blabel = BubbleLabel()
        self.conn = pymysql.connect(host='localhost', port=3306, user='root', password="123123", db="petadoption")
        self.cur = self.conn.cursor()
        #注册页面
        self.register = Ui_RegisterWindow()  # 初始化ci_one.py的窗口设置
        self.register.setupUi(self.register)

    def keyPressEvent(self, QKeyEvent):
        """快捷键"""
        if QKeyEvent.key() == Qt.Key_Escape:  # esc
            if self.e == 1:
                self.animation_exit()
                self.cur.close()
                self.conn.close()
            elif self.e == 0:
                self.animation_start()
                self.conn = pymysql.connect(host='localhost', port=3306, user='root', password="123123",
                                            db="petadoption")
                self.cur = self.conn.cursor()

    def animation_start(self):
        self.e = 1
        self.show()
        self.anim = QPropertyAnimation(self, b'geometry')  # 动画类型
        #self.anim.setStartValue(QRect(QDesktopWidget().screenGeometry().width() / 2 - 230, QDesktopWidget().screenGeometry().height() / 2 - 338, 461, 676))
        #self.anim.setEndValue(QRect(0, 0, QDesktopWidget().screenGeometry().width(), QDesktopWidget().screenGeometry().height()))
        self.anim.setDuration(400)
        self.anim.setEasingCurve(QEasingCurve.OutBounce)
        main_opacity = QPropertyAnimation(self, b"windowOpacity", self)
        main_opacity.setStartValue(0)
        main_opacity.setEndValue(1)
        main_opacity.setDuration(400)
        main_opacity.start()

        # self.anim.setLoopCount(-1)  # 设置循环旋转
        self.anim.start()

    def animation_exit(self):
        self.e = 0
        self.anim = QPropertyAnimation(self, b'geometry')  # 动画类型
        self.anim.setStartValue(QRect(0, 0, self.width(), self.height()))
#        self.anim.setEndValue(QRect(QDesktopWidget().screenGeometry().width() / 2 - 230, QDesktopWidget().screenGeometry().height() / 2 - 338, 461,676))
        self.anim.setDuration(400)
        self.anim.setEasingCurve(QEasingCurve.OutBounce)
        main_opacity = QPropertyAnimation(self, b"windowOpacity", self)
        main_opacity.setStartValue(1)
        main_opacity.setEndValue(0)
        main_opacity.setDuration(400)
        main_opacity.start()

        # self.anim.setLoopCount(-1)  # 设置循环旋转
        self.anim.start()

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            super(MyMainForm, self).mousePressEvent(event)
            self.start_x = event.x()
            self.start_y = event.y()

    def mouseReleaseEvent(self, event):
        self.start_x = None
        self.start_y = None

    def mouseMoveEvent(self, event):
        try:
            super(MyMainForm, self).mouseMoveEvent(event)
            dis_x = event.x() - self.start_x
            dis_y = event.y() - self.start_y
            self.move(self.x() + dis_x, self.y() + dis_y)
        except:
            pass

    def effect_shadow_style(self, widget):
        effect_shadow = QtWidgets.QGraphicsDropShadowEffect(self)
        effect_shadow.setOffset(12, 12)  # 偏移
        effect_shadow.setBlurRadius(128)  # 阴影半径
        effect_shadow.setColor(QColor(155, 230, 237, 150))  # 阴影颜色
        widget.setGraphicsEffect(effect_shadow)

    def open_register_page(self):
        self.close()
        self.register.label.setText("账号注册")
        self.register.pushButton_2.setText("注册")
        self.register.animation_start()  # 显示该窗口

    def login(self):
        # 执行sql语句和实现事件、、、
        # 查询的sql语句
        self.u_no = self.lineEdit.text()
        u_password = self.lineEdit_2.text()
        sql = "SELECT * FROM account WHERE account.u_no='" + self.u_no + "';"
        self.cur.execute(sql)
        # 获取查询到的数据，是以字典的形式存储的，所以读取需要使用data[i][j]下标定位
        accountInf = self.cur.fetchall()
        # 打印测试
        print(accountInf)
        if self.u_no =='':
            msg = "请填写账号"
        elif u_password == '':
            msg = "请填写密码"
        elif len(accountInf) == 0:
            msg = "账号不存在"
        elif accountInf[0][2] != u_password:
            msg = "账号或密码错误"
        elif self.checkBox.isChecked():
            if accountInf[0][1] != 'A':
                self.close()
                #self.start = Ui_StartWindow()
                self.start = adoptPage.AdoptPage()
                self.start.stackedWidget_5.setCurrentIndex(1)
                self.start.stackedWidget.setCurrentIndex(3)
                self.start.set_uid(self.u_no)
                #self.start.setupUi(self.start)

                self.start.show()
                return
            else:
                msg = "您不是管理员"
        else:
            self.close()
            self.start = adoptPage.AdoptPage()
            self.start.stackedWidget_5.setCurrentIndex(0)
            self.start.stackedWidget.setCurrentIndex(0)
            self.start.set_uid(self.u_no)
            #self.start.setupUi(self.start)

            self.start.show()
            return
        print(msg)
        self._blabel.setText(msg)
        self._blabel.show()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainForm()
    myWin.animation_start()
    sys.exit(app.exec_())
