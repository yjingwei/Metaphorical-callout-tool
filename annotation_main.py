import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from annotations import *
# 读取数据
import pandas as pd
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QTableWidgetItem, QComboBox, QMessageBox, \
    QHeaderView
import numpy as np

start = 0
end = 300
filename = "iF_去重.csv"
pic_file = r"D:/yjw/iFYTEK_pics/"
    #"/Users/jingwei.yu/Desktop/隐喻标注_中文广告/iFYTEK_pics/"

def subdata(filename,start,end):
    data = pd.read_csv("iF_1.csv", encoding='utf-8')[start:end]
    df_diff = data[data.Metaphor != data.Metaphor_2]
    df_same = data[data.Metaphor == data.Metaphor_2]
    return df_diff, df_same


def mergedata(df1, df2):
    pd.concat([df1, df2], axis=0)
    # id_num	pic_id	Text	Metaphor	Target	Target category	Source	Source category	sentiment	Metaphor_2	yudi
    pd.to_csv('final_iF.csv', index=False)
    return

class MyClass(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyClass, self).__init__(parent)
        self.data = pd.read_csv(filename, encoding='utf-8')[start:end]


        self.data['annotation'] = 0
        self.subdata()
        self.index = -1
        # self.Metaphor_fix1 = ""
        # self.target_fix1 = ""
        # self.source_fix1 = ""

        self.setupUi(self)
        self.radioButton_0.setCheckable(True)
        self.pushButton_next_pic.clicked.connect(self.nextimage)
        jpg = QtGui.QPixmap("./imgs/img.png").scaled(self.label_category_pic.width(), self.label_category_pic.height())
        self.label_category_pic.setPixmap(jpg)
        jpg = QtGui.QPixmap("./imgs/img_1.png").scaled(self.label_adj_pic.width(), self.label_adj_pic.height())
        self.label_adj_pic.setPixmap(jpg)
        self.pushButton_confirm.clicked.connect(self.writeincsv)
        self.pushButton_pre_pic.clicked.connect(self.preimage)
        self.radioButton_0.toggled.connect(self.setdata1)
        self.radioButton_1.toggled.connect(self.setdata2)

       # self.mergedata()

    def nextimage(self):
        self.index = self.index + 1
        if(self.index >= self.len):
            msg_box = QMessageBox(QMessageBox.Warning, '恭喜你', '完成标注')
            msg_box.exec_()
            return

        _translate = QtCore.QCoreApplication.translate

        img_path = os.path.join(pic_file, self.df_diff.iloc[self.index, 1])
        print("img_path====", img_path)
        if(int(self.df_diff.iloc[self.index, 11]) == 1):
            self.get_whether_annotation.setText(_translate("MainWindow", "Yes!{0}/{1}".format(self.index,self.len)))
        else:
            self.get_whether_annotation.setText(_translate("MainWindow", "NoNoNo!{0}/{1}".format(self.index,self.len)))
        #imgName, imgType = QFileDialog.getOpenFileName(self, "打开图片", "", "*.jpg;;*.png;;All Files(*)")

        self.metaphor_fix1 = str(self.df_diff.iloc[self.index, 3])
        self.target_fix = str(self.df_diff.iloc[self.index, 4])
        self.target_category_fix = str(self.df_diff.iloc[self.index, 5])
        self.source_fix = str(self.df_diff.iloc[self.index, 6])
        self.source_category_fix = str(self.df_diff.iloc[self.index, 7])
        self.sentiment_fix = str(self.df_diff.iloc[self.index, 8])
        self.metaphor_fix2 = str(int(self.df_diff.iloc[self.index, 9]))
        if (self.metaphor_fix2 != self.metaphor_fix2):
            self.metaphor_fix2 = 0
        self.yudi_fix = str(self.df_diff.iloc[self.index, 10])

        jpg = QtGui.QPixmap(img_path).scaled(self.label_showimage.width(), self.label_showimage.height())
        self.label_showimage.setPixmap(jpg)
        self.label_metaphor_fix1.setText(_translate("MainWindow", self.metaphor_fix1))
        self.label_target_fix.setText(_translate("MainWindow", self.target_fix))
        self.label_target_category_fix.setText(_translate("MainWindow", self.target_category_fix))
        self.label_source_fix.setText(_translate("MainWindow", self.source_fix))
        self.label_source_category_fix.setText(_translate("MainWindow", self.source_category_fix))
        self.label_metaphor_fix2.setText(_translate("MainWindow", str(self.metaphor_fix2)))
        self.label_yudi_fix.setText(_translate("MainWindow", self.yudi_fix))

        self.setdata1()
        self.setdata2()




        # self.lineEdit_metaphor.setText(_translate("MainWindow", self.metaphor_fix1))
        # self.lineEdit_target.setText(_translate("MainWindow", self.target_fix))
        # self.lineEdit_target_category.setText(_translate("MainWindow", self.target_category_fix))
        # self.lineEdit_source.setText(_translate("MainWindow", self.source_fix))
        # self.lineEdit_source_category.setText(_translate("MainWindow", self.source_category_fix))
        # self.lineEdit_yudi.setText(_translate("MainWindow", self.yudi_fix))

    def preimage(self):
        self.index =self.index -1
        if (self.index < 0):
            msg_box = QMessageBox(QMessageBox.Warning, '警告', '已经是第一张啦 往后看吧')
            msg_box.exec_()
            return
        _translate = QtCore.QCoreApplication.translate
        # if (self.index >= len(self.df_diff)):
        #     self.label_finish.setText(_translate("MainWindow", "标注已完成！！！"))
        img_path = os.path.join(pic_file,
                                self.df_diff.iloc[self.index, 1])
        if(int(self.df_diff.iloc[self.index, 11]) == 1):
            self.get_whether_annotation.setText(_translate("MainWindow", "Yes!{0}/{1}".format(self.index,self.len)))
        else:
            self.get_whether_annotation.setText(_translate("MainWindow", "NoNoNo快点标吧 还剩下!{0}/{1}".format(self.index,self.len)))
        # imgName, imgType = QFileDialog.getOpenFileName(self, "打开图片", "", "*.jpg;;*.png;;All Files(*)")

        self.metaphor_fix1 = str(self.df_diff.iloc[self.index, 3])
        self.target_fix = str(self.df_diff.iloc[self.index, 4])
        self.target_category_fix = str(self.df_diff.iloc[self.index, 5])
        self.source_fix = str(self.df_diff.iloc[self.index, 6])
        self.source_category_fix = str(self.df_diff.iloc[self.index, 7])
        self.sentiment_fix = str(self.df_diff.iloc[self.index, 8])
        self.metaphor_fix2 = str(self.df_diff.iloc[self.index, 9])
        self.yudi_fix = str(self.df_diff.iloc[self.index, 10])

        jpg = QtGui.QPixmap(img_path).scaled(self.label_showimage.width(), self.label_showimage.height())
        self.label_showimage.setPixmap(jpg)
        self.label_metaphor_fix1.setText(_translate("MainWindow", self.metaphor_fix1))
        self.label_target_fix.setText(_translate("MainWindow", self.target_fix))
        self.label_target_category_fix.setText(_translate("MainWindow", self.target_category_fix))
        self.label_source_fix.setText(_translate("MainWindow", self.source_fix))
        self.label_source_category_fix.setText(_translate("MainWindow", self.source_category_fix))
        self.label_metaphor_fix2.setText(_translate("MainWindow", self.metaphor_fix2))
        self.label_yudi_fix.setText(_translate("MainWindow", self.yudi_fix))

        self.setdata1()
        self.setdata2()

    def setdata2(self):
        if self.radioButton_1.isChecked()==True:
            if int(self.metaphor_fix1) == 1:
                self.listento1()
            else:
                self.listento2()
        # else:
        #     if int(self.metaphor_fix1) == 0:
        #         self.listento1()
        #     else:
        #         self.listento2()
        # _translate = QtCore.QCoreApplication.translate
        # if int(self.metaphor_fix1) == 1:
        #     self.metaphor_fix1 = int(self.metaphor_fix1)
        #     # self.lineEdit_metaphor.setText(_translate("MainWindow", self.metaphor_fix1))
        #     self.lineEdit_target.setText(_translate("MainWindow", self.target_fix))
        #     self.lineEdit_target_category.setText(_translate("MainWindow", self.target_category_fix))
        #     self.lineEdit_source.setText(_translate("MainWindow", self.source_fix))
        #     self.lineEdit_source_category.setText(_translate("MainWindow", self.source_category_fix))
        #     self.lineEdit_yudi.setText(_translate("MainWindow", ""))
        # else:
        #     self.metaphor_fix1 = int(self.metaphor_fix2)
        #     # self.lineEdit_metaphor.setText(_translate("MainWindow", self.metaphor_fix1))
        #     self.lineEdit_target.setText(_translate("MainWindow", ""))
        #     self.lineEdit_target_category.setText(_translate("MainWindow", ""))
        #     self.lineEdit_source.setText(_translate("MainWindow", ""))
        #     self.lineEdit_source_category.setText(_translate("MainWindow", ""))
        #     self.lineEdit_yudi.setText(_translate("MainWindow", self.yudi_fix))

    def listento1(self):
        _translate = QtCore.QCoreApplication.translate
        self.lineEdit_metaphor_fix1 = int(self.metaphor_fix1)
        # self.lineEdit_metaphor.setText(_translate("MainWindow", self.metaphor_fix1))
        self.lineEdit_target.setText(_translate("MainWindow", self.target_fix))
        self.lineEdit_target_category.setText(_translate("MainWindow", self.target_category_fix))
        self.lineEdit_source.setText(_translate("MainWindow", self.source_fix))
        self.lineEdit_source_category.setText(_translate("MainWindow", self.source_category_fix))
        self.lineEdit_yudi.setText(_translate("MainWindow", ""))

    def listento2(self):
        _translate = QtCore.QCoreApplication.translate
        # print("self.metaphor_fix2===", self.metaphor_fix2)

        self.lineEdit_metaphor_fix1 = int(self.metaphor_fix2)
        # self.lineEdit_metaphor.setText(_translate("MainWindow", self.metaphor_fix1))
        self.lineEdit_target.setText(_translate("MainWindow", ""))
        self.lineEdit_target_category.setText(_translate("MainWindow", ""))
        self.lineEdit_source.setText(_translate("MainWindow", ""))
        self.lineEdit_source_category.setText(_translate("MainWindow", ""))
        self.lineEdit_yudi.setText(_translate("MainWindow", self.yudi_fix))

    def setdata1(self):
        if self.radioButton_0.isChecked()==True:
            _translate = QtCore.QCoreApplication.translate
            self.lineEdit_metaphor_fix1 = 0
            # self.lineEdit_metaphor.setText(_translate("MainWindow", self.metaphor_fix1))
            self.lineEdit_target.setText(_translate("MainWindow", ""))
            self.lineEdit_target_category.setText(_translate("MainWindow", ""))
            self.lineEdit_source.setText(_translate("MainWindow", ""))
            self.lineEdit_source_category.setText(_translate("MainWindow", ""))
            self.lineEdit_yudi.setText(_translate("MainWindow", ""))
            # if int(self.metaphor_fix1) == 0:
            #     self.listento1()
            # else:
            #     self.listento2()

    def changenan(self,str):
        # return lambda str: "" if str == "nan" else str
        if(str == "nan"):
            return ""
        else:
            return str

    def writeincsv(self):
        _translate = QtCore.QCoreApplication.translate

        self.metaphor_fix1 = int(self.radioButton_1.isChecked())
        self.target_fix = self.changenan(self.lineEdit_target.text())

        self.target_category_fix = self.changenan(self.lineEdit_target_category.text())
        self.source_fix = self.changenan(self.lineEdit_source.text())
        self.source_category_fix = self.changenan(self.lineEdit_source_category.text())
        self.yudi_fix = self.changenan(self.lineEdit_yudi.text())

        #
        self.df_diff.loc[self.index, 'Metaphor'] = self.metaphor_fix1
        self.df_diff.loc[self.index, 'Target'] = self.target_fix
        self.df_diff.loc[self.index, 'Target category'] = self.target_category_fix
        self.df_diff.loc[self.index, 'Source'] = self.source_fix
        self.df_diff.loc[self.index, 'Source category'] = self.source_category_fix
        self.df_diff.loc[self.index, 'yudi'] = self.yudi_fix
        self.df_diff.loc[self.index, 'annotation'] = 1

        if (int(self.df_diff.iloc[self.index, 11]) == 1):
            self.get_whether_annotation.setText(_translate("MainWindow", "Yes!{0}/{1}".format(self.index,self.len)))
        else:
            self.get_whether_annotation.setText(_translate("MainWindow", "NoNONo{0}/{1}".format(self.index,self.len)))
        #if self.index % 3 ==0:
        self.mergedata()
        # self.df_diff.to_csv("diff{}.csv".format(self.index),index=False)
        # self.radioButton_0.setChecked(False)
        # self.radioButton_1.setChecked(False)



    def subdata(self):
        self.data['Metaphor_2'].fillna(int(0),inplace=True)
        # self.data['yudi'].fillna(int(0),inplace=True)
        self.data['Metaphor'] = self.data['Metaphor'].apply(lambda x : int(x))
        self.data['Metaphor_2'] = self.data['Metaphor_2'].apply(lambda x: int(x))
        #print(self.data.head(10))
        self.df_diff = self.data[self.data.Metaphor != self.data.Metaphor_2].reset_index(drop=True)
        self.df_same = self.data[self.data.Metaphor == self.data.Metaphor_2].reset_index(drop=True)
        self.len = len(self.df_diff)


    def mergedata(self):
        self.final = pd.concat([self.df_diff, self.df_same], axis=0)
        # self.final.to_csv('final_iF_{}.csv'.format(self.index), index=False)
        self.final.to_csv('final_iF.csv', index=False)




if __name__ == '__main__':

    app = QApplication(sys.argv)
    myWin = MyClass()
    myWin.show()
    sys.exit(app.exec_())


