# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_windows.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 626)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.findEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.findEdit.setObjectName("findEdit")
        self.horizontalLayout.addWidget(self.findEdit)
        self.btnRefresh = QtWidgets.QToolButton(self.centralwidget)
        icon=QtGui.QIcon("view-refresh.png")
        self.btnRefresh.setIcon(icon)
        self.btnRefresh.setObjectName("btnRefresh")
        self.horizontalLayout.addWidget(self.btnRefresh)
        self.btnSettings = QtWidgets.QToolButton(self.centralwidget)
        icon = QtGui.QIcon("preferences-system.png")
        self.btnSettings.setIcon(icon)
        self.btnSettings.setObjectName("btnSettings")
        self.horizontalLayout.addWidget(self.btnSettings)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        self.treeWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        sizePolicy.setHeightForWidth(self.treeWidget.sizePolicy().hasHeightForWidth())
        self.treeWidget.setSizePolicy(sizePolicy)
        self.treeWidget.setMouseTracking(True)
        self.treeWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.treeWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.treeWidget.setProperty("showDropIndicator", False)
        self.treeWidget.setAlternatingRowColors(False)
        self.treeWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.treeWidget.setRootIsDecorated(False)
        self.treeWidget.setUniformRowHeights(False)
        self.treeWidget.setItemsExpandable(False)
        self.treeWidget.setColumnCount(5)
        self.treeWidget.setObjectName("treeWidget")
        # self.treeWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0.setCheckState(0, QtCore.Qt.Checked)
        self.treeWidget.header().setVisible(True)
        self.treeWidget.header().setStretchLastSection(False)
        self.treeWidget.header().setSectionResizeMode(QtWidgets.QHeaderView.Interactive)
        self.verticalLayout.addWidget(self.treeWidget)
        # self.EditNew = QtWidgets.QLineEdit(self.centralwidget)
        self.EditNew = QtWidgets.QLineEdit(self.centralwidget)
        self.EditNew.setObjectName("EditNew")
        self.verticalLayout.addWidget(self.EditNew)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionConfiguracion = QtWidgets.QAction(MainWindow)
        self.actionConfiguracion.setCheckable(True)
        self.treeWidget.setColumnWidth(0,18)
        self.treeWidget.setColumnWidth(1,400)
        self.treeWidget.sortByColumn(1,QtCore.Qt.AscendingOrder)
        self.actionConfiguracion.setObjectName("actionConfiguracion")
        self.findEdit.setClearButtonEnabled(True)
        icon = QtGui.QIcon("icon.png")
        MainWindow.setWindowIcon(icon)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Todoxt"))
        self.label.setText(_translate("MainWindow", "Find"))
        self.btnRefresh.setText(_translate("MainWindow", "..."))
        self.btnRefresh.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.btnSettings.setText(_translate("MainWindow", "..."))
        self.btnSettings.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.treeWidget.setSortingEnabled(True)
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", ""))
        self.treeWidget.headerItem().setText(1, _translate("MainWindow", "Todo"))
        self.treeWidget.headerItem().setText(2, _translate("MainWindow", "Creation date"))
        self.treeWidget.headerItem().setText(3, _translate("MainWindow", "Context"))
        self.treeWidget.headerItem().setText(4, _translate("MainWindow", "Project"))
        self.actionConfiguracion.setText(_translate("MainWindow", "Configuration"))



class customQtTreeWidgetItem(QtWidgets.QTreeWidgetItem):

    def __init__(self, todo):
        super(customQtTreeWidgetItem, self).__init__()
        self._todo = todo


import resource
