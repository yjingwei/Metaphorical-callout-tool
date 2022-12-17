# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'annotations.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1359, 974)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame_tagging = QtWidgets.QFrame(self.centralwidget)
        self.frame_tagging.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_tagging.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_tagging.setObjectName("frame_tagging")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_tagging)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_pic = QtWidgets.QFrame(self.frame_tagging)
        self.frame_pic.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_pic.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_pic.setObjectName("frame_pic")
        self.label_showimage = QtWidgets.QLabel(self.frame_pic)
        self.label_showimage.setGeometry(QtCore.QRect(0, 0, 661, 701))
        self.label_showimage.setObjectName("label_showimage")
        self.pushButton_pre_pic = QtWidgets.QPushButton(self.frame_pic)
        self.pushButton_pre_pic.setGeometry(QtCore.QRect(70, 740, 93, 28))
        self.pushButton_pre_pic.setObjectName("pushButton_pre_pic")
        self.pushButton_next_pic = QtWidgets.QPushButton(self.frame_pic)
        self.pushButton_next_pic.setGeometry(QtCore.QRect(240, 740, 93, 28))
        self.pushButton_next_pic.setObjectName("pushButton_next_pic")
        self.get_whether_annotation = QtWidgets.QLabel(self.frame_pic)
        self.get_whether_annotation.setGeometry(QtCore.QRect(450, 740, 151, 31))
        self.get_whether_annotation.setObjectName("get_whether_annotation")
        self.label_finish = QtWidgets.QLabel(self.frame_pic)
        self.label_finish.setGeometry(QtCore.QRect(130, 660, 231, 16))
        self.label_finish.setText("")
        self.label_finish.setObjectName("label_finish")
        self.frame_show = QtWidgets.QFrame(self.frame_pic)
        self.frame_show.setGeometry(QtCore.QRect(670, 0, 664, 792))
        self.frame_show.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_show.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_show.setObjectName("frame_show")
        self.label_category_pic = QtWidgets.QLabel(self.frame_show)
        self.label_category_pic.setGeometry(QtCore.QRect(0, 0, 651, 351))
        self.label_category_pic.setObjectName("label_category_pic")
        self.label_adj_pic = QtWidgets.QLabel(self.frame_show)
        self.label_adj_pic.setGeometry(QtCore.QRect(10, 440, 631, 301))
        self.label_adj_pic.setObjectName("label_adj_pic")
        self.label1 = QtWidgets.QLabel(self.frame_show)
        self.label1.setGeometry(QtCore.QRect(10, 380, 41, 16))
        self.label1.setObjectName("label1")
        self.label6 = QtWidgets.QLabel(self.frame_show)
        self.label6.setGeometry(QtCore.QRect(20, 750, 41, 16))
        self.label6.setObjectName("label6")
        self.label7 = QtWidgets.QLabel(self.frame_show)
        self.label7.setGeometry(QtCore.QRect(260, 750, 41, 16))
        self.label7.setObjectName("label7")
        self.label2 = QtWidgets.QLabel(self.frame_show)
        self.label2.setGeometry(QtCore.QRect(180, 380, 51, 16))
        self.label2.setObjectName("label2")
        self.label4 = QtWidgets.QLabel(self.frame_show)
        self.label4.setGeometry(QtCore.QRect(400, 380, 41, 16))
        self.label4.setObjectName("label4")
        self.label5 = QtWidgets.QLabel(self.frame_show)
        self.label5.setGeometry(QtCore.QRect(150, 410, 81, 20))
        self.label5.setObjectName("label5")
        self.label3 = QtWidgets.QLabel(self.frame_show)
        self.label3.setGeometry(QtCore.QRect(370, 410, 72, 15))
        self.label3.setObjectName("label3")
        self.label_metaphor_fix1 = QtWidgets.QLabel(self.frame_show)
        self.label_metaphor_fix1.setGeometry(QtCore.QRect(60, 380, 72, 15))
        self.label_metaphor_fix1.setObjectName("label_metaphor_fix1")
        self.label_target_fix = QtWidgets.QLabel(self.frame_show)
        self.label_target_fix.setGeometry(QtCore.QRect(260, 380, 72, 15))
        self.label_target_fix.setObjectName("label_target_fix")
        self.label_target_category_fix = QtWidgets.QLabel(self.frame_show)
        self.label_target_category_fix.setGeometry(QtCore.QRect(260, 410, 72, 15))
        self.label_target_category_fix.setObjectName("label_target_category_fix")
        self.label_source_fix = QtWidgets.QLabel(self.frame_show)
        self.label_source_fix.setGeometry(QtCore.QRect(460, 380, 72, 15))
        self.label_source_fix.setObjectName("label_source_fix")
        self.label_source_category_fix = QtWidgets.QLabel(self.frame_show)
        self.label_source_category_fix.setGeometry(QtCore.QRect(460, 410, 72, 15))
        self.label_source_category_fix.setObjectName("label_source_category_fix")
        self.label_metaphor_fix2 = QtWidgets.QLabel(self.frame_show)
        self.label_metaphor_fix2.setGeometry(QtCore.QRect(70, 750, 72, 15))
        self.label_metaphor_fix2.setObjectName("label_metaphor_fix2")
        self.label_yudi_fix = QtWidgets.QLabel(self.frame_show)
        self.label_yudi_fix.setGeometry(QtCore.QRect(310, 650, 72, 15))
        self.label_yudi_fix.setText("")
        self.label_yudi_fix.setObjectName("label_yudi_fix")
        self.gridLayout.addWidget(self.frame_pic, 2, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame_tagging, 0, 0, 1, 1)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 100))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.lineEdit_source_category = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_source_category.setObjectName("lineEdit_source_category")
        self.gridLayout_3.addWidget(self.lineEdit_source_category, 3, 6, 1, 1)
        self.yudi = QtWidgets.QLabel(self.frame_3)
        self.yudi.setObjectName("yudi")
        self.gridLayout_3.addWidget(self.yudi, 3, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 0, 7, 1, 1)
        self.source_category = QtWidgets.QLabel(self.frame_3)
        self.source_category.setObjectName("source_category")
        self.gridLayout_3.addWidget(self.source_category, 3, 4, 1, 2)
        self.lineEdit_source = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_source.setObjectName("lineEdit_source")
        self.gridLayout_3.addWidget(self.lineEdit_source, 3, 3, 1, 1)
        self.lineEdit_target_category = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_target_category.setObjectName("lineEdit_target_category")
        self.gridLayout_3.addWidget(self.lineEdit_target_category, 0, 5, 1, 2)
        self.lineEdit_yudi = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_yudi.setObjectName("lineEdit_yudi")
        self.gridLayout_3.addWidget(self.lineEdit_yudi, 3, 1, 1, 1)
        self.source = QtWidgets.QLabel(self.frame_3)
        self.source.setObjectName("source")
        self.gridLayout_3.addWidget(self.source, 3, 2, 1, 1)
        self.lineEdit_target = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_target.setObjectName("lineEdit_target")
        self.gridLayout_3.addWidget(self.lineEdit_target, 0, 3, 1, 1)
        self.radioButton_0 = QtWidgets.QRadioButton(self.frame_3)
        self.radioButton_0.setObjectName("radioButton_0")
        self.gridLayout_3.addWidget(self.radioButton_0, 0, 1, 1, 1)
        self.metaphor = QtWidgets.QLabel(self.frame_3)
        self.metaphor.setObjectName("metaphor")
        self.gridLayout_3.addWidget(self.metaphor, 0, 0, 1, 1)
        self.target = QtWidgets.QLabel(self.frame_3)
        self.target.setObjectName("target")
        self.gridLayout_3.addWidget(self.target, 0, 2, 1, 1)
        self.pushButton_confirm = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_confirm.setObjectName("pushButton_confirm")
        self.gridLayout_3.addWidget(self.pushButton_confirm, 3, 7, 1, 1)
        self.targetcategory = QtWidgets.QLabel(self.frame_3)
        self.targetcategory.setObjectName("targetcategory")
        self.gridLayout_3.addWidget(self.targetcategory, 0, 4, 1, 1)
        self.radioButton_1 = QtWidgets.QRadioButton(self.frame_3)
        self.radioButton_1.setObjectName("radioButton_1")
        self.gridLayout_3.addWidget(self.radioButton_1, 1, 1, 1, 1)
        self.gridLayout_2.addWidget(self.frame_3, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1359, 26))
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
        self.label_showimage.setText(_translate("MainWindow", "showimage"))
        self.pushButton_pre_pic.setText(_translate("MainWindow", "上一个"))
        self.pushButton_next_pic.setText(_translate("MainWindow", "下一个"))
        self.get_whether_annotation.setText(_translate("MainWindow", "TextLabel"))
        self.label_category_pic.setText(_translate("MainWindow", "catagory"))
        self.label_adj_pic.setText(_translate("MainWindow", "adj"))
        self.label1.setText(_translate("MainWindow", "隐喻:"))
        self.label6.setText(_translate("MainWindow", "隐喻:"))
        self.label7.setText(_translate("MainWindow", "喻底:"))
        self.label2.setText(_translate("MainWindow", "目标域:"))
        self.label4.setText(_translate("MainWindow", "源域:"))
        self.label5.setText(_translate("MainWindow", "目标域类别:"))
        self.label3.setText(_translate("MainWindow", "源域类别:"))
        self.label_metaphor_fix1.setText(_translate("MainWindow", "TextLabel"))
        self.label_target_fix.setText(_translate("MainWindow", "TextLabel"))
        self.label_target_category_fix.setText(_translate("MainWindow", "TextLabel"))
        self.label_source_fix.setText(_translate("MainWindow", "TextLabel"))
        self.label_source_category_fix.setText(_translate("MainWindow", "TextLabel"))
        self.label_metaphor_fix2.setText(_translate("MainWindow", "TextLabel"))
        self.yudi.setText(_translate("MainWindow", "喻底"))
        self.source_category.setText(_translate("MainWindow", "源域类别"))
        self.source.setText(_translate("MainWindow", "源域"))
        self.radioButton_0.setText(_translate("MainWindow", "0"))
        self.metaphor.setText(_translate("MainWindow", "隐喻"))
        self.target.setText(_translate("MainWindow", "目标域"))
        self.pushButton_confirm.setText(_translate("MainWindow", "标注完成"))
        self.targetcategory.setText(_translate("MainWindow", "目标域类别"))
        self.radioButton_1.setText(_translate("MainWindow", "1"))
