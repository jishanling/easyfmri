# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmMAClassicNetworkGUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_frmMAClassicNetwork(object):
    def setupUi(self, frmMAClassicNetwork):
        frmMAClassicNetwork.setObjectName("frmMAClassicNetwork")
        frmMAClassicNetwork.resize(782, 636)
        self.btnInFile = QtWidgets.QPushButton(frmMAClassicNetwork)
        self.btnInFile.setGeometry(QtCore.QRect(710, 20, 51, 32))
        self.btnInFile.setObjectName("btnInFile")
        self.label_33 = QtWidgets.QLabel(frmMAClassicNetwork)
        self.label_33.setGeometry(QtCore.QRect(30, 20, 211, 16))
        self.label_33.setObjectName("label_33")
        self.txtInFile = QtWidgets.QLineEdit(frmMAClassicNetwork)
        self.txtInFile.setGeometry(QtCore.QRect(180, 20, 521, 21))
        self.txtInFile.setText("")
        self.txtInFile.setObjectName("txtInFile")
        self.btnConvert = QtWidgets.QPushButton(frmMAClassicNetwork)
        self.btnConvert.setGeometry(QtCore.QRect(620, 590, 141, 32))
        self.btnConvert.setObjectName("btnConvert")
        self.btnClose = QtWidgets.QPushButton(frmMAClassicNetwork)
        self.btnClose.setGeometry(QtCore.QRect(30, 590, 141, 32))
        self.btnClose.setObjectName("btnClose")
        self.tabWidget = QtWidgets.QTabWidget(frmMAClassicNetwork)
        self.tabWidget.setGeometry(QtCore.QRect(30, 170, 731, 401))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(20, 50, 151, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(20, 90, 141, 16))
        self.label_3.setObjectName("label_3")
        self.txtLabel = QtWidgets.QComboBox(self.tab)
        self.txtLabel.setGeometry(QtCore.QRect(210, 90, 181, 26))
        self.txtLabel.setEditable(True)
        self.txtLabel.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.txtLabel.setObjectName("txtLabel")
        self.txtData = QtWidgets.QComboBox(self.tab)
        self.txtData.setGeometry(QtCore.QRect(210, 50, 181, 26))
        self.txtData.setEditable(True)
        self.txtData.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.txtData.setObjectName("txtData")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(290, 10, 51, 17))
        self.label.setObjectName("label")
        self.label_31 = QtWidgets.QLabel(self.tab)
        self.label_31.setGeometry(QtCore.QRect(20, 130, 181, 16))
        self.label_31.setObjectName("label_31")
        self.txtCond = QtWidgets.QComboBox(self.tab)
        self.txtCond.setGeometry(QtCore.QRect(210, 130, 181, 26))
        self.txtCond.setEditable(True)
        self.txtCond.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.txtCond.setObjectName("txtCond")
        self.lblImgShape = QtWidgets.QLabel(self.tab)
        self.lblImgShape.setGeometry(QtCore.QRect(440, 50, 271, 20))
        self.lblImgShape.setObjectName("lblImgShape")
        self.label_32 = QtWidgets.QLabel(self.tab)
        self.label_32.setGeometry(QtCore.QRect(20, 170, 131, 16))
        self.label_32.setObjectName("label_32")
        self.txtCoord = QtWidgets.QComboBox(self.tab)
        self.txtCoord.setGeometry(QtCore.QRect(210, 170, 181, 26))
        self.txtCoord.setEditable(True)
        self.txtCoord.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.txtCoord.setObjectName("txtCoord")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.groupBox = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox.setGeometry(QtCore.QRect(30, 10, 671, 71))
        self.groupBox.setObjectName("groupBox")
        self.cbScale = QtWidgets.QCheckBox(self.groupBox)
        self.cbScale.setGeometry(QtCore.QRect(20, 32, 161, 21))
        self.cbScale.setChecked(False)
        self.cbScale.setObjectName("cbScale")
        self.label_15 = QtWidgets.QLabel(self.tab_2)
        self.label_15.setGeometry(QtCore.QRect(30, 110, 251, 16))
        self.label_15.setObjectName("label_15")
        self.txtThre = QtWidgets.QLineEdit(self.tab_2)
        self.txtThre.setGeometry(QtCore.QRect(290, 110, 160, 21))
        self.txtThre.setObjectName("txtThre")
        self.txtEdgeThre = QtWidgets.QLineEdit(self.tab_2)
        self.txtEdgeThre.setGeometry(QtCore.QRect(290, 144, 160, 21))
        self.txtEdgeThre.setObjectName("txtEdgeThre")
        self.label_16 = QtWidgets.QLabel(self.tab_2)
        self.label_16.setGeometry(QtCore.QRect(30, 144, 251, 16))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.tab_2)
        self.label_17.setGeometry(QtCore.QRect(30, 180, 251, 16))
        self.label_17.setObjectName("label_17")
        self.txtAtlasPath = QtWidgets.QLineEdit(self.tab_2)
        self.txtAtlasPath.setGeometry(QtCore.QRect(290, 180, 160, 21))
        self.txtAtlasPath.setObjectName("txtAtlasPath")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.label_4 = QtWidgets.QLabel(self.tab_4)
        self.label_4.setGeometry(QtCore.QRect(20, 30, 201, 16))
        self.label_4.setObjectName("label_4")
        self.txtFilter = QtWidgets.QLineEdit(self.tab_4)
        self.txtFilter.setGeometry(QtCore.QRect(190, 30, 291, 21))
        self.txtFilter.setObjectName("txtFilter")
        self.label_5 = QtWidgets.QLabel(self.tab_4)
        self.label_5.setGeometry(QtCore.QRect(490, 30, 211, 16))
        self.label_5.setObjectName("label_5")
        self.txtClass = QtWidgets.QTextEdit(self.tab_4)
        self.txtClass.setGeometry(QtCore.QRect(190, 70, 91, 281))
        self.txtClass.setReadOnly(True)
        self.txtClass.setObjectName("txtClass")
        self.label_10 = QtWidgets.QLabel(self.tab_4)
        self.label_10.setGeometry(QtCore.QRect(20, 70, 201, 16))
        self.label_10.setObjectName("label_10")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.label_6 = QtWidgets.QLabel(self.tab_6)
        self.label_6.setGeometry(QtCore.QRect(30, 30, 201, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.tab_6)
        self.label_7.setGeometry(QtCore.QRect(500, 30, 211, 16))
        self.label_7.setObjectName("label_7")
        self.label_11 = QtWidgets.QLabel(self.tab_6)
        self.label_11.setGeometry(QtCore.QRect(30, 70, 201, 16))
        self.label_11.setObjectName("label_11")
        self.txtRegions = QtWidgets.QLineEdit(self.tab_6)
        self.txtRegions.setGeometry(QtCore.QRect(200, 30, 291, 21))
        self.txtRegions.setText("")
        self.txtRegions.setObjectName("txtRegions")
        self.txtRegionList = QtWidgets.QTextEdit(self.tab_6)
        self.txtRegionList.setGeometry(QtCore.QRect(200, 70, 91, 281))
        self.txtRegionList.setReadOnly(True)
        self.txtRegionList.setObjectName("txtRegionList")
        self.lblRegion = QtWidgets.QLabel(self.tab_6)
        self.lblRegion.setGeometry(QtCore.QRect(310, 330, 391, 16))
        self.lblRegion.setObjectName("lblRegion")
        self.tabWidget.addTab(self.tab_6, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.tabWidget.addTab(self.tab_5, "")
        self.label_35 = QtWidgets.QLabel(frmMAClassicNetwork)
        self.label_35.setGeometry(QtCore.QRect(30, 100, 111, 16))
        self.label_35.setObjectName("label_35")
        self.txtOutFile = QtWidgets.QLineEdit(frmMAClassicNetwork)
        self.txtOutFile.setGeometry(QtCore.QRect(180, 100, 521, 21))
        self.txtOutFile.setText("")
        self.txtOutFile.setObjectName("txtOutFile")
        self.btnOutFile = QtWidgets.QPushButton(frmMAClassicNetwork)
        self.btnOutFile.setGeometry(QtCore.QRect(710, 100, 51, 32))
        self.btnOutFile.setObjectName("btnOutFile")
        self.cbDiagram = QtWidgets.QCheckBox(frmMAClassicNetwork)
        self.cbDiagram.setGeometry(QtCore.QRect(30, 140, 341, 22))
        self.cbDiagram.setChecked(True)
        self.cbDiagram.setObjectName("cbDiagram")
        self.btnRedraw = QtWidgets.QPushButton(frmMAClassicNetwork)
        self.btnRedraw.setGeometry(QtCore.QRect(460, 590, 141, 32))
        self.btnRedraw.setObjectName("btnRedraw")
        self.btnAtlasFile = QtWidgets.QPushButton(frmMAClassicNetwork)
        self.btnAtlasFile.setGeometry(QtCore.QRect(710, 60, 51, 32))
        self.btnAtlasFile.setObjectName("btnAtlasFile")
        self.label_37 = QtWidgets.QLabel(frmMAClassicNetwork)
        self.label_37.setGeometry(QtCore.QRect(30, 60, 211, 16))
        self.label_37.setObjectName("label_37")
        self.txtAtlasFile = QtWidgets.QLineEdit(frmMAClassicNetwork)
        self.txtAtlasFile.setGeometry(QtCore.QRect(180, 60, 521, 21))
        self.txtAtlasFile.setText("")
        self.txtAtlasFile.setObjectName("txtAtlasFile")

        self.retranslateUi(frmMAClassicNetwork)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(frmMAClassicNetwork)
        frmMAClassicNetwork.setTabOrder(self.txtInFile, self.btnInFile)
        frmMAClassicNetwork.setTabOrder(self.btnInFile, self.tabWidget)
        frmMAClassicNetwork.setTabOrder(self.tabWidget, self.txtData)
        frmMAClassicNetwork.setTabOrder(self.txtData, self.txtLabel)
        frmMAClassicNetwork.setTabOrder(self.txtLabel, self.btnConvert)
        frmMAClassicNetwork.setTabOrder(self.btnConvert, self.btnClose)

    def retranslateUi(self, frmMAClassicNetwork):
        _translate = QtCore.QCoreApplication.translate
        frmMAClassicNetwork.setWindowTitle(_translate("frmMAClassicNetwork", "RAS"))
        self.btnInFile.setText(_translate("frmMAClassicNetwork", "..."))
        self.label_33.setText(_translate("frmMAClassicNetwork", "Input Data "))
        self.btnConvert.setText(_translate("frmMAClassicNetwork", "Analyze"))
        self.btnClose.setText(_translate("frmMAClassicNetwork", "Close"))
        self.label_2.setText(_translate("frmMAClassicNetwork", "Data"))
        self.label_3.setText(_translate("frmMAClassicNetwork", "Label"))
        self.label.setText(_translate("frmMAClassicNetwork", "ID"))
        self.label_31.setText(_translate("frmMAClassicNetwork", "Condition (can be empty)"))
        self.lblImgShape.setText(_translate("frmMAClassicNetwork", "imgShape"))
        self.label_32.setText(_translate("frmMAClassicNetwork", "Coordinate"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("frmMAClassicNetwork", "Data"))
        self.groupBox.setTitle(_translate("frmMAClassicNetwork", "<Input Data Normalization>"))
        self.cbScale.setText(_translate("frmMAClassicNetwork", "Scale Data~N(0,1)"))
        self.label_15.setText(_translate("frmMAClassicNetwork", "Network thresholding (of max)"))
        self.txtThre.setText(_translate("frmMAClassicNetwork", "0.95"))
        self.txtEdgeThre.setText(_translate("frmMAClassicNetwork", "0.8"))
        self.label_16.setText(_translate("frmMAClassicNetwork", "Edge thresholding (in figure)"))
        self.label_17.setText(_translate("frmMAClassicNetwork", "Atlas PATH"))
        self.txtAtlasPath.setText(_translate("frmMAClassicNetwork", "/tmp/atlas.nii.gz"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("frmMAClassicNetwork", "Parameters"))
        self.label_4.setText(_translate("frmMAClassicNetwork", "Remove Class IDs"))
        self.txtFilter.setText(_translate("frmMAClassicNetwork", "0"))
        self.label_5.setText(_translate("frmMAClassicNetwork", "e.g. 0 or [1,2]"))
        self.label_10.setText(_translate("frmMAClassicNetwork", "Existed Classes"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("frmMAClassicNetwork", "Filter Class ID"))
        self.label_6.setText(_translate("frmMAClassicNetwork", "Keep Regions"))
        self.label_7.setText(_translate("frmMAClassicNetwork", "e.g. 0 or [1,2]"))
        self.label_11.setText(_translate("frmMAClassicNetwork", "Existed Regions"))
        self.lblRegion.setText(_translate("frmMAClassicNetwork", "Number of Regions: 0"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("frmMAClassicNetwork", "Keep Region"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("frmMAClassicNetwork", "Integration"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("frmMAClassicNetwork", "Metric"))
        self.label_35.setText(_translate("frmMAClassicNetwork", "Output Data"))
        self.btnOutFile.setText(_translate("frmMAClassicNetwork", "..."))
        self.cbDiagram.setText(_translate("frmMAClassicNetwork", "Show Diagrams"))
        self.btnRedraw.setText(_translate("frmMAClassicNetwork", "Redraw"))
        self.btnAtlasFile.setText(_translate("frmMAClassicNetwork", "..."))
        self.label_37.setText(_translate("frmMAClassicNetwork", "Atlas"))

