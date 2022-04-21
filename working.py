# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface1.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
from random import randint, choice

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QIcon
from PIL import Image


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1218, 827)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.width_spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.width_spinBox.setMinimumSize(QtCore.QSize(100, 0))
        self.width_spinBox.setObjectName("width_spinBox")
        self.gridLayout.addWidget(self.width_spinBox, 4, 5, 1, 1)
        self.height_spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.height_spinBox.setMinimumSize(QtCore.QSize(100, 0))
        self.height_spinBox.setObjectName("height_spinBox")
        self.gridLayout.addWidget(self.height_spinBox, 4, 3, 1, 1)
        self.quantity_spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.quantity_spinBox.setMinimumSize(QtCore.QSize(70, 0))
        self.quantity_spinBox.setObjectName("quantity_spinBox")
        self.gridLayout.addWidget(self.quantity_spinBox, 4, 13, 1, 1)
        self.apply_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.apply_pushButton.setMinimumSize(QtCore.QSize(70, 40))
        self.apply_pushButton.setStyleSheet("font: 12pt \"MS PGothic\";\n"
                                            "")
        self.apply_pushButton.setObjectName("apply_pushButton")
        self.gridLayout.addWidget(self.apply_pushButton, 4, 15, 1, 1)
        self.width_label = QtWidgets.QLabel(self.centralwidget)
        self.width_label.setMinimumSize(QtCore.QSize(10, 0))
        self.width_label.setMaximumSize(QtCore.QSize(200, 40))
        self.width_label.setStyleSheet("font: 12pt \"MS PGothic\";")
        self.width_label.setObjectName("width_label")
        self.gridLayout.addWidget(self.width_label, 3, 5, 1, 2)
        self.max_height_label = QtWidgets.QLabel(self.centralwidget)
        self.max_height_label.setObjectName("max_height_label")
        self.gridLayout.addWidget(self.max_height_label, 4, 4, 1, 1)
        self.max_width_label = QtWidgets.QLabel(self.centralwidget)
        self.max_width_label.setObjectName("max_width_label")
        self.gridLayout.addWidget(self.max_width_label, 4, 6, 1, 1)
        self.main_image_label = QtWidgets.QLabel(self.centralwidget)
        self.main_image_label.setMinimumSize(QtCore.QSize(1200, 700))
        self.main_image_label.setMaximumSize(QtCore.QSize(1200, 700))
        self.main_image_label.setStyleSheet("background-color: rgb(118, 255, 97);")
        self.main_image_label.setText("")
        self.main_image_label.setObjectName("main_image_label")
        self.gridLayout.addWidget(self.main_image_label, 0, 0, 3, 17)
        self.blue_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.blue_pushButton.setObjectName("blue_pushButton")
        self.gridLayout.addWidget(self.blue_pushButton, 4, 11, 1, 1)
        self.green_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.green_pushButton.setObjectName("green_pushButton")
        self.gridLayout.addWidget(self.green_pushButton, 4, 10, 1, 1)
        self.color_label = QtWidgets.QLabel(self.centralwidget)
        self.color_label.setStyleSheet("font: 12pt \"MS PGothic\";")
        self.color_label.setObjectName("color_label")
        self.gridLayout.addWidget(self.color_label, 3, 10, 1, 1)
        self.red_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.red_pushButton.setObjectName("red_pushButton")
        self.gridLayout.addWidget(self.red_pushButton, 4, 9, 1, 1)
        self.name_im_label = QtWidgets.QLabel(self.centralwidget)
        self.name_im_label.setStyleSheet("font: 12pt \"MS PGothic\";")
        self.name_im_label.setObjectName("name_im_label")
        self.gridLayout.addWidget(self.name_im_label, 3, 0, 1, 1)
        self.load_im_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.load_im_pushButton.setObjectName("load_im_pushButton")
        self.gridLayout.addWidget(self.load_im_pushButton, 4, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 4, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 4, 8, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 4, 12, 1, 1)
        self.height_label = QtWidgets.QLabel(self.centralwidget)
        self.height_label.setMinimumSize(QtCore.QSize(10, 0))
        self.height_label.setStyleSheet("font: 12pt \"MS PGothic\";")
        self.height_label.setObjectName("height_label")
        self.gridLayout.addWidget(self.height_label, 3, 3, 1, 2)
        self.image_name_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.image_name_lineEdit.setObjectName("image_name_lineEdit")
        self.gridLayout.addWidget(self.image_name_lineEdit, 4, 0, 1, 1)
        self.quantity_label = QtWidgets.QLabel(self.centralwidget)
        self.quantity_label.setStyleSheet("font: 12pt \"MS PGothic\";")
        self.quantity_label.setObjectName("quantity_label")
        self.gridLayout.addWidget(self.quantity_label, 3, 13, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1218, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.apply_pushButton.setText(_translate("MainWindow", "Apply"))
        self.width_label.setText(_translate("MainWindow", "Width of surface"))
        self.max_height_label.setText(_translate("MainWindow", "Maximum - 1000"))
        self.max_width_label.setText(_translate("MainWindow", "Maximum - 1600"))
        self.blue_pushButton.setText(_translate("MainWindow", "Blue"))
        self.green_pushButton.setText(_translate("MainWindow", "Green"))
        self.color_label.setText(_translate("MainWindow", "Color of surface"))
        self.red_pushButton.setText(_translate("MainWindow", "Red"))
        self.name_im_label.setText(_translate("MainWindow", "Name of image"))
        self.load_im_pushButton.setText(_translate("MainWindow", "Load"))
        self.height_label.setText(_translate("MainWindow", "Height of surface"))
        self.quantity_label.setText(_translate("MainWindow", "Quantity"))

    def set_image(self):
        self.main_image_width = 1200
        self.main_image_height = 700
        self.main_image = Image.new('RGB', (self.main_image_width, self.main_image_height), (118, 255, 97))

        self.image = Image.open('image/Image.png')

        self.width, self.height = self.image.size

        print(f'''Start image size:
        Width: {self.width} Height: {self.height}
''')

        self.assist_image = Image.new('RGB', (self.width, self.height),
                                      (118, 255, 97))  # assist image = green bg + editing image
        self.assist_image.paste(self.image, (0, 0), self.image)
        # self.assist_image.show()
        self.pixels = self.assist_image.load()
        self.main_image_matrix = [[0 for i in range(self.main_image_height)] for j in range(self.main_image_width)]

        # -------------------------------------------------------------------------------------------
        # ---------------------------------CROPPING, COUNTING SQUARE---------------------------------
        # -------------------------------------------------------------------------------------------
        self.image_square = 0
        lower_right_coord = [None, None]  # lower right - L
        upper_left_coord = [None, None]  # upper left - U:
        # _  _  U  _  _  1  _  _  _  _  _
        # _  _  _  _  _  1  _  _  _  _  _
        # _  _  1  2  3  4  5  6  7  _  _
        # _  _  1  _  _  2  _  _  3  _  _
        # _  _  1  _  _  2  _  _  L  _  _

        for i in range(self.width):
            for j in range(self.height):
                r, g, b = self.pixels[i, j]
                if r != 118 and g != 255 and b != 97:  # if pix not green = if pix != None
                    # -----------------------------
                    self.image_square += 1
                    # -----------------------------
                    if upper_left_coord[0] is None:
                        upper_left_coord[0] = i
                    if upper_left_coord[1] is None:
                        upper_left_coord[1] = j

                    if lower_right_coord[0] is None:
                        lower_right_coord[0] = i
                    if lower_right_coord[1] is None:
                        lower_right_coord[1] = j
                    else:
                        if upper_left_coord[0] > i:
                            upper_left_coord = i
                        if upper_left_coord[1] > j:
                            upper_left_coord[1] = j

                        if lower_right_coord[0] < i:
                            lower_right_coord[0] = i
                        if lower_right_coord[1] < j:
                            lower_right_coord[1] = j
                    # -----------------------------

        print((f'''New coords:
            Upper Left point: {upper_left_coord[0], upper_left_coord[1]};
            Lower right point: {lower_right_coord[0], lower_right_coord[1]}
'''))
        print(f'''Square of PNG im (in pixels): {self.image_square}
''')
        # -------RESULTING--------

        # ---maximum possible quality of small images in big main image---
        possible_quality = (1200 * 700) // self.image_square
        self.assist_image = self.assist_image.crop(
            (upper_left_coord[0], upper_left_coord[1], lower_right_coord[0], lower_right_coord[1]))
        self.image = self.image.crop(
            (upper_left_coord[0], upper_left_coord[1], lower_right_coord[0], lower_right_coord[1]))
        self.assist_image.show()
        print(f'''Possible quality: {possible_quality}
''')

        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        pixmap = QPixmap('image/Image.png')
        self.main_image_label.setPixmap(pixmap)

        #
        #
        #
        #
        #
        # for i in range(2):
        # ------------------------------------------------------------------------------------------
        # --------------------------------------RANDOM EDITING--------------------------------------
        # ------------------------------------------------------------------------------------------

        flip_degrees = [0, 90, 180, 270]  # список градусов поворота
        degrees = choice(flip_degrees)  # выбор градуса поворота

        self.image = self.image.rotate(degrees, expand=True)  # поворот PNG изображения
        self.assist_image = self.assist_image.rotate(
            degrees,
            expand=True)  # поворот того же изображения, но наложенного на зеленый фон (r = 118 and g = 255 and b = 97)
        self.assist_image.show()
        # self.image.show()
        self.width, self.height = self.image.size  # переопределение размеров
        x, y = (randint(0, self.main_image_width - self.width)), (self.main_image_height - self.height)
        # x, y = 10, (self.main_image_height - self.height)
        print(
            f'''New random coordinates: {x, y}
    New random flip degrees: {degrees}
    ''')

        # ------------------------------------------------------------------------------------------
        # --------------------------------------TABLE CREATING--------------------------------------
        # ------------------------------------------------------------------------------------------

        pixels = self.assist_image.load()
        self.image_matrix = [[0 for i in range(self.height)] for j in
                             range(self.width)]  # создание матрицы с нулями
        for i in range(self.height):
            for j in range(self.width):
                r, g, b = pixels[j, i]
                if r != 118 and g != 255 and b != 97:  # if pix not green = if pix != None
                    self.image_matrix[j][i] = 1  # замена 0 на 1
        print(self.image_matrix)

        # ------------------------------------------------------------------------------------------
        # -----------------------------------MAIN MATRIX UPDATING-----------------------------------
        # ------------------------------------------------------------------------------------------
        # transferring little matrix to big one for checking overlaying
        #
        # copied_matrix = self.main_image_matrix
        # good_height = False
        # self.image_quality = 0
        # while y >= 0 and not good_height:
        #     overlay = False
        #     fail_counter = 0
        #     count = 0
        #     for j in range(self.main_image_width):
        #         for i in range(self.main_image_height):
        #             # вход в обработку матрицы
        #             if x <= j < x + self.width and y < i < y + self.height:
        #                 new_j, new_i = j - x, i - y
        #                 print(y)
        #                 #print(i, x, j, y, new_i, new_j)
        #                 if self.main_image_matrix[j][i] == self.image_matrix[new_j][new_i] == 1:
        #                     overlay = True
        #                     count += 1
        #                 else:
        #                     self.main_image_matrix[j][i] = self.image_matrix[new_j][new_i]
        #
        #
        #     if overlay:
        #         y -= 1
        #         self.main_image_matrix = copied_matrix
        #         fail_counter += 1
        #         print(count)
        #         overlay = False
        #     else:
        #         good_height = True
        #         self.main_image.paste(self.image, (x, y), self.image)
        #         fail_counter = 0
        #         self.image_quality += 1
        #         print('OK')
        # if y < 0:
        #     print('pisez')
        #     print(self.main_image_matrix)
        # self.main_image.show()


if __name__ == "__main__":
    # try:
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()

    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.set_image()

    # MainWindow.show()
    sys.exit(app.exec_())
# except IndexError:
#     print()
