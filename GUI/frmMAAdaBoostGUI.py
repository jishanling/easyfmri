# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmMAAdaBoostGUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_frmMAAdaBoost(object):
    def setupUi(self, frmMAAdaBoost):
        frmMAAdaBoost.setObjectName("frmMAAdaBoost")
        frmMAAdaBoost.resize(846, 764)
        self.btnInFile = QtWidgets.QPushButton(frmMAAdaBoost)
        self.btnInFile.setGeometry(QtCore.QRect(780, 20, 51, 32))
        self.btnInFile.setObjectName("btnInFile")
        self.label_33 = QtWidgets.QLabel(frmMAAdaBoost)
        self.label_33.setGeometry(QtCore.QRect(30, 20, 211, 16))
        self.label_33.setObjectName("label_33")
        self.btnOutFile = QtWidgets.QPushButton(frmMAAdaBoost)
        self.btnOutFile.setGeometry(QtCore.QRect(780, 60, 51, 32))
        self.btnOutFile.setObjectName("btnOutFile")
        self.txtInFile = QtWidgets.QLineEdit(frmMAAdaBoost)
        self.txtInFile.setGeometry(QtCore.QRect(210, 20, 551, 21))
        self.txtInFile.setText("")
        self.txtInFile.setObjectName("txtInFile")
        self.btnConvert = QtWidgets.QPushButton(frmMAAdaBoost)
        self.btnConvert.setGeometry(QtCore.QRect(690, 715, 141, 32))
        self.btnConvert.setObjectName("btnConvert")
        self.label_35 = QtWidgets.QLabel(frmMAAdaBoost)
        self.label_35.setGeometry(QtCore.QRect(30, 60, 211, 16))
        self.label_35.setObjectName("label_35")
        self.txtOutFile = QtWidgets.QLineEdit(frmMAAdaBoost)
        self.txtOutFile.setGeometry(QtCore.QRect(210, 60, 551, 21))
        self.txtOutFile.setText("")
        self.txtOutFile.setObjectName("txtOutFile")
        self.btnClose = QtWidgets.QPushButton(frmMAAdaBoost)
        self.btnClose.setGeometry(QtCore.QRect(30, 715, 141, 32))
        self.btnClose.setObjectName("btnClose")
        self.tabWidget = QtWidgets.QTabWidget(frmMAAdaBoost)
        self.tabWidget.setGeometry(QtCore.QRect(30, 150, 801, 551))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 60, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(20, 110, 60, 16))
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(360, 10, 61, 16))
        self.label.setObjectName("label")
        self.txtITrLabel = QtWidgets.QComboBox(self.tab)
        self.txtITrLabel.setGeometry(QtCore.QRect(240, 110, 121, 26))
        self.txtITrLabel.setEditable(True)
        self.txtITrLabel.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.txtITrLabel.setObjectName("txtITrLabel")
        self.txtITrData = QtWidgets.QComboBox(self.tab)
        self.txtITrData.setGeometry(QtCore.QRect(240, 70, 121, 26))
        self.txtITrData.setEditable(True)
        self.txtITrData.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.txtITrData.setObjectName("txtITrData")
        self.txtITeLabel = QtWidgets.QComboBox(self.tab)
        self.txtITeLabel.setGeometry(QtCore.QRect(390, 110, 121, 26))
        self.txtITeLabel.setEditable(True)
        self.txtITeLabel.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.txtITeLabel.setObjectName("txtITeLabel")
        self.txtITeData = QtWidgets.QComboBox(self.tab)
        self.txtITeData.setGeometry(QtCore.QRect(390, 70, 121, 26))
        self.txtITeData.setEditable(True)
        self.txtITeData.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.txtITeData.setObjectName("txtITeData")
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(285, 40, 81, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.tab)
        self.label_8.setGeometry(QtCore.QRect(430, 40, 81, 16))
        self.label_8.setObjectName("label_8")
        self.txtFoldID = QtWidgets.QComboBox(self.tab)
        self.txtFoldID.setGeometry(QtCore.QRect(240, 150, 121, 26))
        self.txtFoldID.setEditable(True)
        self.txtFoldID.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.txtFoldID.setObjectName("txtFoldID")
        self.label_9 = QtWidgets.QLabel(self.tab)
        self.label_9.setGeometry(QtCore.QRect(20, 150, 121, 16))
        self.label_9.setObjectName("label_9")
        self.lbFoldID = QtWidgets.QLabel(self.tab)
        self.lbFoldID.setGeometry(QtCore.QRect(390, 150, 251, 16))
        self.lbFoldID.setObjectName("lbFoldID")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.groupBox = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox.setGeometry(QtCore.QRect(30, 20, 751, 80))
        self.groupBox.setObjectName("groupBox")
        self.cbScale = QtWidgets.QCheckBox(self.groupBox)
        self.cbScale.setGeometry(QtCore.QRect(20, 40, 641, 21))
        self.cbScale.setChecked(True)
        self.cbScale.setObjectName("cbScale")
        self.txtLearningRate = QtWidgets.QLineEdit(self.tab_2)
        self.txtLearningRate.setGeometry(QtCore.QRect(260, 200, 160, 21))
        self.txtLearningRate.setObjectName("txtLearningRate")
        self.label_11 = QtWidgets.QLabel(self.tab_2)
        self.label_11.setGeometry(QtCore.QRect(30, 200, 221, 16))
        self.label_11.setObjectName("label_11")
        self.cbAlgorithm = QtWidgets.QComboBox(self.tab_2)
        self.cbAlgorithm.setGeometry(QtCore.QRect(260, 120, 161, 26))
        self.cbAlgorithm.setObjectName("cbAlgorithm")
        self.label_19 = QtWidgets.QLabel(self.tab_2)
        self.label_19.setGeometry(QtCore.QRect(30, 120, 231, 16))
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.tab_2)
        self.label_20.setGeometry(QtCore.QRect(30, 160, 221, 16))
        self.label_20.setObjectName("label_20")
        self.txtNEstimators = QtWidgets.QLineEdit(self.tab_2)
        self.txtNEstimators.setGeometry(QtCore.QRect(260, 160, 160, 21))
        self.txtNEstimators.setObjectName("txtNEstimators")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.tabWidget.addTab(self.tab_6, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.txtFoldFrom = QtWidgets.QSpinBox(self.tab_3)
        self.txtFoldFrom.setGeometry(QtCore.QRect(100, 30, 80, 24))
        self.txtFoldFrom.setMaximum(100000)
        self.txtFoldFrom.setProperty("value", 1)
        self.txtFoldFrom.setObjectName("txtFoldFrom")
        self.label_17 = QtWidgets.QLabel(self.tab_3)
        self.label_17.setGeometry(QtCore.QRect(40, 30, 60, 16))
        self.label_17.setObjectName("label_17")
        self.txtFoldTo = QtWidgets.QSpinBox(self.tab_3)
        self.txtFoldTo.setGeometry(QtCore.QRect(270, 30, 80, 24))
        self.txtFoldTo.setMaximum(100000)
        self.txtFoldTo.setProperty("value", 1)
        self.txtFoldTo.setObjectName("txtFoldTo")
        self.label_44 = QtWidgets.QLabel(self.tab_3)
        self.label_44.setGeometry(QtCore.QRect(210, 30, 60, 16))
        self.label_44.setObjectName("label_44")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 20, 771, 201))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_10 = QtWidgets.QLabel(self.groupBox_2)
        self.label_10.setGeometry(QtCore.QRect(20, 70, 201, 16))
        self.label_10.setObjectName("label_10")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(20, 40, 201, 16))
        self.label_4.setObjectName("label_4")
        self.txtFilter = QtWidgets.QLineEdit(self.groupBox_2)
        self.txtFilter.setGeometry(QtCore.QRect(190, 40, 441, 21))
        self.txtFilter.setObjectName("txtFilter")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(640, 40, 111, 16))
        self.label_5.setObjectName("label_5")
        self.txtClass = QtWidgets.QTextEdit(self.groupBox_2)
        self.txtClass.setGeometry(QtCore.QRect(190, 70, 231, 121))
        self.txtClass.setReadOnly(True)
        self.txtClass.setObjectName("txtClass")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 230, 771, 201))
        self.groupBox_3.setObjectName("groupBox_3")
        self.cbFilterTrID = QtWidgets.QCheckBox(self.groupBox_3)
        self.cbFilterTrID.setGeometry(QtCore.QRect(20, 40, 191, 21))
        self.cbFilterTrID.setObjectName("cbFilterTrID")
        self.txtFilterTrID = QtWidgets.QComboBox(self.groupBox_3)
        self.txtFilterTrID.setGeometry(QtCore.QRect(190, 40, 231, 26))
        self.txtFilterTrID.setEditable(True)
        self.txtFilterTrID.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.txtFilterTrID.setObjectName("txtFilterTrID")
        self.label_6 = QtWidgets.QLabel(self.groupBox_3)
        self.label_6.setGeometry(QtCore.QRect(20, 80, 201, 16))
        self.label_6.setObjectName("label_6")
        self.label_13 = QtWidgets.QLabel(self.groupBox_3)
        self.label_13.setGeometry(QtCore.QRect(640, 80, 111, 16))
        self.label_13.setObjectName("label_13")
        self.txtFilterTrContent = QtWidgets.QLineEdit(self.groupBox_3)
        self.txtFilterTrContent.setGeometry(QtCore.QRect(190, 80, 441, 21))
        self.txtFilterTrContent.setText("")
        self.txtFilterTrContent.setObjectName("txtFilterTrContent")
        self.label_14 = QtWidgets.QLabel(self.groupBox_3)
        self.label_14.setGeometry(QtCore.QRect(640, 160, 111, 16))
        self.label_14.setObjectName("label_14")
        self.cbFilterTeID = QtWidgets.QCheckBox(self.groupBox_3)
        self.cbFilterTeID.setGeometry(QtCore.QRect(20, 120, 191, 21))
        self.cbFilterTeID.setObjectName("cbFilterTeID")
        self.txtFilterTeContent = QtWidgets.QLineEdit(self.groupBox_3)
        self.txtFilterTeContent.setGeometry(QtCore.QRect(190, 160, 441, 21))
        self.txtFilterTeContent.setText("")
        self.txtFilterTeContent.setObjectName("txtFilterTeContent")
        self.txtFilterTeID = QtWidgets.QComboBox(self.groupBox_3)
        self.txtFilterTeID.setGeometry(QtCore.QRect(190, 120, 231, 26))
        self.txtFilterTeID.setEditable(True)
        self.txtFilterTeID.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.txtFilterTeID.setObjectName("txtFilterTeID")
        self.label_16 = QtWidgets.QLabel(self.groupBox_3)
        self.label_16.setGeometry(QtCore.QRect(20, 160, 201, 16))
        self.label_16.setObjectName("label_16")
        self.btnShowFilterContent = QtWidgets.QPushButton(self.groupBox_3)
        self.btnShowFilterContent.setGeometry(QtCore.QRect(620, 40, 141, 23))
        self.btnShowFilterContent.setObjectName("btnShowFilterContent")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.cbAverage = QtWidgets.QCheckBox(self.tab_5)
        self.cbAverage.setGeometry(QtCore.QRect(20, 30, 181, 20))
        self.cbAverage.setChecked(True)
        self.cbAverage.setObjectName("cbAverage")
        self.cbPrecision = QtWidgets.QCheckBox(self.tab_5)
        self.cbPrecision.setGeometry(QtCore.QRect(20, 70, 181, 20))
        self.cbPrecision.setChecked(True)
        self.cbPrecision.setObjectName("cbPrecision")
        self.cbPrecisionAvg = QtWidgets.QComboBox(self.tab_5)
        self.cbPrecisionAvg.setGeometry(QtCore.QRect(240, 70, 321, 26))
        self.cbPrecisionAvg.setObjectName("cbPrecisionAvg")
        self.cbAPrecisionAvg = QtWidgets.QComboBox(self.tab_5)
        self.cbAPrecisionAvg.setGeometry(QtCore.QRect(240, 110, 321, 26))
        self.cbAPrecisionAvg.setObjectName("cbAPrecisionAvg")
        self.cbAPrecision = QtWidgets.QCheckBox(self.tab_5)
        self.cbAPrecision.setGeometry(QtCore.QRect(20, 110, 231, 20))
        self.cbAPrecision.setChecked(False)
        self.cbAPrecision.setObjectName("cbAPrecision")
        self.cbRecallAvg = QtWidgets.QComboBox(self.tab_5)
        self.cbRecallAvg.setGeometry(QtCore.QRect(240, 150, 321, 26))
        self.cbRecallAvg.setObjectName("cbRecallAvg")
        self.cbRecall = QtWidgets.QCheckBox(self.tab_5)
        self.cbRecall.setGeometry(QtCore.QRect(20, 150, 181, 20))
        self.cbRecall.setChecked(True)
        self.cbRecall.setObjectName("cbRecall")
        self.cbF1 = QtWidgets.QCheckBox(self.tab_5)
        self.cbF1.setGeometry(QtCore.QRect(20, 190, 181, 20))
        self.cbF1.setChecked(True)
        self.cbF1.setObjectName("cbF1")
        self.cbF1Avg = QtWidgets.QComboBox(self.tab_5)
        self.cbF1Avg.setGeometry(QtCore.QRect(240, 190, 321, 26))
        self.cbF1Avg.setObjectName("cbF1Avg")
        self.tabWidget.addTab(self.tab_5, "")
        self.label_12 = QtWidgets.QLabel(frmMAAdaBoost)
        self.label_12.setGeometry(QtCore.QRect(185, 720, 421, 20))
        self.label_12.setObjectName("label_12")
        self.btnOutModel = QtWidgets.QPushButton(frmMAAdaBoost)
        self.btnOutModel.setGeometry(QtCore.QRect(780, 100, 51, 32))
        self.btnOutModel.setObjectName("btnOutModel")
        self.label_36 = QtWidgets.QLabel(frmMAAdaBoost)
        self.label_36.setGeometry(QtCore.QRect(30, 100, 231, 16))
        self.label_36.setObjectName("label_36")
        self.txtOutModel = QtWidgets.QLineEdit(frmMAAdaBoost)
        self.txtOutModel.setGeometry(QtCore.QRect(210, 100, 551, 21))
        self.txtOutModel.setText("")
        self.txtOutModel.setObjectName("txtOutModel")

        self.retranslateUi(frmMAAdaBoost)
        self.tabWidget.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(frmMAAdaBoost)
        frmMAAdaBoost.setTabOrder(self.txtInFile, self.btnInFile)
        frmMAAdaBoost.setTabOrder(self.btnInFile, self.txtOutFile)
        frmMAAdaBoost.setTabOrder(self.txtOutFile, self.btnOutFile)
        frmMAAdaBoost.setTabOrder(self.btnOutFile, self.tabWidget)
        frmMAAdaBoost.setTabOrder(self.tabWidget, self.txtITrData)
        frmMAAdaBoost.setTabOrder(self.txtITrData, self.txtITrLabel)
        frmMAAdaBoost.setTabOrder(self.txtITrLabel, self.btnConvert)
        frmMAAdaBoost.setTabOrder(self.btnConvert, self.btnClose)

    def retranslateUi(self, frmMAAdaBoost):
        _translate = QtCore.QCoreApplication.translate
        frmMAAdaBoost.setWindowTitle(_translate("frmMAAdaBoost", "AdaBoost"))
        self.btnInFile.setText(_translate("frmMAAdaBoost", "..."))
        self.label_33.setText(_translate("frmMAAdaBoost", "Input Data (per fold)"))
        self.btnOutFile.setText(_translate("frmMAAdaBoost", "..."))
        self.btnConvert.setText(_translate("frmMAAdaBoost", "Analyze"))
        self.label_35.setText(_translate("frmMAAdaBoost", "Analysis Results"))
        self.btnClose.setText(_translate("frmMAAdaBoost", "Close"))
        self.label_2.setText(_translate("frmMAAdaBoost", "Data"))
        self.label_3.setText(_translate("frmMAAdaBoost", "Label"))
        self.label.setText(_translate("frmMAAdaBoost", "Input"))
        self.label_7.setText(_translate("frmMAAdaBoost", "Train"))
        self.label_8.setText(_translate("frmMAAdaBoost", "Test"))
        self.label_9.setText(_translate("frmMAAdaBoost", "FoldID"))
        self.lbFoldID.setText(_translate("frmMAAdaBoost", "ID=None"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("frmMAAdaBoost", "Data"))
        self.groupBox.setTitle(_translate("frmMAAdaBoost", "<Input Data Normalization>"))
        self.cbScale.setText(_translate("frmMAAdaBoost", "Scale Data Train~N(0,1) and Test~N(0,1)"))
        self.txtLearningRate.setText(_translate("frmMAAdaBoost", "1"))
        self.label_11.setText(_translate("frmMAAdaBoost", "Learning Rate"))
        self.label_19.setText(_translate("frmMAAdaBoost", "Algorithm"))
        self.label_20.setText(_translate("frmMAAdaBoost", "Num of Estimators"))
        self.txtNEstimators.setText(_translate("frmMAAdaBoost", "50"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("frmMAAdaBoost", "Parameters"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("frmMAAdaBoost", "Base Algorithm"))
        self.label_17.setText(_translate("frmMAAdaBoost", "From:"))
        self.label_44.setText(_translate("frmMAAdaBoost", "To:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("frmMAAdaBoost", "Fold"))
        self.groupBox_2.setTitle(_translate("frmMAAdaBoost", "<Filter based on Class ID>"))
        self.label_10.setText(_translate("frmMAAdaBoost", "Existed Classes"))
        self.label_4.setText(_translate("frmMAAdaBoost", "Remove Class IDs"))
        self.txtFilter.setText(_translate("frmMAAdaBoost", "0"))
        self.label_5.setText(_translate("frmMAAdaBoost", "e.g. 0 or [1,2]"))
        self.groupBox_3.setTitle(_translate("frmMAAdaBoost", "<Based on a reference>"))
        self.cbFilterTrID.setText(_translate("frmMAAdaBoost", "Filter training based on"))
        self.label_6.setText(_translate("frmMAAdaBoost", "Remove training contents"))
        self.label_13.setText(_translate("frmMAAdaBoost", "e.g. 0 or [1,2]"))
        self.label_14.setText(_translate("frmMAAdaBoost", "e.g. 0 or [1,2]"))
        self.cbFilterTeID.setText(_translate("frmMAAdaBoost", "Filter testing based on"))
        self.label_16.setText(_translate("frmMAAdaBoost", "Remove testing contents"))
        self.btnShowFilterContent.setText(_translate("frmMAAdaBoost", "Show Content"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("frmMAAdaBoost", "Filter"))
        self.cbAverage.setText(_translate("frmMAAdaBoost", "Average"))
        self.cbPrecision.setText(_translate("frmMAAdaBoost", "Precision"))
        self.cbAPrecision.setText(_translate("frmMAAdaBoost", "Average of Precision"))
        self.cbRecall.setText(_translate("frmMAAdaBoost", "Recall"))
        self.cbF1.setText(_translate("frmMAAdaBoost", "f1 score"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("frmMAAdaBoost", "Metrics"))
        self.label_12.setText(_translate("frmMAAdaBoost", "$FOLD$ will be replaced by fold number."))
        self.btnOutModel.setText(_translate("frmMAAdaBoost", "..."))
        self.label_36.setText(_translate("frmMAAdaBoost", "Models (per fold/opt)"))

