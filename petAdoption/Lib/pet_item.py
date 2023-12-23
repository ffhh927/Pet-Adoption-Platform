import main

try:
    from PyQt5.QtCore import QSize, QUrl
    from PyQt5.QtGui import QPaintEvent, QPixmap
    from PyQt5.QtNetwork import QNetworkRequest
    from PyQt5.QtWidgets import QWidget
except ImportError:
    from PySide2.QtCore import QSize, QUrl
    from PySide2.QtGui import QPaintEvent, QPixmap
    from PySide2.QtNetwork import QNetworkRequest
    from PySide2.QtWidgets import QWidget

from Lib.itemwidget import Ui_Form
try:
    from PyQt5.QtCore import QPoint, QRect, QSize, Qt
    from PyQt5.QtWidgets import (QApplication, QLayout, QPushButton,
                                 QSizePolicy, QWidget)
except ImportError:
    from PySide2.QtCore import QPoint, QRect, QSize, Qt
    from PySide2.QtWidgets import (QApplication, QLayout, QPushButton,
                                   QSizePolicy, QWidget)


from PyQt5.QtGui import QPalette,QPixmap,QFont
class Pet_Item(QWidget, Ui_Form):

    def __init__(self, *args):
        super(Pet_Item, self).__init__(*args)


        self.setupUi(self)
        # self.pushButton.clicked.connect(lambda: self.click_jump_alter())
        self.pet_name = ''
        self.pet_nature = ''
        self.pet_age = ''
        self.pet_breed = ''
        self.pet_id = ''

    def init(self, pet_name, pet_nature, pet_age, pet_breed,pet_id,pet_sex):
        self.pet_name = pet_name
        self.pet_nature = pet_nature
        self.pet_age = pet_age
        self.pet_breed = pet_breed
        self.pet_id = pet_id
        self.pet_sex = pet_sex
        print(pet_sex)
        # if str(self.pet_sex) == '0':
        #     self.pet_sex_text = '公'
        # else:
        #     self.pet_sex_text = '母'
        self.label_id.setText("<html><head/><body><p><span style=\" color:#222222;\">"+pet_id + "</span></p></body></html>")
        self.label_name.setText("<html><head/><body><p><span style=\" color:#222222;\">"+pet_name + "</span></p></body></html>")
        self.label_breed.setText("<html><head/><body><p><span style=\" color:#222222;\">"+pet_breed + "</span></p></body></html>")
        self.label_age.setText("<html><head/><body><p><span style=\" color:#222222;\">"+pet_age + "</span></p></body></html>")
        self.label_nature.setText("<html><head/><body><p><span style=\" color:#222222;\">"+pet_nature + "</span></p></body></html>")
        self.label_id_2.setText("<html><head/><body><p><span style=\" color:#222222;\">"+str(self.pet_sex) + "</span></p></body></html>")

    # def click_jump_alter(self):
    #     main.start.stackedWidget.setCurrentIndex(6)
    #     main.start.lineEdit_breed_3.setText(str(self.pet_id))
    #     main.start.lineEdit_name_2.setText(str(self.pet_name))
    #     main.start.lineEdit_breed_2.setText(str(self.pet_breed))
    #     main.start.lineEdit_age_2.setText(str(self.pet_age))
    #     main.start.comboBox_sex_2.setCurrentIndex(int(self.pet_sex))
    #     main.start.textEdit_3.setText(str(self.pet_nature))

    # self.label.setText(_translate("Form", "照片"))
# self.label_2.setText(_translate("Form", "名字："))
# self.label_3.setText(_translate("Form", "品种："))
# self.label_4.setText(_translate("Form", "年龄："))
# self.label_5.setText(_translate("Form", "性格："))
# self.pushButton.setText(_translate("Form", "前往申请领养"))
if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    mainWin = Pet_Item()
    mainWin.show()
    sys.exit(app.exec_())