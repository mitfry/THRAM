
#!/usr/bin/env python
__author__ = 'Mitchell'

# IPFIT5 imports
# Built-in
import sys
import time
from PyQt4.QtGui import QTreeWidgetItem

# Add folder "functions" to the locations to import from
sys.path.append(sys.path[0]+"/../functions")

# Custom
import Software
import Hardware
import Hash
import Cloud

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Development\School\IPFIT5_2015\Source\Gui\gui_maken\interface_thram.ui'
#
# Created: Fri Jun 12 12:39:41 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)
        self._active = False
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(960, 550)
        MainWindow.setMinimumSize(QtCore.QSize(960, 0))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Logo/THRAM_Logo_Geen_Tekst.PNG")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_3 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.tab_Menu = QtGui.QTabWidget(self.centralwidget)
        self.tab_Menu.setEnabled(True)
        self.tab_Menu.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.tab_Menu.setObjectName(_fromUtf8("tab_Menu"))
        self.tab_Project = QtGui.QWidget()
        self.tab_Project.setObjectName(_fromUtf8("tab_Project"))
        self.gridLayout_6 = QtGui.QGridLayout(self.tab_Project)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.btn_Test = QtGui.QPushButton(self.tab_Project)
        self.btn_Test.setObjectName(_fromUtf8("btn_Test"))
        self.gridLayout_6.addWidget(self.btn_Test, 0, 0, 1, 1)
        self.btn_Progressbar = QtGui.QPushButton(self.tab_Project)
        self.btn_Progressbar.setObjectName(_fromUtf8("btn_Progressbar"))
        self.gridLayout_6.addWidget(self.btn_Progressbar, 1, 0, 1, 1)
        self.tab_Menu.addTab(self.tab_Project, _fromUtf8(""))
        self.tab_System = QtGui.QWidget()
        self.tab_System.setObjectName(_fromUtf8("tab_System"))
        self.gridLayout_2 = QtGui.QGridLayout(self.tab_System)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.btn_Hardware = QtGui.QPushButton(self.tab_System)
        self.btn_Hardware.setObjectName(_fromUtf8("btn_Hardware"))
        self.gridLayout_2.addWidget(self.btn_Hardware, 0, 0, 1, 1)
        self.tab_Menu.addTab(self.tab_System, _fromUtf8(""))
        self.tab_Software = QtGui.QWidget()
        self.tab_Software.setObjectName(_fromUtf8("tab_Software"))
        self.gridLayout = QtGui.QGridLayout(self.tab_Software)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.btn_Processen = QtGui.QPushButton(self.tab_Software)
        self.btn_Processen.setObjectName(_fromUtf8("btn_Processen"))
        self.gridLayout.addWidget(self.btn_Processen, 0, 0, 1, 1)
        self.btn_Services = QtGui.QPushButton(self.tab_Software)
        self.btn_Services.setObjectName(_fromUtf8("btn_Services"))
        self.gridLayout.addWidget(self.btn_Services, 0, 1, 1, 1)
        self.btn_Software = QtGui.QPushButton(self.tab_Software)
        self.btn_Software.setObjectName(_fromUtf8("btn_Software"))
        self.gridLayout.addWidget(self.btn_Software, 0, 2, 1, 1)
        self.btn_Cloud = QtGui.QPushButton(self.tab_Software)
        self.btn_Cloud.setObjectName(_fromUtf8("btn_Cloud"))
        self.gridLayout.addWidget(self.btn_Cloud, 0, 3, 1, 1)
        self.treew_Software = QtGui.QTreeWidget(self.tab_Software)
        self.treew_Software.setAlternatingRowColors(False)
        self.treew_Software.setObjectName(_fromUtf8("treew_Software"))
        self.gridLayout.addWidget(self.treew_Software, 1, 0, 1, 4)
        self.tab_Menu.addTab(self.tab_Software, _fromUtf8(""))
        self.tab_Internet = QtGui.QWidget()
        self.tab_Internet.setObjectName(_fromUtf8("tab_Internet"))
        self.gridLayout_5 = QtGui.QGridLayout(self.tab_Internet)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.chk_Mozilla_FireFox = QtGui.QCheckBox(self.tab_Internet)
        self.chk_Mozilla_FireFox.setObjectName(_fromUtf8("chk_Mozilla_FireFox"))
        self.gridLayout_5.addWidget(self.chk_Mozilla_FireFox, 2, 0, 1, 1)
        self.btn_Load_Internet_History = QtGui.QPushButton(self.tab_Internet)
        self.btn_Load_Internet_History.setObjectName(_fromUtf8("btn_Load_Internet_History"))
        self.gridLayout_5.addWidget(self.btn_Load_Internet_History, 6, 0, 1, 1)
        self.lbl_Search_Internet_History = QtGui.QLabel(self.tab_Internet)
        self.lbl_Search_Internet_History.setObjectName(_fromUtf8("lbl_Search_Internet_History"))
        self.gridLayout_5.addWidget(self.lbl_Search_Internet_History, 0, 4, 1, 1)
        self.chk_Internet_History_Search_Capital_Letter = QtGui.QCheckBox(self.tab_Internet)
        self.chk_Internet_History_Search_Capital_Letter.setObjectName(_fromUtf8("chk_Internet_History_Search_Capital_Letter"))
        self.gridLayout_5.addWidget(self.chk_Internet_History_Search_Capital_Letter, 1, 4, 1, 1)
        self.lbl_Internet_History_Amount = QtGui.QLabel(self.tab_Internet)
        self.lbl_Internet_History_Amount.setObjectName(_fromUtf8("lbl_Internet_History_Amount"))
        self.gridLayout_5.addWidget(self.lbl_Internet_History_Amount, 1, 3, 1, 1)
        self.chk_Internet_Explorer = QtGui.QCheckBox(self.tab_Internet)
        self.chk_Internet_Explorer.setObjectName(_fromUtf8("chk_Internet_Explorer"))
        self.gridLayout_5.addWidget(self.chk_Internet_Explorer, 1, 0, 1, 1)
        self.btn_Show_Internet_History = QtGui.QPushButton(self.tab_Internet)
        self.btn_Show_Internet_History.setObjectName(_fromUtf8("btn_Show_Internet_History"))
        self.gridLayout_5.addWidget(self.btn_Show_Internet_History, 6, 3, 1, 1)
        self.btn_Search_Internet_History = QtGui.QPushButton(self.tab_Internet)
        self.btn_Search_Internet_History.setObjectName(_fromUtf8("btn_Search_Internet_History"))
        self.gridLayout_5.addWidget(self.btn_Search_Internet_History, 6, 4, 1, 1)
        self.lbl_Internet_History_Most_Visited = QtGui.QLabel(self.tab_Internet)
        self.lbl_Internet_History_Most_Visited.setObjectName(_fromUtf8("lbl_Internet_History_Most_Visited"))
        self.gridLayout_5.addWidget(self.lbl_Internet_History_Most_Visited, 0, 3, 1, 1)
        self.lbl_Browsers = QtGui.QLabel(self.tab_Internet)
        self.lbl_Browsers.setMinimumSize(QtCore.QSize(298, 0))
        self.lbl_Browsers.setObjectName(_fromUtf8("lbl_Browsers"))
        self.gridLayout_5.addWidget(self.lbl_Browsers, 0, 0, 1, 1)
        self.txt_Internet_History_Search = QtGui.QLineEdit(self.tab_Internet)
        self.txt_Internet_History_Search.setObjectName(_fromUtf8("txt_Internet_History_Search"))
        self.gridLayout_5.addWidget(self.txt_Internet_History_Search, 2, 4, 1, 1)
        self.treeWidget = QtGui.QTreeWidget(self.tab_Internet)
        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))
        self.gridLayout_5.addWidget(self.treeWidget, 7, 0, 1, 5)
        self.chk_Google_Chrome = QtGui.QCheckBox(self.tab_Internet)
        self.chk_Google_Chrome.setObjectName(_fromUtf8("chk_Google_Chrome"))
        self.gridLayout_5.addWidget(self.chk_Google_Chrome, 3, 0, 1, 1)
        self.txt_Internet_History_Amount = QtGui.QLineEdit(self.tab_Internet)
        self.txt_Internet_History_Amount.setObjectName(_fromUtf8("txt_Internet_History_Amount"))
        self.gridLayout_5.addWidget(self.txt_Internet_History_Amount, 2, 3, 1, 1)
        self.tab_Menu.addTab(self.tab_Internet, _fromUtf8(""))
        self.tab_Email = QtGui.QWidget()
        self.tab_Email.setObjectName(_fromUtf8("tab_Email"))
        self.gridLayout_4 = QtGui.QGridLayout(self.tab_Email)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.btn_Email = QtGui.QPushButton(self.tab_Email)
        self.btn_Email.setObjectName(_fromUtf8("btn_Email"))
        self.gridLayout_4.addWidget(self.btn_Email, 0, 0, 1, 1)
        self.tab_Menu.addTab(self.tab_Email, _fromUtf8(""))
        self.tab_Files = QtGui.QWidget()
        self.tab_Files.setObjectName(_fromUtf8("tab_Files"))
        self.gridLayout_7 = QtGui.QGridLayout(self.tab_Files)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.txt_Live_Search = QtGui.QLineEdit(self.tab_Files)
        self.txt_Live_Search.setObjectName(_fromUtf8("txt_Live_Search"))
        self.gridLayout_7.addWidget(self.txt_Live_Search, 5, 0, 1, 1)
        self.btn_Hash = QtGui.QPushButton(self.tab_Files)
        self.btn_Hash.setEnabled(False)
        self.btn_Hash.setObjectName(_fromUtf8("btn_Hash"))
        self.gridLayout_7.addWidget(self.btn_Hash, 6, 0, 1, 1)
        self.treew_Bestanden = QtGui.QTreeWidget(self.tab_Files)
        self.treew_Bestanden.setEnabled(True)
        self.treew_Bestanden.setAutoFillBackground(False)
        self.treew_Bestanden.setAutoScroll(True)
        self.treew_Bestanden.setTabKeyNavigation(False)
        self.treew_Bestanden.setAlternatingRowColors(True)
        self.treew_Bestanden.setObjectName(_fromUtf8("treew_Bestanden"))
        self.treew_Bestanden.header().setCascadingSectionResizes(True)
        self.treew_Bestanden.header().setDefaultSectionSize(100)
        self.treew_Bestanden.header().setHighlightSections(True)
        self.treew_Bestanden.header().setSortIndicatorShown(True)
        self.gridLayout_7.addWidget(self.treew_Bestanden, 7, 0, 1, 1)
        self.btn_Search_From = QtGui.QPushButton(self.tab_Files)
        self.btn_Search_From.setCheckable(False)
        self.btn_Search_From.setObjectName(_fromUtf8("btn_Search_From"))
        self.gridLayout_7.addWidget(self.btn_Search_From, 1, 0, 1, 1)
        self.info_Search_From = QtGui.QLabel(self.tab_Files)
        self.info_Search_From.setObjectName(_fromUtf8("info_Search_From"))
        self.gridLayout_7.addWidget(self.info_Search_From, 2, 0, 1, 1)
        self.lbl_Live_Search = QtGui.QLabel(self.tab_Files)
        self.lbl_Live_Search.setObjectName(_fromUtf8("lbl_Live_Search"))
        self.gridLayout_7.addWidget(self.lbl_Live_Search, 4, 0, 1, 1)
        self.show_Search_From = QtGui.QLineEdit(self.tab_Files)
        self.show_Search_From.setEnabled(False)
        self.show_Search_From.setObjectName(_fromUtf8("show_Search_From"))
        self.gridLayout_7.addWidget(self.show_Search_From, 3, 0, 1, 1)
        self.tab_Menu.addTab(self.tab_Files, _fromUtf8(""))
        self.gridLayout_3.addWidget(self.tab_Menu, 2, 0, 1, 1)
        self.progressBar = QtGui.QProgressBar(self.centralwidget)
        self.progressBar.setMouseTracking(False)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.gridLayout_3.addWidget(self.progressBar, 3, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 960, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuBestand = QtGui.QMenu(self.menubar)
        self.menuBestand.setObjectName(_fromUtf8("menuBestand"))
        self.menuOpties = QtGui.QMenu(self.menubar)
        self.menuOpties.setObjectName(_fromUtf8("menuOpties"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setEnabled(True)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionNieuw = QtGui.QAction(MainWindow)
        self.actionNieuw.setObjectName(_fromUtf8("actionNieuw"))
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionOpslaan = QtGui.QAction(MainWindow)
        self.actionOpslaan.setObjectName(_fromUtf8("actionOpslaan"))
        self.actionFuncties = QtGui.QAction(MainWindow)
        self.actionFuncties.setObjectName(_fromUtf8("actionFuncties"))
        self.actionInfo = QtGui.QAction(MainWindow)
        self.actionInfo.setObjectName(_fromUtf8("actionInfo"))
        self.actionTechnical_manual = QtGui.QAction(MainWindow)
        self.actionTechnical_manual.setObjectName(_fromUtf8("actionTechnical_manual"))
        self.actionOver = QtGui.QAction(MainWindow)
        self.actionOver.setObjectName(_fromUtf8("actionOver"))
        self.menuBestand.addAction(self.actionNieuw)
        self.menuBestand.addAction(self.actionOpen)
        self.menuBestand.addAction(self.actionOpslaan)
        self.menuOpties.addAction(self.actionFuncties)
        self.menuHelp.addAction(self.actionInfo)
        self.menuHelp.addAction(self.actionTechnical_manual)
        self.menuHelp.addAction(self.actionOver)
        self.menubar.addAction(self.menuBestand.menuAction())
        self.menubar.addAction(self.menuOpties.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tab_Menu.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "THRAM - The Ultimate Triage Solution", None))
        self.btn_Test.setText(_translate("MainWindow", "Test mijn functie", None))
        self.btn_Progressbar.setText(_translate("MainWindow", "Start", None))
        self.tab_Menu.setTabText(self.tab_Menu.indexOf(self.tab_Project), _translate("MainWindow", "Project", None))
        self.btn_Hardware.setText(_translate("MainWindow", "Hardware Info", None))
        self.tab_Menu.setTabText(self.tab_Menu.indexOf(self.tab_System), _translate("MainWindow", "Systeem", None))
        self.btn_Processen.setText(_translate("MainWindow", "Processen", None))
        self.btn_Services.setText(_translate("MainWindow", "Services", None))
        self.btn_Software.setText(_translate("MainWindow", "Software", None))
        self.btn_Cloud.setText(_translate("MainWindow", "Cloud", None))
        self.treew_Software.headerItem().setText(0, _translate("MainWindow", " ", None))
        self.treew_Software.headerItem().setText(1, _translate("MainWindow", " ", None))
        self.treew_Software.headerItem().setText(2, _translate("MainWindow", " ", None))
        self.treew_Software.headerItem().setText(3, _translate("MainWindow", " ", None))
        self.treew_Software.headerItem().setText(4, _translate("MainWindow", " ", None))
        self.treew_Software.headerItem().setText(5, _translate("MainWindow", " ", None))
        self.treew_Software.headerItem().setText(6, _translate("MainWindow", " ", None))
        self.treew_Software.headerItem().setText(7, _translate("MainWindow", " ", None))
        self.treew_Software.headerItem().setText(8, _translate("MainWindow", " ", None))
        self.treew_Software.headerItem().setText(9, _translate("MainWindow", " ", None))
        self.tab_Menu.setTabText(self.tab_Menu.indexOf(self.tab_Software), _translate("MainWindow", "Software", None))
        self.chk_Mozilla_FireFox.setText(_translate("MainWindow", "Mozilla FireFox", None))
        self.btn_Load_Internet_History.setText(_translate("MainWindow", "Load data", None))
        self.lbl_Search_Internet_History.setText(_translate("MainWindow", "Zoeken", None))
        self.chk_Internet_History_Search_Capital_Letter.setText(_translate("MainWindow", "Hoofdletter gevoelig", None))
        self.lbl_Internet_History_Amount.setText(_translate("MainWindow", "Aantal:", None))
        self.chk_Internet_Explorer.setText(_translate("MainWindow", "Internet Explorer", None))
        self.btn_Show_Internet_History.setText(_translate("MainWindow", "Internetgeschiedenis tonen", None))
        self.btn_Search_Internet_History.setText(_translate("MainWindow", "Zoeken", None))
        self.lbl_Internet_History_Most_Visited.setText(_translate("MainWindow", "Meest bezocht", None))
        self.lbl_Browsers.setText(_translate("MainWindow", "Browsers", None))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "Browser", None))
        self.treeWidget.headerItem().setText(1, _translate("MainWindow", "Titel", None))
        self.treeWidget.headerItem().setText(2, _translate("MainWindow", "Aantal keer", None))
        self.treeWidget.headerItem().setText(3, _translate("MainWindow", "Laatst bezocht", None))
        self.treeWidget.headerItem().setText(4, _translate("MainWindow", "URL", None))
        self.chk_Google_Chrome.setText(_translate("MainWindow", "Google Chrome", None))
        self.tab_Menu.setTabText(self.tab_Menu.indexOf(self.tab_Internet), _translate("MainWindow", "Internet", None))
        self.btn_Email.setText(_translate("MainWindow", "E-mail", None))
        self.tab_Menu.setTabText(self.tab_Menu.indexOf(self.tab_Email), _translate("MainWindow", "E-mail", None))
        self.btn_Hash.setText(_translate("MainWindow", "Geef een externe doelmap op:", None))
        self.treew_Bestanden.headerItem().setText(0, _translate("MainWindow", "Bestand", None))
        self.treew_Bestanden.headerItem().setText(1, _translate("MainWindow", "Locatie", None))
        self.treew_Bestanden.headerItem().setText(2, _translate("MainWindow", "Hashvorm", None))
        self.treew_Bestanden.headerItem().setText(3, _translate("MainWindow", "Hashwaarde", None))
        self.treew_Bestanden.headerItem().setText(4, _translate("MainWindow", "Bestandsgrootte in kb", None))
        self.treew_Bestanden.headerItem().setText(5, _translate("MainWindow", "Aangepast op", None))
        self.treew_Bestanden.headerItem().setText(6, _translate("MainWindow", "Laatst geopend op", None))
        self.treew_Bestanden.headerItem().setText(7, _translate("MainWindow", "Aangemaakt op", None))
        self.btn_Search_From.setText(_translate("MainWindow", "Geef een hoofdmap op:", None))
        self.info_Search_From.setText(_translate("MainWindow", "U zoekt vanaf:", None))
        self.lbl_Live_Search.setText(_translate("MainWindow", "Zoeken naar:", None))
        self.tab_Menu.setTabText(self.tab_Menu.indexOf(self.tab_Files), _translate("MainWindow", "Bestanden", None))
        self.menuBestand.setTitle(_translate("MainWindow", "Bestand", None))
        self.menuOpties.setTitle(_translate("MainWindow", "Opties", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.actionNieuw.setText(_translate("MainWindow", "Nieuw...", None))
        self.actionOpen.setText(_translate("MainWindow", "Open...", None))
        self.actionOpslaan.setText(_translate("MainWindow", "Opslaan...", None))
        self.actionFuncties.setText(_translate("MainWindow", "Functies", None))
        self.actionInfo.setText(_translate("MainWindow", "Gebruikershandleiding", None))
        self.actionTechnical_manual.setText(_translate("MainWindow", "Technische handleiding", None))
        self.actionOver.setText(_translate("MainWindow", "Over", None))


        # IPFIT5 Buttons, Methods and other code
        self.setWindowTitle(_translate("MainWindow", "THRAM" + u'\u2122' + "- The Ultimate Triage Solution", None))

        # Tab Project:
        self.btn_Test.clicked.connect(self.test_mijn_functie)
        self.btn_Progressbar.clicked.connect(self.update_progress)

        # Tab Systeem:

        # Tab Software:
        self.btn_Processen.clicked.connect(lambda: self.status_bar("Lijst vernieuwen...", 1000))
        self.btn_Processen.clicked.connect(lambda: self.fill_software_treewidget(Software.processes()))
        self.btn_Services.clicked.connect(lambda: self.status_bar("Lijst vernieuwen...", 1000))
        self.btn_Services.clicked.connect(lambda: self.fill_software_treewidget(Software.services()))
        self.btn_Software.clicked.connect(lambda: self.status_bar("Lijst vernieuwen...", 1000))
        self.btn_Software.clicked.connect(lambda: self.fill_software_treewidget(Software.software_installed()))
        self.btn_Software.clicked.connect(lambda: self.status_bar("Lijst vernieuwen...", 1000))
        self.btn_Cloud.clicked.connect(lambda: Cloud.CloudSearch())

        # Tab Internet:

        # Tab E-maail:

        # Tab Bestanden:
        self.btn_Search_From.clicked.connect(lambda: self.fill_searchbar(Hash.inputfolder()))
        self.btn_Hash.clicked.connect(
            lambda: self.fill_hash_treewidget(Hash.calculate_hash_from_multiplee_files(output_list)))

    def fill_software_treewidget(self, passed_list):
        self.treew_Software.clear()
        passed_list_number = 0

        for title in passed_list[0]:
            self.treew_Software.headerItem().setText(passed_list_number, _translate("MainWindow", title, None))
            passed_list_number += 1

        passed_list_number = 0
        for row in passed_list[1:]:
            item = QTreeWidgetItem()
            for row_nr in range(0, len(row)):
                item.setText(row_nr, unicode(row[row_nr]))

            self.treew_Software.insertTopLevelItem(passed_list_number, item)
            QtGui.qApp.processEvents()
            passed_list_number += 1

    def fill_searchbar(self, output):
        global output_list
        self.show_Search_From.clear()
        self.show_Search_From.insert(str(output))
        self.btn_Hash.setEnabled(True)
        output_list = output

    def fill_hash_treewidget(self, passed_list):
        self.treew_Bestanden.clear()
        for row in passed_list:
            row_number = 0
            item = QTreeWidgetItem()
            while row_number < 8:
                item.setText(row_number, unicode(row[row_number]))
                self.treew_Bestanden.insertTopLevelItem(row_number, item)
                row_number += 1
            QtGui.qApp.processEvents()

    def update_progress(self):
        if not self._active:
            self._active = True
            self.btn_Progressbar.setText('Stop')
            if self.progressBar.value() == self.progressBar.maximum():
                self.progressBar.reset()
            QtCore.QTimer.singleShot(0, self.startLoop)
        else:
            self._active = False

    def closeEvent(self, event):
        self._active = False

    def startLoop(self):
        while True:
            time.sleep(0.05)
            value = self.progressBar.value() + 1
            self.progressBar.setValue(value)
            QtGui.qApp.processEvents()
            if (not self._active or
                        value >= self.progressBar.maximum()):
                break
        self.btn_Progressbar.setText('Start')
        self._active = False

    # Het is niet te geloven dames!

    global x
    x = 0

    def status_bar(self, message, time_in_mills):
        self.statusbar.showMessage(message, time_in_mills)

    def test_mijn_functie(self):
        global x
        if x < 2:
            print "Pauper"
        elif x < 5:
            print "Pauperr!"
        elif x < 9:
            print "Wat klik je nou nog?!"
        elif x < 12:
            print "Noob alert: Application soon exiting..."
            for i in range(0, 5):
                i = 5 - i
                self.status_bar("Exiting in: " + str(i) + " seconds... =3", 0)
                time.sleep(1)

            print "Laatsnorr.."
            self.status_bar("Laatsnorr...", 0)
            time.sleep(1)
            sys.exit()
        x += 1

# IPFIT5 constructor
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    ex = Ui_MainWindow()
    ex.show()

    # Starting threads for generating information
    Software.WorkerThread().start()

    sys.exit(app.exec_())
