# Form implementation generated from reading ui file 'final.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(967, 1080)
        Form.setMinimumSize(QtCore.QSize(800, 700))
        Form.setMaximumSize(QtCore.QSize(1920, 1080))
        self.frame = QtWidgets.QFrame(parent=Form)
        self.frame.setGeometry(QtCore.QRect(0, 0, 150, 1081))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(243, 237, 247))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(249, 246, 251))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(121, 118, 123))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(162, 158, 165))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(243, 237, 247))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(249, 246, 251))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(243, 237, 247))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(249, 246, 251))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(121, 118, 123))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(162, 158, 165))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(243, 237, 247))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(249, 246, 251))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(121, 118, 123))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(243, 237, 247))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(249, 246, 251))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(121, 118, 123))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(162, 158, 165))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(121, 118, 123))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(121, 118, 123))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(243, 237, 247))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(243, 237, 247))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(243, 237, 247))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.ToolTipText, brush)
        self.frame.setPalette(palette)
        self.frame.setAutoFillBackground(True)
        self.frame.setObjectName("frame")
        self.CreateDumpPage = QtWidgets.QPushButton(parent=self.frame)
        self.CreateDumpPage.setGeometry(QtCore.QRect(0, 20, 150, 70))
        self.CreateDumpPage.setAutoFillBackground(False)
        self.CreateDumpPage.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../icons/make.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.CreateDumpPage.setIcon(icon)
        self.CreateDumpPage.setIconSize(QtCore.QSize(150, 70))
        self.CreateDumpPage.setAutoDefault(False)
        self.CreateDumpPage.setDefault(False)
        self.CreateDumpPage.setFlat(True)
        self.CreateDumpPage.setObjectName("CreateDumpPage")
        self.LoadDumpPage = QtWidgets.QPushButton(parent=self.frame)
        self.LoadDumpPage.setGeometry(QtCore.QRect(0, 120, 150, 70))
        self.LoadDumpPage.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../icons/load.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.LoadDumpPage.setIcon(icon1)
        self.LoadDumpPage.setIconSize(QtCore.QSize(150, 70))
        self.LoadDumpPage.setFlat(True)
        self.LoadDumpPage.setObjectName("LoadDumpPage")
        self.WatchDumpPage = QtWidgets.QPushButton(parent=self.frame)
        self.WatchDumpPage.setGeometry(QtCore.QRect(0, 220, 150, 70))
        self.WatchDumpPage.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../icons/show.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.WatchDumpPage.setIcon(icon2)
        self.WatchDumpPage.setIconSize(QtCore.QSize(150, 70))
        self.WatchDumpPage.setFlat(True)
        self.WatchDumpPage.setObjectName("WatchDumpPage")
        self.ConsoleButton = QtWidgets.QPushButton(parent=self.frame)
        self.ConsoleButton.setGeometry(QtCore.QRect(0, 320, 150, 70))
        self.ConsoleButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../icons/console.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.ConsoleButton.setIcon(icon3)
        self.ConsoleButton.setIconSize(QtCore.QSize(150, 70))
        self.ConsoleButton.setFlat(True)
        self.ConsoleButton.setObjectName("ConsoleButton")
        self.OptionsButton = QtWidgets.QPushButton(parent=self.frame)
        self.OptionsButton.setGeometry(QtCore.QRect(0, 1000, 150, 70))
        self.OptionsButton.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../icons/settings.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.OptionsButton.setIcon(icon4)
        self.OptionsButton.setIconSize(QtCore.QSize(150, 70))
        self.OptionsButton.setFlat(True)
        self.OptionsButton.setObjectName("OptionsButton")
        self.stackedWidget = QtWidgets.QStackedWidget(parent=Form)
        self.stackedWidget.setGeometry(QtCore.QRect(150, 0, 1831, 1081))
        self.stackedWidget.setObjectName("stackedWidget")
        self.mainWindow = QtWidgets.QWidget()
        self.mainWindow.setObjectName("mainWindow")
        self.textEdit = QtWidgets.QTextEdit(parent=self.mainWindow)
        self.textEdit.setGeometry(QtCore.QRect(60, 260, 691, 261))
        self.textEdit.setObjectName("textEdit")
        self.stackedWidget.addWidget(self.mainWindow)
        self.CreateDump = QtWidgets.QWidget()
        self.CreateDump.setObjectName("CreateDump")
        self.widget_2 = QtWidgets.QWidget(parent=self.CreateDump)
        self.widget_2.setGeometry(QtCore.QRect(30, 250, 761, 120))
        self.widget_2.setObjectName("widget_2")
        self.textBrowser = QtWidgets.QTextBrowser(parent=self.widget_2)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 751, 51))
        self.textBrowser.setObjectName("textBrowser")
        self.continueCreateDumpButton = QtWidgets.QPushButton(parent=self.widget_2)
        self.continueCreateDumpButton.setGeometry(QtCore.QRect(440, 60, 311, 51))
        self.continueCreateDumpButton.setAutoFillBackground(False)
        self.continueCreateDumpButton.setStyleSheet("border-radius: 20px;   \n"
"font: 34pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(101, 85, 143);")
        self.continueCreateDumpButton.setObjectName("continueCreateDumpButton")
        self.openFolderButton = QtWidgets.QPushButton(parent=self.widget_2)
        self.openFolderButton.setGeometry(QtCore.QRect(370, 60, 50, 50))
        self.openFolderButton.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("../icons/Folders.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.openFolderButton.setIcon(icon5)
        self.openFolderButton.setIconSize(QtCore.QSize(50, 50))
        self.openFolderButton.setFlat(True)
        self.openFolderButton.setObjectName("openFolderButton")
        self.textBrowser_2 = QtWidgets.QTextBrowser(parent=self.widget_2)
        self.textBrowser_2.setGeometry(QtCore.QRect(0, 60, 361, 41))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.stackedWidget.addWidget(self.CreateDump)
        self.DownloadDumpPage = QtWidgets.QWidget()
        self.DownloadDumpPage.setObjectName("DownloadDumpPage")
        self.widget_3 = QtWidgets.QWidget(parent=self.DownloadDumpPage)
        self.widget_3.setGeometry(QtCore.QRect(30, 250, 761, 120))
        self.widget_3.setObjectName("widget_3")
        self.textBrowser_3 = QtWidgets.QTextBrowser(parent=self.widget_3)
        self.textBrowser_3.setGeometry(QtCore.QRect(0, 0, 751, 51))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.continueCreateDumpButton_2 = QtWidgets.QPushButton(parent=self.widget_3)
        self.continueCreateDumpButton_2.setGeometry(QtCore.QRect(440, 60, 311, 51))
        self.continueCreateDumpButton_2.setAutoFillBackground(False)
        self.continueCreateDumpButton_2.setStyleSheet("border-radius: 20px;   \n"
"background-color: rgb(101, 85, 143);\n"
"font: 34pt \"MS Shell Dlg 2\";")
        self.continueCreateDumpButton_2.setObjectName("continueCreateDumpButton_2")
        self.openFolderButton_2 = QtWidgets.QPushButton(parent=self.widget_3)
        self.openFolderButton_2.setGeometry(QtCore.QRect(370, 60, 50, 50))
        self.openFolderButton_2.setText("")
        self.openFolderButton_2.setIcon(icon5)
        self.openFolderButton_2.setIconSize(QtCore.QSize(50, 50))
        self.openFolderButton_2.setFlat(True)
        self.openFolderButton_2.setObjectName("openFolderButton_2")
        self.textBrowser_4 = QtWidgets.QTextBrowser(parent=self.widget_3)
        self.textBrowser_4.setGeometry(QtCore.QRect(0, 60, 361, 41))
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.stackedWidget.addWidget(self.DownloadDumpPage)
        self.CheckDumpPage = QtWidgets.QWidget()
        self.CheckDumpPage.setObjectName("CheckDumpPage")
        self.browserLabel = QtWidgets.QLabel(parent=self.CheckDumpPage)
        self.browserLabel.setGeometry(QtCore.QRect(290, 40, 181, 41))
        self.browserLabel.setStyleSheet("background-color: rgb(101, 85, 143);\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"border-radius: 20px;   \n"
"background-color: rgb(101, 85, 143);")
        self.browserLabel.setObjectName("browserLabel")
        self.historyTreeWidget = QtWidgets.QTreeWidget(parent=self.CheckDumpPage)
        self.historyTreeWidget.setGeometry(QtCore.QRect(70, 140, 651, 851))
        self.historyTreeWidget.setStyleSheet("")
        self.historyTreeWidget.setObjectName("historyTreeWidget")
        self.browserComboBox = QtWidgets.QComboBox(parent=self.CheckDumpPage)
        self.browserComboBox.setGeometry(QtCore.QRect(290, 90, 181, 41))
        self.browserComboBox.setStyleSheet("border-radius: 20px;   \n"
"")
        self.browserComboBox.setObjectName("browserComboBox")
        self.horizontalScrollBar = QtWidgets.QScrollBar(parent=self.CheckDumpPage)
        self.horizontalScrollBar.setGeometry(QtCore.QRect(80, 970, 631, 16))
        self.horizontalScrollBar.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.horizontalScrollBar.setObjectName("horizontalScrollBar")
        self.stackedWidget.addWidget(self.CheckDumpPage)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.textEdit.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:36pt;\">Тут пока пусто.<br /></span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:28pt;\">Загрузите дамп для анализа, чтобы продолжить работу или создайте новый дамп.</span></p></body></html>"))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">Выберите путь для сохранения дампа.</span></p></body></html>"))
        self.continueCreateDumpButton.setText(_translate("Form", "Продолжить"))
        self.textBrowser_2.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; color:#7d7d7d;\">Не выбрано</span></p></body></html>"))
        self.textBrowser_3.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">Выберите дамп, который необходимо открыть.</span></p></body></html>"))
        self.continueCreateDumpButton_2.setText(_translate("Form", "Продолжить"))
        self.textBrowser_4.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; color:#7d7d7d;\">Не выбрано</span></p></body></html>"))
        self.browserLabel.setText(_translate("Form", "  Выберите браузер"))
