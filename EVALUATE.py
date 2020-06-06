# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'finalpage.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_evaluationwindow(object):
    def setupU(self,evaluationwindow):
        evaluationwindow.setObjectName("evaluationwindow")
        evaluationwindow.resize(514, 432)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../ms-dhoni.webp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        evaluationwindow.setWindowIcon(icon)
        evaluationwindow.setStyleSheet("background-color: rgb(170, 170, 170);")
        self.verticalLayout = QtWidgets.QVBoxLayout(evaluationwindow)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(evaluationwindow)
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.line = QtWidgets.QFrame(evaluationwindow)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.matchlabel = QtWidgets.QLabel(evaluationwindow)
        self.matchlabel.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.matchlabel.setObjectName("matchlabel")
        self.horizontalLayout_5.addWidget(self.matchlabel)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.teamlabel = QtWidgets.QLabel(evaluationwindow)
        self.teamlabel.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.teamlabel.setObjectName("teamlabel")
        self.horizontalLayout_5.addWidget(self.teamlabel)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.teamcomboBox = QtWidgets.QComboBox(evaluationwindow)
        self.teamcomboBox.setMaximumSize(QtCore.QSize(73, 16777215))
        self.teamcomboBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.teamcomboBox.setObjectName("teamcomboBox")
        
        
        import sqlite3
        conn = sqlite3.connect('mycricket.db')
        self.horizontalLayout_2.addWidget(self.teamcomboBox)
        sql="select name from teams;"
        cur=conn.execute(sql)
        teams=[]
        for row in cur:
            self.teamcomboBox.addItem(row[0])        
        conn.close()
        spacerItem1 = QtWidgets.QSpacerItem(78, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.matchcomboBox = QtWidgets.QComboBox(evaluationwindow)
        self.matchcomboBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.matchcomboBox.setEditable(False)
        self.matchcomboBox.setCurrentText("")
        self.matchcomboBox.setObjectName("matchcomboBox")
        self.horizontalLayout_2.addWidget(self.matchcomboBox)
        self.matchcomboBox.addItem("match1")
        self.matchcomboBox.addItem("match2")
        self.matchcomboBox.addItem("match3")
        self.matchcomboBox.addItem("match4")
        self.matchcomboBox.addItem("match5")
        

        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.line_2 = QtWidgets.QFrame(evaluationwindow)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.playerlabel = QtWidgets.QLabel(evaluationwindow)
        self.playerlabel.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.playerlabel.setObjectName("playerlabel")
        self.horizontalLayout_4.addWidget(self.playerlabel)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.pointslabel = QtWidgets.QLabel(evaluationwindow)
        self.pointslabel.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pointslabel.setObjectName("pointslabel")
        self.horizontalLayout_4.addWidget(self.pointslabel)
        self.lineEdit = QtWidgets.QLineEdit(evaluationwindow)
        self.lineEdit.setStyleSheet("background-color: rgb(247, 247, 247);")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_4.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.playerslistWidget = QtWidgets.QListWidget(evaluationwindow)
        self.playerslistWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.playerslistWidget.setObjectName("playerslistWidget")
        self.horizontalLayout.addWidget(self.playerslistWidget)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.pointslistWidget = QtWidgets.QListWidget(evaluationwindow)
        self.pointslistWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pointslistWidget.setObjectName("pointslistWidget")
        self.horizontalLayout.addWidget(self.pointslistWidget)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.line_3 = QtWidgets.QFrame(evaluationwindow)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout.addWidget(self.line_3)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.calculatepushButton = QtWidgets.QPushButton(evaluationwindow)
        self.calculatepushButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.calculatepushButton.setObjectName("calculatepushButton")

        self.calculatepushButton.clicked.connect(self.calculate)
        
        self.horizontalLayout_3.addWidget(self.calculatepushButton)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(evaluationwindow)
        QtCore.QMetaObject.connectSlotsByName(evaluationwindow)

    def calculate(self):
        import sqlite3
        conn = sqlite3.connect('mycricket.db')
        team=self.teamcomboBox.currentText()
        self.playerslistWidget.clear()
        sql1="SELECT Player, Value from Teams where Name='"+team+"'"
        cur=conn.execute(sql1)
        row=cur.fetchone()
        selected=row[0].split(',')
       # print (selected)
        self.playerslistWidget.addItems(selected)
        teamttl=0
        #print("ded")
        self.pointslistWidget.clear()
        match=self.matchcomboBox.currentText()
        for i in range(self.playerslistWidget.count()-1):
            ttl, batscore, bowlscore, fieldscore=0,0,0,0
            nm=self.playerslistWidget.item(i).text()
            cursor=conn.execute("select * from "+match+" where player='"+nm+"';")
            while True:
                row=cursor.fetchone()
                if row == None:
                    break
                else:
                    batscore=int(row[1]/2)
                    if batscore>=50: batscore+=5
                    if batscore>=100: batscore+=10
                    if row[1]>0:
                        sr=row[1]/row[2]
                        if sr>=80 and sr<100: batscore+=2
                        if sr>=100:batscore+=4
                    batscore=batscore+row[3]
                    batscore=batscore+2*row[4]
                    #print ("batting score=", batscore)
                    bowlscore=row[8]*10
                    if row[8]>=3: bowlscore=bowlscore+5
                    if row[8]>=5: bowlscore=bowlscore=bowlscore+10
                    if row[7]>0:
                        er=6*row[7]/row[5]
                        #print ("eco:")
                        if er<=2: bowlscore=bowlscore+10
                        if er>2 and er<=3.5: bowlscore=bowlscore+7
                        if er>3.5 and er<=4.5: bowlscore=bowlscore+4
                    fieldscore=(row[9]+row[10]+row[11])*10            
                    ttl=batscore+bowlscore+fieldscore
            #print("frfm")
            self.pointslistWidget.addItem(str(ttl))
            int(ttl)
            teamttl=teamttl+ttl
            
        self.lineEdit.setText(str(teamttl))
        #print("du")
        
    
    def retranslateUi(self, evaluationwindow):
        _translate = QtCore.QCoreApplication.translate
        evaluationwindow.setWindowTitle(_translate("evaluationwindow", "evaluation"))
        self.label.setText(_translate("evaluationwindow", "Evaluate the performance of your fantasy team"))
        self.matchlabel.setText(_translate("evaluationwindow", "Team"))
        self.teamlabel.setText(_translate("evaluationwindow", "Match"))
        self.playerlabel.setText(_translate("evaluationwindow", "Players"))
        self.pointslabel.setText(_translate("evaluationwindow", "Points"))
        self.calculatepushButton.setText(_translate("evaluationwindow", "calculate"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    evaluationwindow = QtWidgets.QDialog()
    ui = Ui_evaluationwindow()
    ui.setupU(evaluationwindow)
    evaluationwindow.show()
    sys.exit(app.exec_())
