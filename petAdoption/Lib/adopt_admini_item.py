import pymysql

from Lib.adopt_admini_widget import Ui_Form
try:
    from PyQt5.QtCore import QPoint, QRect, QSize, Qt
    from PyQt5.QtWidgets import (QApplication, QLayout, QPushButton,
                                 QSizePolicy, QWidget)
except ImportError:
    from PySide2.QtCore import QPoint, QRect, QSize, Qt
    from PySide2.QtWidgets import (QApplication, QLayout, QPushButton,
                                   QSizePolicy, QWidget)
class adopt_admini_item(QWidget, Ui_Form):

    def __init__(self, *args):
        super(adopt_admini_item, self).__init__(*args)
        self.setupUi(self)
        self.pushButton.clicked.connect(lambda : self.click_agree())
        self.pushButton_2.clicked.connect(lambda : self.click_refuse())

    def init(self, name, sex, age, addr, f_mun,is_adopted,phone,email,p_id,reason,ap_id,a_id):
        self.ap_id = ap_id
        self.a_id = a_id
        self.label_12.setText(
            "<html><head/><body><p><span style=\" color:#222222;\">" + str(name) + "</span></p></body></html>")
        self.label_13.setText(
            "<html><head/><body><p><span style=\" color:#222222;\">" + str(sex) + "</span></p></body></html>")
        self.label_14.setText(
            "<html><head/><body><p><span style=\" color:#222222;\">" + str(age) + "</span></p></body></html>")
        self.label_10.setText(
            "<html><head/><body><p><span style=\" color:#222222;\">" + str(f_mun) + "</span></p></body></html>")
        self.label_11.setText(
            "<html><head/><body><p><span style=\" color:#222222;\">" + str(addr) + "</span></p></body></html>")
        self.checkBox.setChecked(bool(is_adopted))
        self.checkBox.setEnabled(False)
        self.label_15.setText(
            "<html><head/><body><p><span style=\" color:#222222;\">" + str(phone) + "</span></p></body></html>")
        self.label_16.setText(
            "<html><head/><body><p><span style=\" color:#222222;\">" + str(email) + "</span></p></body></html>")
        self.label_17.setText(
            "<html><head/><body><p><span style=\" color:#222222;\">" + str(p_id) + "</span></p></body></html>")
        self.label_18.setText(
            "<html><head/><body><p><span style=\" color:#222222;\">" + str(reason) + "</span></p></body></html>")

    def click_agree(self):
        self.conn = pymysql.connect(host='localhost', port=3306, user='root', password="123123",
                                    db="petadoption")
        self.cur = self.conn.cursor()
        sql_adopt_update = "update petadoption.adoptionapplication set a_state = 'Y' ,a_result = 'Y' ,a_id = '{}'where ap_id = '{}'".format(self.a_id,self.ap_id)
        self.cur.execute(sql_adopt_update)
        self.conn.commit()
        self.cur.close()
        self.conn.close()
        self.close()

    def click_refuse(self):
        self.conn = pymysql.connect(host='localhost', port=3306, user='root', password="123123",
                                    db="petadoption")
        self.cur = self.conn.cursor()
        sql_adopt_update = "update petadoption.adoptionapplication set a_state = 'Y' ,a_result = 'N' ,a_id = '{}'where ap_id = '{}'".format(self.a_id,self.ap_id)
        self.cur.execute(sql_adopt_update)
        self.conn.commit()
        self.cur.close()
        self.conn.close()
        self.close()