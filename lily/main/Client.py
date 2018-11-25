# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MongodbMain.ui'
#
# Created by: PyQt5 UI code generator 5.8
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from lily.mongodb import DataBaseSupport
import sys
from lily.mongodb.SqlResolver import SqlResolver

class Ui_MainWindow(object):



    def __init__(self) -> None:
        super().__init__()
        self.dataBaseName=""
        self.tableName=""
        self.pageSize = 20
        self.currPage = 1
        self.find = {}

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1107, 865)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.rtframe = QtWidgets.QFrame(self.centralwidget)
        self.rtframe.setGeometry(QtCore.QRect(200, 0, 901, 181))
        self.rtframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.rtframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.rtframe.setObjectName("rtframe")
        self.textEdit = QtWidgets.QTextEdit(self.rtframe)
        self.textEdit.setGeometry(QtCore.QRect(10, 50, 881, 121))
        self.textEdit.setObjectName("textEdit")
        self.pushButton_3 = QtWidgets.QPushButton(self.rtframe)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 20, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.rtframe)
        self.pushButton_4.setGeometry(QtCore.QRect(100, 20, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.lframe = QtWidgets.QFrame(self.centralwidget)
        self.lframe.setGeometry(QtCore.QRect(0, 0, 191, 811))
        self.lframe.setAutoFillBackground(False)
        self.lframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.lframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lframe.setObjectName("lframe")
        self.treeView = QtWidgets.QTreeWidget(self.lframe)
        self.treeView.setGeometry(QtCore.QRect(10, 10, 171, 791))
        self.treeView.setObjectName("treeView")
        self.rbframe = QtWidgets.QFrame(self.centralwidget)
        self.rbframe.setGeometry(QtCore.QRect(200, 200, 901, 611))
        self.rbframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.rbframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.rbframe.setObjectName("rbframe")
        self.tableView = QtWidgets.QTableWidget(self.rbframe)
        self.tableView.setGeometry(QtCore.QRect(10, 50, 881, 551))
        self.tableView.setObjectName("tableView")
        self.comboBox = QtWidgets.QComboBox(self.rbframe)
        self.comboBox.setGeometry(QtCore.QRect(630, 10, 31, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label = QtWidgets.QLabel(self.rbframe)
        self.label.setGeometry(QtCore.QRect(670, 12, 171, 16))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.rbframe)
        self.pushButton.setGeometry(QtCore.QRect(590, 10, 31, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.rbframe)
        self.pushButton_2.setGeometry(QtCore.QRect(550, 10, 31, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1107, 23))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionconnect = QtWidgets.QAction(MainWindow)
        self.actionconnect.setObjectName("actionconnect")
        self.actionopen_file = QtWidgets.QAction(MainWindow)
        self.actionopen_file.setObjectName("actionopen_file")
        self.menuFile.addAction(self.actionconnect)
        self.menuFile.addAction(self.actionopen_file)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_3.setText(_translate("MainWindow", "Execute"))
        self.pushButton_4.setText(_translate("MainWindow", "Clear"))
        self.comboBox.setItemText(0, _translate("MainWindow", "5"))
        self.comboBox.setItemText(1, _translate("MainWindow", "10"))
        self.comboBox.setItemText(2, _translate("MainWindow", "20"))
        self.label.setText(_translate("MainWindow", "第 1 页 共 5 页"))
        self.pushButton.setText(_translate("MainWindow", "Nex"))
        self.pushButton_2.setText(_translate("MainWindow", "Pre"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionconnect.setText(_translate("MainWindow", "connect"))
        self.actionopen_file.setText(_translate("MainWindow", "open file"))

        # 设置TableWiew 数据
        self.loadTableView()
        # 加载左边树状 database 数据
        self.loadTreeView()
        # 执行按钮事件绑定
        self.pushButton_3.clicked.connect(self.execute)
        # 下一页按钮事件绑定
        self.pushButton.clicked.connect(self.nextPage)
        # 上一页按钮事件绑定
        self.pushButton_2.clicked.connect(self.prePage)


    def prePage(self):
        print("pre pages")
        self.currPage = self.currPage - 1
        if self.currPage < 1 :
            self.currPage = 1
        self.loadTableView()

    def nextPage(self):
        print("next pages")
        self.currPage = self.currPage+1
        if self.currPage>self.total:
            self.currPage = self.total
        self.loadTableView()

    def execute(self):
        print("execute")
        sql = self.textEdit.toPlainText()
        self.sql = sql
        self.dataBaseName = "imapi"
        # print( self.loadData(sql))
        self.loadTableView(2)



    def setPager(self):
        _translate = QtCore.QCoreApplication.translate
        t = "第 "+str(self.currPage)+" 页 共 "+str(self.total)+" 页 总记录 "+str(self.count)
        self.label.setText(_translate("MainWindow", t))

    def loadTreeView(self):
        print('set tree view')
        self.treeView.setColumnCount(1)
        self.treeView.setHeaderLabel('Databases')
        va = DataBaseSupport.MongodbUtil.shwDatabases()
        t = 0
        for v in va:
            item = QTreeWidgetItem(self.treeView)
            item.setText(0, v)
            t = t+1
            for c in va[v]:
                itemc = QTreeWidgetItem(item)
                itemc.setText(0,c)
            self.treeView.addTopLevelItem(item)
        self.treeView.itemDoubleClicked['QTreeWidgetItem*','int'].connect(self.getitem)

    def getitem(self, item, column):
        p = item.parent()
        print(p)
        if p is None:return
        self.dataBaseName = item.parent().text(0)
        self.tableName = item.text(0)
        self.currPage = 1
        self.find = {}
        self.loadTableView()

    def loadTableView(self,type=1):
        tableData = None
        if type == 1 :
            if self.dataBaseName.strip() == "" or self.tableName.strip() == "":
                return
            tableData = self.getTableData(self.dataBaseName,self.tableName,self.currPage,self.pageSize,**self.find)
        else :
            tableData = self.loadData(self.sql)

        self.total = tableData["total"]
        self.count = tableData["count"]
        self.setPager()
        self.tableView.setColumnCount(tableData["cloumsCount"])
        self.tableView.setRowCount(tableData["rowCount"])
        self.tableView.setHorizontalHeaderLabels(tableData["cloums"])
        self.tableView.setColumnWidth(0, 50)
        tdata = tableData["data"]
        for i in range(len(tdata)):
            doc = tdata[i]
            j = 0
            for key in tableData["cloums"]:
                if key in doc:
                    self.tableView.setItem(i, j, QTableWidgetItem(str(doc[key])))
                else:
                    self.tableView.setItem(i, j, QTableWidgetItem(""))
                j += 1

    def loadData(self,sql):
        print("loadData")
        commend = SqlResolver.resolv(sql)
        print(commend.find)
        # print(SqlResolver.executeCommend(commend))
        self.tableName = commend.collection
        self.find = commend.find
        l = self.getTableData(self.dataBaseName,self.tableName,self.currPage,self.pageSize,**commend.find)
        print("load data")
        print(l)
        return l

    def getTableData(self,dataBaseName,tableName,currPage,pageSize,**find):
        tableData = {}
        result = DataBaseSupport.MongodbUtil.getDocuments(dataBaseName,tableName,currPage,pageSize,**find)
        tdata = result["data"]
        total = result["total"]
        count = result["count"]
        print("count ： ",count)
        cloums = []
        for i in range(len(tdata)):
            doc = tdata[i]
            j = 0
            for key in doc:
                if key not in cloums:
                    cloums.append(key)
                j += 1
        tableData["cloums"] = cloums
        tableData["rowCount"] = len(tdata)
        tableData["cloumsCount"] = len(cloums)
        tableData["data"] = tdata
        tableData["total"] = total
        tableData["count"] = count
        return tableData

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()

    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())