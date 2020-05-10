# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PortalDesign.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import json
import requests
import webbrowser


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")

        MainWindow.setFixedSize(426, 300)
        MainWindow.setWindowIcon(QtGui.QIcon("Logo/pic.png"))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setEnabled(True)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(220, 90, 151, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("Sports")
        self.comboBox.addItem("Entertainment")
        self.comboBox.addItem("Business")
        self.comboBox.addItem("Technology")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(140, 20, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(30, 90, 191, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(130, 150, 131, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 426, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.pushButton.clicked.connect(self.Submit)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "News Portal"))
        self.label.setText(_translate("MainWindow", "News Portal"))
        self.label_2.setText(_translate("MainWindow", "Please select the News category:"))
        self.pushButton.setText(_translate("MainWindow", "Submit"))

    def Warning(self,title,text):
        self.msg=QtWidgets.QMessageBox()
        self.msg.setWindowTitle(title)
        self.msg.setIcon(QtWidgets.QMessageBox.Information)
        self.msg.setText(text)
        self.msg.exec()



    def WriteHtml(self,Data):
        f = open('Report.html', 'w',encoding="utf16")
        htmlcontent="""
        <!DOCTYPE html>
<html>
<head>
<style>
table {
  font-family: arial, sans-serif;
  border-collapse: collapse;
  width: 80%;
}

td, th {
  border: 1px solid #dddddd;
  text-align: left;
  padding: 8px;
}

tr:nth-child(even) {
  background-color: #dddddd;
}
</style>
</head>
<body>

<h2>News Report</h2>

<table>
  <tr>
      <th>SR.No</th>
    <th>Title</th>
    <th>Description</th>
    <th>URL</th>
      <th>Image</th>
  </tr>"""+Data+"""
</table>

</body>
</html>
        
        
        """

        f.write(htmlcontent)
        f.close()

        webbrowser.open_new_tab('Report.html')

    def RequestData(self, result):
        apilink = "https://newsapi.org/v2/top-headlines?category=" + str(
            result) + "&language=en&apiKey=4e96082c9ca2451ea7bbdffc2078039a"
        try:
            r = requests.get(apilink)
            r_dict = r.json()
            news = r_dict["articles"]
            Data = ""
            count = 1
            for i in news:
                # print(i)
                # print(i["title"])
                # print(i["description"])
                # print(i["url"])
                # print(i["urlToImage"])

                Data = Data + "<tr><td>" + str(count) + "</td><td>" + str(i["title"]) + "</td><td>" + str(
                    i["description"]) + "</td><td><a href=\"" + str(i["url"]) + "\" target=\"_blank\"</a>" + str(i["url"]) + "</td><td><img src=\"" + str(i["urlToImage"]) + "\" height=\"60\"  width=\"60\"></td></tr>"
                count = count + 1
            self.WriteHtml(Data)
        except Exception as e:
            self.Warning("Warning", "Please check the Internet Connection!!!\n" + str(e))

    def Submit(self):
        result=self.comboBox.currentText()
        if result!="":
            self.RequestData(result)

        else:
            self.Warning("No Input","Please select the category!!!")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
