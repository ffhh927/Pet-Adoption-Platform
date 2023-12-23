import pymysql

from Lib.adopt_admini_over import Ui_Form
try:
    from PyQt5.QtCore import QPoint, QRect, QSize, Qt
    from PyQt5.QtWidgets import (QApplication, QLayout, QPushButton,
                                 QSizePolicy, QWidget)
except ImportError:
    from PySide2.QtCore import QPoint, QRect, QSize, Qt
    from PySide2.QtWidgets import (QApplication, QLayout, QPushButton,
                                   QSizePolicy, QWidget)
class adopt_admini_over_item(QWidget, Ui_Form):

    def __init__(self, *args):
        super(adopt_admini_over_item, self).__init__(*args)
        self.setupUi(self)

    def init(self, name, sex, age,addr,f_mun,is_adopted,phone,email,p_id,reason,ap_id,a_state,a_result):
        self.ap_id = ap_id
        self.label_12.setText("<html><head/><body><p><span style=\" color:#222222;\">"+str(name)+ "</span></p></body></html>")
        self.label_13.setText("<html><head/><body><p><span style=\" color:#222222;\">"+str(sex)+ "</span></p></body></html>")
        self.label_14.setText("<html><head/><body><p><span style=\" color:#222222;\">"+str(age)+ "</span></p></body></html>")
        self.label_10.setText("<html><head/><body><p><span style=\" color:#222222;\">"+str(f_mun)+ "</span></p></body></html>")
        self.label_11.setText("<html><head/><body><p><span style=\" color:#222222;\">"+str(addr)+ "</span></p></body></html>")
        self.checkBox.setChecked(bool(is_adopted))
        self.checkBox.setEnabled(False)
        self.label_15.setText("<html><head/><body><p><span style=\" color:#222222;\">"+str(phone)+ "</span></p></body></html>")
        self.label_16.setText("<html><head/><body><p><span style=\" color:#222222;\">"+str(email)+ "</span></p></body></html>")
        self.label_17.setText("<html><head/><body><p><span style=\" color:#222222;\">"+str(p_id)+ "</span></p></body></html>")
        self.label_18.setText("<html><head/><body><p><span style=\" color:#222222;\">"+str(reason)+ "</span></p></body></html>")

        if str(a_state) == 'Y':
            self.label_20.setText(
                "<html><head/><body><p><span style=\" color:#222222;\">" + '已处理' + "</span></p></body></html>")
        else:
            self.label_20.setText(
                "<html><head/><body><p><span style=\" color:#222222;\">" + '未处理' + "</span></p></body></html>")
        #  self.label_20.setText("<html><head/><body><p><span style=\" color:#222222;\">"+str(a_state)+ "</span></p></body></html>")
        if str(a_result) == 'Y':
            self.label_22.setText(
                "<html><head/><body><p><span style=\" color:#222222;\">" + '批准' + "</span></p></body></html>")
        elif str(a_result) == 'N':
            self.label_22.setText(
                "<html><head/><body><p><span style=\" color:#222222;\">" + '驳回' + "</span></p></body></html>")
        else:
            self.label_22.setText(
                "<html><head/><body><p><span style=\" color:#222222;\">" + '未处理' + "</span></p></body></html>")
