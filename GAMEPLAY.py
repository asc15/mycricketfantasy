from PyQt5 import QtCore, QtGui, QtWidgets 
from PyQt5.QtWidgets import QMessageBox
import sqlite3
conn = sqlite3.connect('mycricket.db')
cur = conn.cursor()

class Ui_GameplayWindow(object):
        
    def setupUi(self,GameplayWindow):
    
        GameplayWindow.setObjectName("GameplayWindow")
        GameplayWindow.setWindowModality(QtCore.Qt.NonModal)
        GameplayWindow.resize(631, 486)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        GameplayWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../virat-kohli.webp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        GameplayWindow.setWindowIcon(icon)
        GameplayWindow.setAutoFillBackground(False)
        GameplayWindow.setStyleSheet("BACKGROUND-COLOR:rgb(170, 255, 127);\n""")
        GameplayWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(GameplayWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.selectionframe = QtWidgets.QFrame(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.selectionframe.setFont(font)
        self.selectionframe.setStyleSheet("BACKGROUND-COLOR:rgb(193, 166, 200);\n""")
        self.selectionframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.selectionframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.selectionframe.setObjectName("selectionframe")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.selectionframe)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Yourselection_label = QtWidgets.QLabel(self.selectionframe)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.Yourselection_label.setFont(font)
        self.Yourselection_label.setStyleSheet("font: 75 8pt \"MS Shell Dlg 2\";")
        self.Yourselection_label.setObjectName("Yourselection_label")
        self.verticalLayout.addWidget(self.Yourselection_label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.bat_label = QtWidgets.QLabel(self.selectionframe)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.bat_label.setFont(font)
        self.bat_label.setStyleSheet("font: 75 8pt \"MS Shell Dlg 2\";\n""BACKGROUND-COLOR:rgb(255, 170, 127);")
        self.bat_label.setObjectName("bat_label")
        self.horizontalLayout.addWidget(self.bat_label)
        self.batsmanlabel = QtWidgets.QLabel(self.selectionframe)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.batsmanlabel.setFont(font)
        self.batsmanlabel.setText("")
        self.batsmanlabel.setObjectName("batsmanlabel")
        self.horizontalLayout.addWidget(self.batsmanlabel)
        spacerItem = QtWidgets.QSpacerItem(17, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.bow_label = QtWidgets.QLabel(self.selectionframe)
        self.bow_label.setStyleSheet("BACKGROUND-COLOR:rgb(255, 170, 127);")
        self.bow_label.setObjectName("bow_label")
        self.horizontalLayout.addWidget(self.bow_label)
        self.bowlerlabel = QtWidgets.QLabel(self.selectionframe)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.bowlerlabel.setFont(font)
        self.bowlerlabel.setText("")
        self.bowlerlabel.setObjectName("bowlerlabel")
        self.horizontalLayout.addWidget(self.bowlerlabel)
        spacerItem1 = QtWidgets.QSpacerItem(17, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.ar_label = QtWidgets.QLabel(self.selectionframe)
        self.ar_label.setStyleSheet("BACKGROUND-COLOR:rgb(255, 170, 127);")
        self.ar_label.setObjectName("ar_label")
        self.horizontalLayout.addWidget(self.ar_label)
        self.allrounderlabel = QtWidgets.QLabel(self.selectionframe)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.allrounderlabel.setFont(font)
        self.allrounderlabel.setText("")
        self.allrounderlabel.setObjectName("allrounderlabel")
        self.horizontalLayout.addWidget(self.allrounderlabel)
        spacerItem2 = QtWidgets.QSpacerItem(17, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.wk_label = QtWidgets.QLabel(self.selectionframe)
        self.wk_label.setStyleSheet("BACKGROUND-COLOR:rgb(255, 170, 127);")
        self.wk_label.setObjectName("wk_label")
        self.horizontalLayout.addWidget(self.wk_label)
        self.wicketkeeperlabel = QtWidgets.QLabel(self.selectionframe)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.wicketkeeperlabel.setFont(font)
        self.wicketkeeperlabel.setText("")
        self.wicketkeeperlabel.setObjectName("wicketkeeperlabel")
        self.horizontalLayout.addWidget(self.wicketkeeperlabel)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addWidget(self.selectionframe)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pointsavail_label = QtWidgets.QLabel(self.centralwidget)
        self.pointsavail_label.setStyleSheet("BACKGROUND-COLOR:rgb(255, 170, 127);")
        self.pointsavail_label.setObjectName("pointsavail_label")
        self.horizontalLayout_2.addWidget(self.pointsavail_label)
        self.palabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.palabel.setFont(font)
        self.palabel.setText("")
        self.palabel.setObjectName("palabel")
        self.horizontalLayout_2.addWidget(self.palabel)
        spacerItem3 = QtWidgets.QSpacerItem(188, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.pointsused_label = QtWidgets.QLabel(self.centralwidget)
        self.pointsused_label.setStyleSheet("BACKGROUND-COLOR:rgb(255, 170, 127);\n""")
        self.pointsused_label.setObjectName("pointsused_label")
        self.horizontalLayout_2.addWidget(self.pointsused_label)
        self.pulabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pulabel.setFont(font)
        self.pulabel.setText("")
        self.pulabel.setObjectName("pulabel")
        self.horizontalLayout_2.addWidget(self.pulabel)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.bat_radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.bat_radioButton.setStyleSheet("background-color:rgb(255, 255, 127);")
        self.bat_radioButton.setObjectName("bat_radioButton")
        self.horizontalLayout_3.addWidget(self.bat_radioButton)
        self.bow_radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.bow_radioButton.setStyleSheet("background-color:rgb(255, 255, 127);\n""")
        self.bow_radioButton.setObjectName("bow_radioButton")
        self.horizontalLayout_3.addWidget(self.bow_radioButton)
        self.ar_radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.ar_radioButton.setStyleSheet("background-color:rgb(255, 255, 127);")
        self.ar_radioButton.setObjectName("ar_radioButton")
        self.horizontalLayout_3.addWidget(self.ar_radioButton)
        self.wk_radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.wk_radioButton.setStyleSheet("background-color:rgb(255, 255, 127);")
        self.wk_radioButton.setObjectName("wk_radioButton")
        self.horizontalLayout_3.addWidget(self.wk_radioButton)
        spacerItem4 = QtWidgets.QSpacerItem(158, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.teamname_label = QtWidgets.QLabel(self.centralwidget)
        self.teamname_label.setStyleSheet("BACKGROUND-COLOR:rgb(255, 170, 127);")
        self.teamname_label.setObjectName("teamname_label")
        self.horizontalLayout_3.addWidget(self.teamname_label)
        self.tnlabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.tnlabel.setFont(font)
        self.tnlabel.setText("")
        self.tnlabel.setObjectName("tnlabel")
        self.horizontalLayout_3.addWidget(self.tnlabel)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem5 = QtWidgets.QSpacerItem(48, 68, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 0, 1, 1, 1)
        self.used_listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.used_listWidget.setStyleSheet("BACKGROUND-COLOR:rgb(227, 227, 227)\n"";")
        self.used_listWidget.setObjectName("used_listWidget")
        self.gridLayout.addWidget(self.used_listWidget, 0, 2, 1, 1)
        self.availabe_listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.availabe_listWidget.setStyleSheet("BACKGROUND-COLOR:rgb(227, 227, 227);")
        self.availabe_listWidget.setObjectName("availabe_listWidget")
        self.gridLayout.addWidget(self.availabe_listWidget, 0, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem6 = QtWidgets.QSpacerItem(228, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem6)
        self.exit_Button = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed Extra Bold")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.exit_Button.setFont(font)
        self.exit_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.exit_Button.setFocusPolicy(QtCore.Qt.TabFocus)
        self.exit_Button.setAutoFillBackground(False)
        self.exit_Button.setStyleSheet("background-color:rgb(255, 0,0);\n""color:white;\n""border:outset;\n""font: 12pt \"Tw Cen MT Condensed Extra Bold\";\n""")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../ms-dhoni.webp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exit_Button.setIcon(icon1)
        self.exit_Button.setAutoDefault(False)
        self.exit_Button.setDefault(False)
        self.exit_Button.setFlat(False)
        self.exit_Button.setObjectName("exit_Button")
        self.horizontalLayout_9.addWidget(self.exit_Button)
        spacerItem7 = QtWidgets.QSpacerItem(228, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem7)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.selectionframe.raise_()
        self.bat_label.raise_()
        self.batsmanlabel.raise_()
        self.bow_label.raise_()
        self.bowlerlabel.raise_()
        self.ar_label.raise_()
        self.allrounderlabel.raise_()
        self.wk_label.raise_()
        self.wicketkeeperlabel.raise_()
        self.palabel.raise_()
        self.pulabel.raise_()
        self.tnlabel.raise_()
        self.bat_label.raise_()
        self.batsmanlabel.raise_()
        self.bow_label.raise_()
        self.bowlerlabel.raise_()
        self.ar_label.raise_()
        self.allrounderlabel.raise_()
        self.wk_label.raise_()
        self.wicketkeeperlabel.raise_()
        GameplayWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(GameplayWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 631, 21))
        self.menubar.setObjectName("menubar")
        self.menuManage_Teams = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.menuManage_Teams.setFont(font)
        self.menuManage_Teams.setStyleSheet("BACKGROUND-COLOR:rgb(255, 170, 0);\n""color:rrgb(255, 255, 127);")
        self.menuManage_Teams.setObjectName("menuManage_Teams")
        GameplayWindow.setMenuBar(self.menubar)
        self.actionNEW_TEAM = QtWidgets.QAction(GameplayWindow)
        self.actionNEW_TEAM.setObjectName("actionNEW_TEAM")
        self.actionSAVE_TEAM = QtWidgets.QAction(GameplayWindow)
        self.actionSAVE_TEAM.setObjectName("actionSAVE_TEAM")
        self.actionOPEN_TEAM = QtWidgets.QAction(GameplayWindow)
        self.actionOPEN_TEAM.setObjectName("actionOPEN_TEAM")
        self.actionEVALUATE_TEAM = QtWidgets.QAction(GameplayWindow)
        self.actionEVALUATE_TEAM.setObjectName("actionEVALUATE_TEAM")
        self.menuManage_Teams.addAction(self.actionNEW_TEAM)
        self.menuManage_Teams.addAction(self.actionSAVE_TEAM)
        self.menuManage_Teams.addSeparator()
        self.menuManage_Teams.addAction(self.actionOPEN_TEAM)
        self.menuManage_Teams.addAction(self.actionEVALUATE_TEAM)
        self.menubar.addAction(self.menuManage_Teams.menuAction())

        



        self.availabe_listWidget.itemDoubleClicked.connect(self.removelist1)
        self.used_listWidget.itemDoubleClicked.connect(self.removelist2)


        self.bow_radioButton.toggled.connect(self.ctg)
        self.bat_radioButton.toggled.connect(self.ctg)
        self.ar_radioButton.toggled.connect(self.ctg)
        self.wk_radioButton.toggled.connect(self.ctg) 


        

        self.menuManage_Teams.triggered[QtWidgets.QAction].connect(self.menu)
        self.exit_Button.clicked.connect(self.exit)
        
        self.bat=0
        self.bwl=0
        self.ar=0
        self.wk=0
        self.avl=200
        self.used=0

        self.retranslateUi(GameplayWindow)
        QtCore.QMetaObject.connectSlotsByName(GameplayWindow)
        
    


    def retranslateUi(self, GameplayWindow):
        _translate = QtCore.QCoreApplication.translate
        GameplayWindow.setWindowTitle(_translate("GameplayWindow", "GAMEPLAY"))
        self.Yourselection_label.setText(_translate("GameplayWindow", "Your Selections:"))
        self.bat_label.setText(_translate("GameplayWindow", "Batsmen(BAT)"))
        self.bow_label.setText(_translate("GameplayWindow", "Bowlers(BOW)"))
        self.ar_label.setText(_translate("GameplayWindow", "Allrounders(AR)"))
        self.wk_label.setText(_translate("GameplayWindow", "WicketKeepers(WK)"))
        self.pointsavail_label.setText(_translate("GameplayWindow", "Points Available"))
        self.pointsused_label.setText(_translate("GameplayWindow", "Points Used"))
        self.bat_radioButton.setText(_translate("GameplayWindow", "BAT"))
        self.bow_radioButton.setText(_translate("GameplayWindow", "BOW"))
        self.ar_radioButton.setText(_translate("GameplayWindow", "AR"))
        self.wk_radioButton.setText(_translate("GameplayWindow", "WK"))
        self.teamname_label.setText(_translate("GameplayWindow", "Team Name"))
        self.exit_Button.setText(_translate("GameplayWindow", "exit"))
        self.exit_Button.setShortcut(_translate("GameplayWindow", "Return"))
        self.menuManage_Teams.setTitle(_translate("GameplayWindow", "Manage Teams"))
        self.actionNEW_TEAM.setText(_translate("GameplayWindow", "NEW TEAM"))
        self.actionSAVE_TEAM.setText(_translate("GameplayWindow", "SAVE TEAM"))
        self.actionOPEN_TEAM.setText(_translate("GameplayWindow", "OPEN TEAM"))
        self.actionEVALUATE_TEAM.setText(_translate("GameplayWindow", "EVALUATE TEAM"))



    def exit(self):
        import sys
        self.showdlg("Thank YOU for Visiting....Hope you enjoyed !!")
        sys.exit()





    def menu(self,action):
        txt=(action.text())
    
        if txt=='NEW TEAM':
            self.bat=0
            self.bwl=0
            self.ar=0
            self.wk=0
            self.avl=200
            self.used=0
            self.availabe_listWidget.clear()
            self.used_listWidget.clear()
            
            
            text, ok=QtWidgets.QInputDialog.getText(GameplayWindow,"Team", "Enter name of team:")
            if ok== True:
                self.tnlabel.setText(str(text))

            self.show()


        if txt=='SAVE TEAM':
            count=self.used_listWidget.count()
            selected=""
            for i in range(count):
                selected+=self.used_listWidget.item(i).text()
                if i<count:
                    selected+=","
            self.saveteam(self.tnlabel.text(),selected,self.used)

        if txt=='OPEN TEAM':
            self.bat=0
            self.bwl=0
            self.ar=0
            self.wk=0
            self.avl=200
            self.used=0
            self.availabe_listWidget.clear()
            self.used_listWidget.clear()
            self.show()

            
            self.openteam()


        if txt=='EVALUATE TEAM':
            from EVALUATE import Ui_evaluationwindow
            self.w= QtWidgets.QDialog()
            self.ui = Ui_evaluationwindow()
            self.ui.setupU(self.w)
            GameplayWindow.hide()
            self.w.show()

            


        


    def show(self):

        self.batsmanlabel.setText(str(self.bat))
        self.bowlerlabel.setText(str(self.bwl))
        self.wicketkeeperlabel.setText(str(self.wk))
        self.allrounderlabel.setText(str(self.ar))
        
        self.palabel.setText(str(self.avl))
        self.pulabel.setText(str(self.used))
        



    def criteria(self,ctgr,item):
        msg=''
        if ctgr=="BAT" and self.bat>=5:msg="Batsmen not more than 5"
        if ctgr=="BOW" and self.bwl>=5:msg="bowlers not more than 5"
        if ctgr=="AR" and self.ar>=3:msg="Allrounders not more than 3"
        if ctgr=="WK" and self.wk>=1:msg="Wicketkeepers not more than 1"
        if msg!='':
            self.showdlg(msg)
            return False
        
        if self.avl<=0:
            msg="You Have Exhausted your Points"
            self.showdlg(msg)
            return False
        
        if ctgr=="BAT":self.bat+=1
        if ctgr=="BOW":self.bwl+=1
        if ctgr=="AR":self.ar+=1
        if ctgr=="WK":self.wk+=1

        
        sql="SELECT points from players where player='"+item.text()+"'"
        cur=conn.execute(sql)
        row=cur.fetchone()
        self.avl-=int(row[0])
        self.used+=int(row[0])
        return True

    
    


    def removelist1(self,item):
        
        ctgr=''
        if self.bat_radioButton.isChecked()==True:ctgr='BAT'
        if self.bow_radioButton.isChecked()==True:ctgr='BOW'
        if self.ar_radioButton.isChecked()==True:ctgr='AR'
        if self.wk_radioButton.isChecked()==True:ctgr='WK'
        ret=self.criteria(ctgr,item)
        
        if ret==True:
            self.availabe_listWidget.takeItem(self.availabe_listWidget.row(item))
            
            self.used_listWidget.addItem(item.text())
            self.show()
            


    def ctg(self):
        ctgr=''
        if self.bat_radioButton.isChecked()==True:ctgr='BAT'
        if self.bow_radioButton.isChecked()==True:ctgr='BOW'
        if self.ar_radioButton.isChecked()==True:ctgr='AR'
        if self.wk_radioButton.isChecked()==True:ctgr='WK'
       	
        self.fillList(ctgr)


    def removelist2(self,item):
        self.used_listWidget.takeItem(self.used_listWidget.row(item))
        
        cursor = conn.execute("SELECT player,points, category from players where player='"+item.text()+"'")
        row=cursor.fetchone()
        self.avl=self.avl+int(row[1])
        self.used=self.used-int(row[1])
        ctgr=row[2]
        if ctgr=="BAT":
            self.bat-=1
            if self.bat_radioButton.isChecked()==True:self.availabe_listWidget.addItem(item.text())
        if ctgr=="BOW":
            self.bwl-=1
            if self.bow_radioButton.isChecked()==True:self.availabe_listWidget.addItem(item.text())
        if ctgr=="AR":
            self.ar-=1
            if self.ar_radioButton.isChecked()==True:self.availabe_listWidget.addItem(item.text())
        if ctgr=="WK":
            self.wk-=1
            if self.wk_radioButton.isChecked()==True:self.availabe_listWidget.addItem(item.text())
        self.show()


    def fillList(self,ctgr):
        if self.tnlabel.text()=='':
            self.showdlg("Enter name of team")
            return
        
        self.availabe_listWidget.clear()
        sql="SELECT player from players where category='"+ctgr+"';"
        cur=conn.execute(sql)
        for row in cur:
            selected=[]
            for i in range(self.used_listWidget.count()):
                selected.append(self.used_listWidget.item(i).text())
            if row[0] not in selected:self.availabe_listWidget.addItem(row[0])
            
        

    def openteam(self):
       
        sql="select name from teams;"
       
        cur=conn.execute(sql)
        teams=[]
        for row in cur:
            teams.append(row[0])
        
        team, ok=QtWidgets.QInputDialog.getItem(GameplayWindow,"Dream","Choose A Team",teams,0,False)
        if ok and team:
            self.tnlabel.setText(team)
        
        sql1="SELECT player,value from teams where name='"+team+"';"
        cur=conn.execute(sql1)
        row=cur.fetchone()
        selected=row[0].split(',')
        self.used_listWidget.addItems(selected)
        self.used=row[1]
        
        self.avl=200-row[1]
        count=self.availabe_listWidget.count()

        for i in range(count-1):
            ply=self.used_listWidget.item(i).text()
            sql="select category from stats where player='"+ply+"';" 
            cur=conn.execute(sql) 
            row=cur.fetchone() 
            ctgr=row[0]
        
            if ctgr=="BAT":self.bat+=1
            if ctgr=="BOW":self.bwl+=1
            if ctgr=="AR":self.ar+=1
            if ctgr=="WK":self.wk+=1
        self.show()
        
        



        

    def saveteam(self,nm,ply,val):
        
        
        if self.bat+self.bwl+self.ar+self.wk!=11:
            self.showdlg("Insufficient players, Please TRY AGAIN!")
            return
        
        
        sql="INSERT INTO teams (name,player,value) VALUES ('"+nm+"','"+ply+"','"+str(val)+"');"
        
        try:
            
            cur=conn.execute(sql)
            
            self.showdlg("Team Saved Succesfully")
            conn.commit()
        except:
            self.showdlg("Error in Operation")
            conn.rollback()   
        
        
    def showdlg(self,msg):
    
        Dialog=QtWidgets.QMessageBox()
        Dialog.setText(msg)
        Dialog.setWindowTitle("Dream Team selector")
        ret=Dialog.exec()
    
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    GameplayWindow = QtWidgets.QMainWindow()
    ui = Ui_GameplayWindow()
    ui.setupUi(GameplayWindow)
    GameplayWindow.show()
    Dialog=QtWidgets.QMessageBox()
    Dialog.setInformativeText("MY FANTASY CRICKET \nLETS PLAY!")
    Dialog.setWindowTitle("WELCOME")
    Dialog.show()    
    sys.exit(app.exec_())
