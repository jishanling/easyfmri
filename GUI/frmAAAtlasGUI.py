# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmAAAtlasGUI.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_frmAAAtlas(object):
    def setupUi(self, frmAAAtlas):
        frmAAAtlas.setObjectName("frmAAAtlas")
        frmAAAtlas.resize(757, 459)
        self.btnInFile = QtWidgets.QPushButton(frmAAAtlas)
        self.btnInFile.setGeometry(QtCore.QRect(690, 20, 51, 32))
        self.btnInFile.setObjectName("btnInFile")
        self.label_33 = QtWidgets.QLabel(frmAAAtlas)
        self.label_33.setGeometry(QtCore.QRect(30, 20, 131, 16))
        self.label_33.setObjectName("label_33")
        self.btnOutFile = QtWidgets.QPushButton(frmAAAtlas)
        self.btnOutFile.setGeometry(QtCore.QRect(690, 100, 51, 32))
        self.btnOutFile.setObjectName("btnOutFile")
        self.txtInFile = QtWidgets.QLineEdit(frmAAAtlas)
        self.txtInFile.setGeometry(QtCore.QRect(160, 20, 521, 21))
        self.txtInFile.setText("")
        self.txtInFile.setObjectName("txtInFile")
        self.btnConvert = QtWidgets.QPushButton(frmAAAtlas)
        self.btnConvert.setGeometry(QtCore.QRect(590, 410, 141, 32))
        self.btnConvert.setObjectName("btnConvert")
        self.label_35 = QtWidgets.QLabel(frmAAAtlas)
        self.label_35.setGeometry(QtCore.QRect(30, 100, 111, 16))
        self.label_35.setObjectName("label_35")
        self.txtOutFile = QtWidgets.QLineEdit(frmAAAtlas)
        self.txtOutFile.setGeometry(QtCore.QRect(160, 100, 521, 21))
        self.txtOutFile.setText("")
        self.txtOutFile.setObjectName("txtOutFile")
        self.btnClose = QtWidgets.QPushButton(frmAAAtlas)
        self.btnClose.setGeometry(QtCore.QRect(30, 410, 141, 32))
        self.btnClose.setObjectName("btnClose")
        self.tabWidget = QtWidgets.QTabWidget(frmAAAtlas)
        self.tabWidget.setGeometry(QtCore.QRect(30, 140, 701, 251))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(140, 50, 60, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(140, 90, 60, 16))
        self.label_3.setObjectName("label_3")
        self.txtCol = QtWidgets.QComboBox(self.tab)
        self.txtCol.setGeometry(QtCore.QRect(260, 130, 121, 26))
        self.txtCol.setEditable(True)
        self.txtCol.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.txtCol.setObjectName("txtCol")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(300, 20, 61, 16))
        self.label.setObjectName("label")
        self.txtLabel = QtWidgets.QComboBox(self.tab)
        self.txtLabel.setGeometry(QtCore.QRect(260, 90, 121, 26))
        self.txtLabel.setEditable(True)
        self.txtLabel.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.txtLabel.setObjectName("txtLabel")
        self.txtData = QtWidgets.QComboBox(self.tab)
        self.txtData.setGeometry(QtCore.QRect(260, 50, 121, 26))
        self.txtData.setEditable(True)
        self.txtData.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.txtData.setObjectName("txtData")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(140, 130, 101, 16))
        self.label_6.setObjectName("label_6")
        self.txtImg = QtWidgets.QComboBox(self.tab)
        self.txtImg.setGeometry(QtCore.QRect(260, 170, 121, 26))
        self.txtImg.setEditable(True)
        self.txtImg.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.txtImg.setObjectName("txtImg")
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(140, 170, 101, 16))
        self.label_7.setObjectName("label_7")
        self.cbScale = QtWidgets.QCheckBox(self.tab)
        self.cbScale.setGeometry(QtCore.QRect(490, 190, 191, 20))
        self.cbScale.setChecked(True)
        self.cbScale.setObjectName("cbScale")
        self.txtTeLabel = QtWidgets.QComboBox(self.tab)
        self.txtTeLabel.setGeometry(QtCore.QRect(420, 90, 121, 26))
        self.txtTeLabel.setEditable(True)
        self.txtTeLabel.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.txtTeLabel.setObjectName("txtTeLabel")
        self.txtTeData = QtWidgets.QComboBox(self.tab)
        self.txtTeData.setGeometry(QtCore.QRect(420, 50, 121, 26))
        self.txtTeData.setEditable(True)
        self.txtTeData.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.txtTeData.setObjectName("txtTeData")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(460, 20, 61, 16))
        self.label_4.setObjectName("label_4")
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label_17 = QtWidgets.QLabel(self.tab_3)
        self.label_17.setGeometry(QtCore.QRect(30, 30, 60, 16))
        self.label_17.setObjectName("label_17")
        self.txtFoldTo = QtWidgets.QSpinBox(self.tab_3)
        self.txtFoldTo.setGeometry(QtCore.QRect(260, 30, 80, 24))
        self.txtFoldTo.setMaximum(100000)
        self.txtFoldTo.setProperty("value", 1)
        self.txtFoldTo.setObjectName("txtFoldTo")
        self.txtFoldFrom = QtWidgets.QSpinBox(self.tab_3)
        self.txtFoldFrom.setGeometry(QtCore.QRect(90, 30, 80, 24))
        self.txtFoldFrom.setMaximum(100000)
        self.txtFoldFrom.setProperty("value", 1)
        self.txtFoldFrom.setObjectName("txtFoldFrom")
        self.label_44 = QtWidgets.QLabel(self.tab_3)
        self.label_44.setGeometry(QtCore.QRect(200, 30, 60, 16))
        self.label_44.setObjectName("label_44")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.txtAtlas = QtWidgets.QLineEdit(frmAAAtlas)
        self.txtAtlas.setGeometry(QtCore.QRect(160, 60, 521, 21))
        self.txtAtlas.setText("")
        self.txtAtlas.setObjectName("txtAtlas")
        self.btnAtlas = QtWidgets.QPushButton(frmAAAtlas)
        self.btnAtlas.setGeometry(QtCore.QRect(690, 60, 51, 32))
        self.btnAtlas.setObjectName("btnAtlas")
        self.label_34 = QtWidgets.QLabel(frmAAAtlas)
        self.label_34.setGeometry(QtCore.QRect(30, 60, 131, 16))
        self.label_34.setObjectName("label_34")
        self.label_12 = QtWidgets.QLabel(frmAAAtlas)
        self.label_12.setGeometry(QtCore.QRect(190, 410, 391, 20))
        self.label_12.setObjectName("label_12")

        self.retranslateUi(frmAAAtlas)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(frmAAAtlas)
        frmAAAtlas.setTabOrder(self.txtInFile, self.btnInFile)
        frmAAAtlas.setTabOrder(self.btnInFile, self.txtOutFile)
        frmAAAtlas.setTabOrder(self.txtOutFile, self.btnOutFile)
        frmAAAtlas.setTabOrder(self.btnOutFile, self.tabWidget)
        frmAAAtlas.setTabOrder(self.tabWidget, self.txtData)
        frmAAAtlas.setTabOrder(self.txtData, self.txtLabel)
        frmAAAtlas.setTabOrder(self.txtLabel, self.txtCol)
        frmAAAtlas.setTabOrder(self.txtCol, self.btnConvert)
        frmAAAtlas.setTabOrder(self.btnConvert, self.btnClose)

    def retranslateUi(self, frmAAAtlas):
        _translate = QtCore.QCoreApplication.translate
        frmAAAtlas.setWindowTitle(_translate("frmAAAtlas", "Incremental Principal Component Analysis (PCA)"))
        self.btnInFile.setText(_translate("frmAAAtlas", "..."))
        self.label_33.setText(_translate("frmAAAtlas", "Input Data"))
        self.btnOutFile.setText(_translate("frmAAAtlas", "..."))
        self.btnConvert.setText(_translate("frmAAAtlas", "Report"))
        self.label_35.setText(_translate("frmAAAtlas", "Output"))
        self.btnClose.setText(_translate("frmAAAtlas", "Close"))
        self.label_2.setText(_translate("frmAAAtlas", "Data"))
        self.label_3.setText(_translate("frmAAAtlas", "Label"))
        self.label.setText(_translate("frmAAAtlas", "Train"))
        self.label_6.setText(_translate("frmAAAtlas", "Coordinate"))
        self.label_7.setText(_translate("frmAAAtlas", "Image Shape"))
        self.cbScale.setText(_translate("frmAAAtlas", "Scale Data X~N(0,1)"))
        self.label_4.setText(_translate("frmAAAtlas", "Test"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("frmAAAtlas", "Data"))
        self.label_17.setText(_translate("frmAAAtlas", "From:"))
        self.label_44.setText(_translate("frmAAAtlas", "To:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("frmAAAtlas", "Fold"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("frmAAAtlas", "Model"))
        self.btnAtlas.setText(_translate("frmAAAtlas", "..."))
        self.label_34.setText(_translate("frmAAAtlas", "Atlas"))
        self.label_12.setText(_translate("frmAAAtlas", "$FOLD$ will be replaced by fold number."))

