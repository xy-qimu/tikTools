# Form implementation generated from reading ui file 'tikTools.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(846, 472)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab.sizePolicy().hasHeightForWidth())
        self.tab.setSizePolicy(sizePolicy)
        self.tab.setObjectName("tab")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.btn_select_file = QtWidgets.QPushButton(parent=self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_select_file.sizePolicy().hasHeightForWidth())
        self.btn_select_file.setSizePolicy(sizePolicy)
        self.btn_select_file.setObjectName("btn_select_file")
        self.gridLayout.addWidget(self.btn_select_file, 1, 0, 1, 1)
        self.btn_gen_ddl = QtWidgets.QPushButton(parent=self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_gen_ddl.sizePolicy().hasHeightForWidth())
        self.btn_gen_ddl.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.btn_gen_ddl.setFont(font)
        self.btn_gen_ddl.setObjectName("btn_gen_ddl")
        self.gridLayout.addWidget(self.btn_gen_ddl, 1, 7, 1, 1)
        self.table_file_content = QtWidgets.QTableView(parent=self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table_file_content.sizePolicy().hasHeightForWidth())
        self.table_file_content.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        self.table_file_content.setFont(font)
        self.table_file_content.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.table_file_content.setAutoFillBackground(True)
        self.table_file_content.setAlternatingRowColors(True)
        self.table_file_content.setShowGrid(False)
        self.table_file_content.setObjectName("table_file_content")
        self.table_file_content.horizontalHeader().setCascadingSectionResizes(False)
        self.gridLayout.addWidget(self.table_file_content, 3, 0, 2, 5)
        self.radioBtn_msql = QtWidgets.QRadioButton(parent=self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioBtn_msql.sizePolicy().hasHeightForWidth())
        self.radioBtn_msql.setSizePolicy(sizePolicy)
        self.radioBtn_msql.setObjectName("radioBtn_msql")
        self.gridLayout.addWidget(self.radioBtn_msql, 1, 10, 1, 1, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.radioBtn_psql = QtWidgets.QRadioButton(parent=self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioBtn_psql.sizePolicy().hasHeightForWidth())
        self.radioBtn_psql.setSizePolicy(sizePolicy)
        self.radioBtn_psql.setChecked(False)
        self.radioBtn_psql.setObjectName("radioBtn_psql")
        self.gridLayout.addWidget(self.radioBtn_psql, 1, 9, 1, 1, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.line_3 = QtWidgets.QFrame(parent=self.tab)
        self.line_3.setLineWidth(0)
        self.line_3.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout.addWidget(self.line_3, 1, 6, 1, 1)
        self.line_5 = QtWidgets.QFrame(parent=self.tab)
        self.line_5.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_5.setObjectName("line_5")
        self.gridLayout.addWidget(self.line_5, 0, 6, 1, 1)
        self.line_2 = QtWidgets.QFrame(parent=self.tab)
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 0, 3, 1, 1)
        self.line = QtWidgets.QFrame(parent=self.tab)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 2, 0, 1, 1)
        self.txt_ddl_content = QtWidgets.QTextEdit(parent=self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_ddl_content.sizePolicy().hasHeightForWidth())
        self.txt_ddl_content.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        self.txt_ddl_content.setFont(font)
        self.txt_ddl_content.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.txt_ddl_content.setPlaceholderText("")
        self.txt_ddl_content.setObjectName("txt_ddl_content")
        self.gridLayout.addWidget(self.txt_ddl_content, 4, 7, 1, 4)
        self.txt_file_name = QtWidgets.QLineEdit(parent=self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_file_name.sizePolicy().hasHeightForWidth())
        self.txt_file_name.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(True)
        self.txt_file_name.setFont(font)
        self.txt_file_name.setPlaceholderText("")
        self.txt_file_name.setObjectName("txt_file_name")
        self.gridLayout.addWidget(self.txt_file_name, 1, 1, 1, 4)
        self.radioBtn_dbt = QtWidgets.QRadioButton(parent=self.tab)
        self.radioBtn_dbt.setChecked(True)
        self.radioBtn_dbt.setObjectName("radioBtn_dbt")
        self.gridLayout.addWidget(self.radioBtn_dbt, 1, 8, 1, 1, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.horizontalLayout.addLayout(self.gridLayout)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_2.sizePolicy().hasHeightForWidth())
        self.tab_2.setSizePolicy(sizePolicy)
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_6 = QtWidgets.QLabel(parent=self.tab_2)
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 3, 5, 1, 1)
        self.label_8 = QtWidgets.QLabel(parent=self.tab_2)
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 3, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(parent=self.tab_2)
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 3, 4, 1, 1)
        self.label_4 = QtWidgets.QLabel(parent=self.tab_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 0, 5, 1, 1)
        self.label = QtWidgets.QLabel(parent=self.tab_2)
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 5, 5, 1, 1)
        self.txt_gen_select = QtWidgets.QTextEdit(parent=self.tab_2)
        self.txt_gen_select.setObjectName("txt_gen_select")
        self.gridLayout_3.addWidget(self.txt_gen_select, 0, 0, 6, 5)
        self.label_2 = QtWidgets.QLabel(parent=self.tab_2)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 5, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(parent=self.tab_2)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 3, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(parent=self.tab_2)
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 1, 3, 1, 1)
        self.btn_gen_select = QtWidgets.QPushButton(parent=self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_gen_select.sizePolicy().hasHeightForWidth())
        self.btn_gen_select.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.btn_gen_select.setFont(font)
        self.btn_gen_select.setObjectName("btn_gen_select")
        self.gridLayout_3.addWidget(self.btn_gen_select, 2, 5, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 846, 22))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(parent=self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menu_about = QtGui.QAction(parent=MainWindow)
        self.menu_about.setObjectName("menu_about")
        self.menu.addSeparator()
        self.menu.addAction(self.menu_about)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.tabWidget, self.btn_select_file)
        MainWindow.setTabOrder(self.btn_select_file, self.txt_file_name)
        MainWindow.setTabOrder(self.txt_file_name, self.radioBtn_msql)
        MainWindow.setTabOrder(self.radioBtn_msql, self.radioBtn_psql)
        MainWindow.setTabOrder(self.radioBtn_psql, self.table_file_content)
        MainWindow.setTabOrder(self.table_file_content, self.txt_ddl_content)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TikTools"))
        self.btn_select_file.setText(_translate("MainWindow", "选择文件"))
        self.btn_gen_ddl.setText(_translate("MainWindow", "Gen"))
        self.radioBtn_msql.setText(_translate("MainWindow", "Mysql"))
        self.radioBtn_psql.setText(_translate("MainWindow", "PGSQL"))
        self.txt_ddl_content.setMarkdown(_translate("MainWindow", "**生成步骤： ** \n"
"\n"
"                                         \n"
"\n"
"1、点击 <选择文件> 按钮，打开excel模板文件  \n"
"\n"
"2、点击 <**Gen**> 按钮，生成脚本\n"
"\n"
""))
        self.txt_ddl_content.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Microsoft YaHei UI\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700; color:#ff0000;\">生成步骤： </span> </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">                                         </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1、点击 &lt;<span style=\" color:#aa00ff;\">选择文件</span>&gt; 按钮，打开excel模板文件  </p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2、点击 &lt;<span style=\" font-weight:700; color:#ff0000;\">Gen</span>&gt; 按钮，生成脚本</p></body></html>"))
        self.txt_file_name.setToolTip(_translate("MainWindow", "<html><head/><body><p>excel数据字典文件 </p></body></html>"))
        self.txt_file_name.setText(_translate("MainWindow", "D:\\Desktop\\数据字典模板"))
        self.radioBtn_dbt.setText(_translate("MainWindow", "Dbt"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "1.生成ddl脚本"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:700; color:#ff0000;\">执行步骤：</span><br/>1、在Excel表格里批量生成数据（<span style=\" font-style:italic;\">第一行是</span><span style=\" font-style:italic; color:#ff0000;\">表头</span><span style=\" font-style:italic;\">，其余行是</span><span style=\" font-style:italic; color:#ff0000;\">数据</span>）<br/>2、Ctrl + C ==》剪切板<br/>3、点击&lt;<span style=\" font-weight:700; color:#ff0000;\">Gen</span>&gt;按钮</p></body></html>"))
        self.btn_gen_select.setText(_translate("MainWindow", "Gen"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "2.生成select-union脚本"))
        self.menu.setTitle(_translate("MainWindow", "帮助"))
        self.menu_about.setText(_translate("MainWindow", "关于"))
        self.menu_about.setToolTip(_translate("MainWindow", "<html><head/><body><p>关于</p><p>fasfasffasdfasdf</p><p><br/></p><p>fdasfasf</p></body></html>"))
