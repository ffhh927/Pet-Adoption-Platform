import time

import pymysql
from PyQt5.QtWidgets import (QPushButton)
from PyQt5.QtCore import Qt, QPropertyAnimation, QRect, QEasingCurve
from PyQt5.uic.properties import QtCore, QtWidgets
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt, QPropertyAnimation, QRect, QEasingCurve
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QMainWindow, QApplication, QDesktopWidget
import main
from BubbleTips import BubbleLabel
from Lib.adoptApplicationItem import adoptApplicationItem
from Lib.adopt_admini_over_item import adopt_admini_over_item
from Lib.pet_item import Pet_Item
from Lib.adopt_admini_item import adopt_admini_item

try:
    from PyQt5.QtCore import QSize, QUrl
    from PyQt5.QtGui import QPaintEvent, QPixmap, QColor
    from PyQt5.QtNetwork import QNetworkRequest
    from PyQt5.QtWidgets import QWidget
except ImportError:
    from PySide2.QtCore import QSize, QUrl
    from PySide2.QtGui import QPaintEvent, QPixmap
    from PySide2.QtNetwork import QNetworkRequest
    from PySide2.QtWidgets import QWidget

from start import Ui_StartWindow


class AdoptPage(Ui_StartWindow,QWidget):

    def __init__(self, *args, **kwargs):
        self._manager = kwargs.pop('manager', None)
        super(AdoptPage, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.u_no = ""
        self.e = 1
        self.pushButton_7.clicked.connect(lambda :self.click_adoption_application())
        self.pushButton_8.clicked.connect(lambda: self.click_clean_application())
        self.pushButton.clicked.connect(lambda: self.click_add_pet())
        self.pushButton_2.clicked.connect(lambda: self.click_clean_add())
        self.listWidget_2.itemClicked.connect(self.click_change_page)
        self.listWidget_3.itemClicked.connect(self.click_change_page)
        self.pushButton_4.clicked.connect(lambda: self.click_exit())
        self.pushButton_3.clicked.connect(lambda: self.click_alter_petInfo())
        self.pushButton_6.clicked.connect(lambda: self.click_delete_petInfo())
        self.pushButton_5.clicked.connect(lambda: self.click_jump_petInfo())

        self.conn = pymysql.connect(host='localhost', port=3306, user='root', password="123123",
                                    db="petadoption")
        self.cur = self.conn.cursor()
        sql_pet = "SELECT * FROM petadoption.petinfo;"
        self.cur.execute(sql_pet)
        # 获取查询到的数据，是以字典的形式存储的，所以读取需要使用data[i][j]下标定位
        petInf = self.cur.fetchall()
        # 打印测试
        print(petInf)
        for item_pet in petInf:
            iwidget = Pet_Item(self.scrollAreaWidgetContents_2)
            iwidget.init(str(item_pet[1]), str(item_pet[4]), str(item_pet[2]), str(item_pet[6]),str(item_pet[0]),str(item_pet[3]))
            print(item_pet[3])
            # iwidget.show()
            iwidget.pushButton.setText("前往申请")
            iwidget.pushButton.clicked.connect(lambda: self.click_jump_app(iwidget))
            self.flowLayout.addWidget(iwidget)
            iwidget = Pet_Item(self.scrollAreaWidgetContents)
            iwidget.init( str(item_pet[1]), str(item_pet[4]), str(item_pet[2]), str(item_pet[6]),
                         str(item_pet[0]),str(item_pet[3]))
            iwidget.pushButton.clicked.connect(lambda: self.click_jump_alter(iwidget))
            self.flowLayout_pet_adm.addWidget(iwidget)


        self._blabel = BubbleLabel()


        # flowLayout = flowlayout.FlowLayout()
        # iwidget = Ui_CoverItemWidget.Ui_CoverItemWidget()
        # flowLayout.addWidget(iwidget)
        # flowLayout.addWidget(QPushButton("Short"))
        # flowLayout = flowlayout.FlowLayout(self)
        # iwidget = Ui_CoverItemWidget.Ui_CoverItemWidget()
        # #flowLayout.addWidget(iwidget)
        # flowLayout.addWidget(QPushButton("Short"))
        # # flowLayout.addWidget(QPushButton("Longer"))
        # # flowLayout.addWidget(QPushButton("Different text"))
        # # flowLayout.addWidget(QPushButton("More text"))
        # # flowLayout.addWidget(QPushButton("Even longer button text"))
        # # flowLayout.addWidget(QLabel("test"))
        # self.widget.setLayout(flowLayout)
    def set_uid(self,u_no):
        self.u_no = u_no
        self.u_id = ''
        self.a_id = ''
        self.label_23.setText('USER: '+str(u_no))
        self.conn = pymysql.connect(host='localhost', port=3306, user='root', password="123123",
                                    db="petadoption")
        self.cur = self.conn.cursor()
        if self.stackedWidget_5.currentIndex() == 0:
            # pass
            sql = "select u_id from adopter where u_no = '{}'".format(u_no)
            self.cur.execute(sql)
            self.u_id = str(self.cur.fetchone()[0])
        else:
            # pass
            sql = "select a_id from administrator where u_no = '{}'".format(u_no)
            self.cur.execute(sql)
            self.a_id = str(self.cur.fetchone()[0])
        self.cur.close()
        self.conn.close()



    def click_adoption_application(self):
        self.conn = pymysql.connect(host='localhost', port=3306, user='root', password="123123",
                                    db="petadoption")
        self.cur = self.conn.cursor()
        #姓名
        name = self.lineEdit.text()
        #年龄
        age = self.lineEdit_5.text()
        #性别
        sex = self.comboBox.currentText()
        #家庭住址
        addr = self.lineEdit_8.text()
        #家庭总人数
        f_num = self.spinBox.text()
        #是否同意
        is_agree = self.checkBox.isChecked()
        #联系电话
        phone = self.lineEdit_6.text()
        #邮箱
        email = self.lineEdit_9.text()
        #宠物编号
        pet_id = self.lineEdit_7.text()
        #申请理由
        reason = self.textEdit.toPlainText()

        print(self.u_no+"aaaa")
        sql = "insert into adoptionapplication(u_name, u_sex, u_age, u_city, u_phone, u_email, c_id, u_fnum, is_agree, reason,ap_pet) values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')" \
               .format(name, sex, age, addr,phone,email,self.u_no,f_num,int(is_agree),reason,pet_id)
        self.cur.execute(sql)
        self.conn.commit()
        # 获取查询到的数据，是以字典的形式存储的，所以读取需要使用data[i][j]下标定位
        accountInf = self.cur.fetchall()
        # 打印测试
        print(accountInf)
        self._blabel.setText('申请成功发送')
        self._blabel.show()
        self.conn.close()

    def click_clean_application(self):
        # 姓名
        name = self.lineEdit.clear()
        # 年龄
        age = self.lineEdit_5.clear()
        # 性别
        sex = self.comboBox.setCurrentIndex(0)
        # 家庭住址
        addr = self.lineEdit_8.clear()
        # 家庭总人数
        f_num = self.spinBox.clear()
        # 是否同意
        is_agree = self.checkBox.setChecked(False)
        # 联系电话
        phone = self.lineEdit_6.clear()
        # 邮箱
        email = self.lineEdit_9.clear()
        # 宠物编号
        pet_id = self.lineEdit_7.clear()
        # 申请理由
        reason = self.textEdit.clear()

    def click_add_pet(self):
        self.conn = pymysql.connect(host='localhost', port=3306, user='root', password="123123",
                                    db="petadoption")
        self.cur = self.conn.cursor()
        #名字
        name = self.lineEdit_name.text()
        #种类
        type = self.lineEdit_type.text()
        #品种
        breed = self.lineEdit_breed.text()
        #年龄
        age = self.lineEdit_age.text()
        #公母
        sex = self.comboBox_sex.currentText()
        #i性格
        nature = self.textEdit_2.toPlainText()

        sql_pet ="call add_pet('{}','{}','{}','{}','{}','{}')".format(name,age,sex,nature,breed,type)
        self.cur.execute(sql_pet)
        self.conn.commit()
        self.clear_layout(self.flowLayout_pet_adm)
        sql_pet = "SELECT * FROM petadoption.petinfo;"
        self.cur.execute(sql_pet)
        # 获取查询到的数据，是以字典的形式存储的，所以读取需要使用data[i][j]下标定位
        petInf = self.cur.fetchall()
        # 打印测试
        print(petInf)
        petInf = self.Reverse(petInf)
        print(petInf)
        for item_pet in petInf:
            iwidget = Pet_Item()
            iwidget.init(str(item_pet[1]), str(item_pet[4]), str(item_pet[2]), str(item_pet[6]),
                         str(item_pet[0]),str(item_pet[3]))
            # iwidget.show()
            iwidget.pushButton.clicked.connect(lambda: self.click_jump_alter(iwidget))
            self.flowLayout_pet_adm.addWidget(iwidget)
        self._blabel.setText('添加成功')
        self._blabel.show()


        self.cur.close()
        self.conn.close()

    def Reverse(self,tuples):
        new_tup = ()
        for k in reversed(tuples):
            new_tup = new_tup + (k,)
        return new_tup
    def click_clean_add(self):
        # 名字
        name = self.lineEdit_name.clear()
        # 种类
        type = self.lineEdit_type.clear()
        # 品种
        breed = self.lineEdit_breed.clear()
        # 年龄
        age = self.lineEdit_age.clear()
        # 公母
        sex = self.comboBox_sex.setCurrentIndex(0)
        # i性格
        nature = self.textEdit_2.clear()

    def click_change_page(self,item):
        self.conn = pymysql.connect(host='localhost', port=3306, user='root', password="123123",
                                    db="petadoption")
        self.cur = self.conn.cursor()
        print(self.u_no)
        print(self.listWidget_2.indexFromItem(item).row())

        if self.stackedWidget_5.currentIndex() == 0:
            if self.listWidget_2.indexFromItem(item).row() == 2:
                sql_adopt = "SELECT * FROM petadoption.adoptionapplication where c_id='{}';".format(self.u_no)
                self.cur.execute(sql_adopt)
                # 获取查询到的数据，是以字典的形式存储的，所以读取需要使用data[i][j]下标定位
                adoptInf = self.cur.fetchall()
                # 打印测试
                print("申请信息")
                print(adoptInf)
                print(".")
                self.clear_layout(self.flowLayout_adopt)

                for item_adopt in adoptInf:
                    if item_adopt[13] =='Y':
                        adoptinf = adopt_admini_over_item()
                        adoptinf.init(item_adopt[0], item_adopt[1], item_adopt[2], item_adopt[3], item_adopt[10],
                                      item_adopt[11],
                                      item_adopt[4], item_adopt[5], item_adopt[17], item_adopt[12], item_adopt[6], item_adopt[13],
                                      item_adopt[15])
                        self.flowLayout_adopt.addWidget(adoptinf)
                    else:
                        adoptinf = adoptApplicationItem()
                        adoptinf.init(item_adopt[0], item_adopt[1], item_adopt[2], item_adopt[3], item_adopt[10], item_adopt[11],
                                      item_adopt[4], item_adopt[5], item_adopt[17], item_adopt[12],item_adopt[6],item_adopt[13],item_adopt[15])
                        self.flowLayout_adopt.addWidget(adoptinf)
            elif self.listWidget_2.indexFromItem(item).row() == 0:
                sql_pet = "SELECT * FROM petadoption.petinfo;"
                self.cur.execute(sql_pet)
                # 获取查询到的数据，是以字典的形式存储的，所以读取需要使用data[i][j]下标定位
                petInf = self.cur.fetchall()
                # 打印测试
                print(petInf)
                self.clear_layout(self.flowLayout)
                for item_pet in petInf:
                    iwidget = Pet_Item(self.scrollAreaWidgetContents_2)
                    iwidget.init( str(item_pet[1]), str(item_pet[4]), str(item_pet[2]), str(item_pet[6]),
                                 str(item_pet[0]),str(item_pet[3]))
                    iwidget.pushButton.setText("前往申请")
                    iwidget.pushButton.clicked.connect(lambda: self.click_jump_app(iwidget))
                    # iwidget.show()

                    self.flowLayout.addWidget(iwidget)


        else:
            print(self.listWidget_3.indexFromItem(item).row())
            if self.listWidget_3.indexFromItem(item).row() == 1 or self.listWidget_3.indexFromItem(item).row() == 2:
                sql_adopt = "SELECT * FROM petadoption.adoptionapplication;"
                self.cur.execute(sql_adopt)
                # 获取查询到的数据，是以字典的形式存储的，所以读取需要使用data[i][j]下标定位
                adoptInf = self.cur.fetchall()
                # 打印测试
                print("申请信息")
                print(adoptInf)
                print(".")
                self.clear_layout(self.flowLayout_app_adm)
                self.clear_layout(self.flowLayout_app_adm_over)
                for item_adopt in adoptInf:
                    adoptinf = adopt_admini_item()
                    adoptinf.init(item_adopt[0], item_adopt[1], item_adopt[2], item_adopt[3], item_adopt[10], item_adopt[11], item_adopt[4], item_adopt[5], item_adopt[17], item_adopt[12], item_adopt[6], self.a_id)
                    if item_adopt[13] != 'Y':
                        self.flowLayout_app_adm.addWidget(adoptinf)
                    else:
                        adoptinf = adopt_admini_over_item()
                        adoptinf.init(item_adopt[0], item_adopt[1], item_adopt[2], item_adopt[3], item_adopt[10],
                                      item_adopt[11],
                                      item_adopt[4], item_adopt[5], item_adopt[17], item_adopt[12], item_adopt[6], item_adopt[13],
                                      item_adopt[15])
                        self.flowLayout_app_adm_over.addWidget(adoptinf)
            elif self.listWidget_3.indexFromItem(item).row() == 0:
                sql_pet = "SELECT * FROM petadoption.petinfo;"
                self.cur.execute(sql_pet)
                # 获取查询到的数据，是以字典的形式存储的，所以读取需要使用data[i][j]下标定位
                petInf = self.cur.fetchall()
                # 打印测试
                print(petInf)
                self.clear_layout(self.flowLayout_pet_adm)
                for item_pet in petInf:
                    iwidget = Pet_Item(self.scrollAreaWidgetContents)
                    iwidget.init( str(item_pet[1]), str(item_pet[4]), str(item_pet[2]), str(item_pet[6]),
                                 str(item_pet[0]),str(item_pet[3]))
                    # iwidget.show()

                    iwidget.pushButton.clicked.connect(lambda: self.click_jump_alter(iwidget))
                    self.flowLayout_pet_adm.addWidget(iwidget)

        # elif self.listWidget_2.currentIndex()==0:
        #     self.flowLayout.c

        self.cur.close()
        self.conn.close()

    def clear_layout(self, layout):
        item_list = list(range(layout.count()))
        item_list.reverse()  # 倒序删除，避免影响布局顺序

        for i in item_list:
            item = layout.itemAt(i)
            layout.removeItem(item)
            if item.widget():
                item.widget().deleteLater()

    def click_exit(self):
        self.close()
        myWin = main.MyMainForm()
        myWin.animation_start()

    def keyPressEvent(self, QKeyEvent):
        """快捷键"""
        if QKeyEvent.key() == Qt.Key_Escape:  # esc
            if self.e == 1:
                self.animation_exit()
            elif self.e == 0:
                self.animation_start()

    def animation_start(self):
        self.e = 1
        self.show()
        self.anim = QPropertyAnimation(self, b'geometry')  # 动画类型
        # self.anim.setStartValue(QRect(QDesktopWidget().screenGeometry().width() / 2 - 230, QDesktopWidget().screenGeometry().height() / 2 - 338, 461, 676))
        # self.anim.setEndValue(QRect(0, 0, QDesktopWidget().screenGeometry().width(), QDesktopWidget().screenGeometry().height()))
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
            super(AdoptPage, self).mousePressEvent(event)
            self.start_x = event.x()
            self.start_y = event.y()

    def mouseReleaseEvent(self, event):
        self.start_x = None
        self.start_y = None

    def mouseMoveEvent(self, event):
        try:
            super(AdoptPage, self).mouseMoveEvent(event)
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

    def click_jump_app(self,item):
        self.stackedWidget.setCurrentIndex(1)
        self.lineEdit_7.setText(str(item.pet_id))

    def click_jump_alter(self,item):
        self.stackedWidget.setCurrentIndex(6)
        self.lineEdit_breed_3.setText(str(item.pet_id))
        self.lineEdit_name_2.setText(str(item.pet_name))
        self.lineEdit_breed_2.setText(str(item.pet_breed))
        self.lineEdit_age_2.setText(str(item.pet_age))
        self.comboBox_sex_2.setCurrentText(str(item.pet_sex))
        self.textEdit_3.setText(str(item.pet_nature))

    def click_alter_petInfo(self):
        self.conn = pymysql.connect(host='localhost', port=3306, user='root', password="123123",
                                    db="petadoption")
        self.cur = self.conn.cursor()
        p_id = self.lineEdit_breed_3.text()
        #名字
        name = self.lineEdit_name_2.text()
        #种类
        type = self.lineEdit_type_2.text()
        #品种
        breed = self.lineEdit_breed_2.text()
        #年龄
        age = self.lineEdit_age_2.text()
        #公母
        sex = self.comboBox_sex_2.currentText()
        #i性格
        nature = self.textEdit_3.toPlainText()

        sql_pet ="call alter_pet('{}','{}','{}','{}','{}','{}','{}')".format(p_id,name,age,sex,nature,breed,type)
        self.cur.execute(sql_pet)
        self.conn.commit()
        self.clear_layout(self.flowLayout_pet_adm)
        sql_pet = "SELECT * FROM petadoption.petinfo;"
        self.cur.execute(sql_pet)
        # 获取查询到的数据，是以字典的形式存储的，所以读取需要使用data[i][j]下标定位
        petInf = self.cur.fetchall()
        # 打印测试
        print(petInf)
        petInf = self.Reverse(petInf)
        print(petInf)
        for item_pet in petInf:
            iwidget = Pet_Item()
            iwidget.init(str(item_pet[1]), str(item_pet[4]), str(item_pet[2]), str(item_pet[6]),
                         str(item_pet[0]),str(item_pet[3]))
            # iwidget.show()
            iwidget.pushButton.clicked.connect(lambda: self.click_jump_alter(iwidget))
            self.flowLayout_pet_adm.addWidget(iwidget)
        self._blabel.setText('修改成功')
        self._blabel.show()


        self.cur.close()
        self.conn.close()


    def click_delete_petInfo(self):
        self.conn = pymysql.connect(host='localhost', port=3306, user='root', password="123123",
                                    db="petadoption")
        self.cur = self.conn.cursor()
        p_id = self.lineEdit_breed_3.text()

        sql_pet ="delete from pet where p_id='{}'".format(p_id)
        self.cur.execute(sql_pet)
        self.conn.commit()
        self.clear_layout(self.flowLayout_pet_adm)
        sql_pet = "SELECT * FROM petadoption.petinfo;"
        self.cur.execute(sql_pet)
        # 获取查询到的数据，是以字典的形式存储的，所以读取需要使用data[i][j]下标定位
        petInf = self.cur.fetchall()
        # 打印测试
        print(petInf)
        petInf = self.Reverse(petInf)
        print(petInf)
        for item_pet in petInf:
            iwidget = Pet_Item()
            iwidget.init(str(item_pet[1]), str(item_pet[4]), str(item_pet[2]), str(item_pet[6]),
                         str(item_pet[0]),str(item_pet[3]))

            # iwidget.show()
            iwidget.pushButton.clicked.connect(lambda: self.click_jump_alter(iwidget))
            self.flowLayout_pet_adm.addWidget(iwidget)
        self._blabel.setText('删除成功')
        self._blabel.show()
        self.cur.close()
        self.conn.close()

    def click_jump_petInfo(self):
         self.stackedWidget.setCurrentIndex(3)
