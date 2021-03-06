# Copyright (c) 2014--2020 Tony (Muhammad) Yousefnezhad
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import sys

import numpy as np
import nibabel as nb
from PyQt5.QtWidgets import *
from sklearn import preprocessing
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from Base.dialogs import LoadFile, SaveFile
from Base.utility import getVersion, getBuild, getCPUCore
from GUI.frmAAVoxelGUI import *
from GUI.frmAAVoxelSelection import *
from MVPA.MultiThreadingVectorClassification import MultiThreadingVectorClassification
from IO.mainIO import mainIO_load, mainIO_save, reshape_1Dvector

import logging


logging.basicConfig(level=logging.DEBUG)
from pyqode.core import api
from pyqode.core import modes
from pyqode.core import panels
from pyqode.qt import QtWidgets as pyWidgets



def EventCode():
    return\
"""from sklearn.linear_model import LogisticRegression as CLS
# Uncomment this line to use Linear SVC
#from sklearn.svm import LinearSVC as CLS
model = CLS()
"""



class frmAAVoxel(Ui_frmAAVoxel):
    ui = Ui_frmAAVoxel()
    dialog = None
    # This function is run when the main form start
    # and initiate the default parameters.
    def show(self):
        global dialog
        global ui
        ui = Ui_frmAAVoxel()
        QtWidgets.QApplication.setStyle(QtWidgets.QStyleFactory.create('Fusion'))
        dialog = QtWidgets.QMainWindow()
        ui.setupUi(dialog)
        self.set_events(self)
        ui.tabWidget.setCurrentIndex(0)


        ui.txtEvents = api.CodeEdit(ui.tab_2)
        ui.txtEvents.setGeometry(QtCore.QRect(10, 10, 641, 200))
        ui.txtEvents.setObjectName("txtEvents")

        ui.txtEvents.backend.start('backend/server.py')

        ui.txtEvents.modes.append(modes.CodeCompletionMode())
        ui.txtEvents.modes.append(modes.CaretLineHighlighterMode())
        ui.txtEvents.modes.append(modes.PygmentsSyntaxHighlighter(ui.txtEvents.document()))
        ui.txtEvents.panels.append(panels.LineNumberPanel(),api.Panel.Position.LEFT)

        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        ui.txtEvents.setFont(font)
        ui.txtEvents.setPlainText(EventCode(),"","")



        dialog.setWindowTitle("easy fMRI Voxel based analysis - V" + getVersion() + "B" + getBuild())
        dialog.setWindowFlags(dialog.windowFlags() | QtCore.Qt.CustomizeWindowHint)
        dialog.setWindowFlags(dialog.windowFlags() & ~QtCore.Qt.WindowMaximizeButtonHint)
        dialog.setFixedSize(dialog.size())
        dialog.show()


    # This function initiate the events procedures
    def set_events(self):
        global ui
        ui.btnClose.clicked.connect(self.btnClose_click)
        ui.btnInFile.clicked.connect(self.btnInFile_click)
        ui.btnOutFile.clicked.connect(self.btnOutFile_click)
        ui.btnConvert.clicked.connect(self.btnConvert_click)
        ui.btnSelection.clicked.connect(self.btnSelection_click)

    def btnSelection_click(self):
        try:
            frmAAVoxelSelection.show(frmAAVoxelSelection)
        except Exception as e:
            print(str(e))

    def btnClose_click(self):
        global dialog
        dialog.close()


    def btnInFile_click(self):
        filename = LoadFile("Load data file ...",['Data files (*.ezx *.mat *.ezdata)'],'ezx',\
                            os.path.dirname(ui.txtInFile.text()))

        if len(filename):
            if os.path.isfile(filename):
                try:
                    data = mainIO_load(filename)
                    Keys = data.keys()

                    # Data
                    ui.txtData.clear()
                    HasDefualt = 0
                    for key in Keys:
                        ui.txtData.addItem(key)
                        if key == "data":
                            HasDefualt = 1
                        if key == "train_data":
                            HasDefualt = 2
                    if HasDefualt == 1:
                        ui.txtData.setCurrentText("data")
                    if HasDefualt == 2:
                        ui.txtData.setCurrentText("train_data")

                    # Test Data
                    ui.txtTeData.clear()
                    HasDefualt = 0
                    for key in Keys:
                        ui.txtTeData.addItem(key)
                        if key == "data":
                            HasDefualt = 1
                        if key == "test_data":
                            HasDefualt = 2
                    if HasDefualt == 1:
                        ui.txtTeData.setCurrentText("data")
                    if HasDefualt == 2:
                        ui.txtTeData.setCurrentText("test_data")



                    # Label
                    ui.txtLabel.clear()
                    HasDefualt = 0
                    for key in Keys:
                        ui.txtLabel.addItem(key)
                        if key == "label":
                            HasDefualt = 1
                        if key == "train_label":
                            HasDefualt = 2
                    if HasDefualt == 1:
                        ui.txtLabel.setCurrentText("label")
                    if HasDefualt == 2:
                        ui.txtLabel.setCurrentText("train_label")

                    # Test Label
                    ui.txtTeLabel.clear()
                    HasDefualt = 0
                    for key in Keys:
                        ui.txtTeLabel.addItem(key)
                        if key == "label":
                            HasDefualt = 1
                        if key == "test_label":
                            HasDefualt = 2
                    if HasDefualt == 1:
                        ui.txtTeLabel.setCurrentText("label")
                    if HasDefualt == 2:
                        ui.txtTeLabel.setCurrentText("test_label")

                    # Coordinate
                    ui.txtCol.clear()
                    HasDefualt = False
                    for key in Keys:
                        ui.txtCol.addItem(key)
                        if key == "coordinate":
                            HasDefualt = True
                    if HasDefualt:
                        ui.txtCol.setCurrentText("coordinate")


                    ui.txtInFile.setText(filename)
                except Exception as e:
                    print(e)
                    print("Cannot load data file!")
                    return
            else:
                print("File not found!")



    def btnOutFile_click(self):
        ofile = SaveFile("Save data file ...",['Data files (*.ezx *.mat)'],'ezx',\
                             os.path.dirname(ui.txtOutFile.text()))
        if len(ofile):
            ui.txtOutFile.setText(ofile)

    def btnConvert_click(self):
        msgBox = QMessageBox()
        print("Loading...")
        # Job
        NumJob = ui.txtJob.value()
        if NumJob < 1:
            NumJob = getCPUCore()
        try:
            FoldFrom = np.int32(ui.txtFoldFrom.text())
            FoldTo   = np.int32(ui.txtFoldTo.text())
        except:
            print("Please check fold parameters!")
            return
        # OutFile
        OutFile = ui.txtOutFile.text()
        if not len(OutFile):
            msgBox.setText("Please enter out file!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return False
        ResData = dict()
        Coord   = None
        CodeText = ui.txtEvents.toPlainText()
        for fold in range(FoldFrom, FoldTo + 1):
            print(f"Analyzing Fold: {fold}...")
            # InFile
            InFile = ui.txtInFile.text()
            if not len(InFile):
                msgBox.setText(f"FOLD {fold}: Please enter input file!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False
            InFile = InFile.replace("$FOLD$", str(fold))
            if not os.path.isfile(InFile):
                msgBox.setText(f"FOLD {fold}: Input file not found!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False
            # Load InData
            InData = None
            try:
                InData = mainIO_load(InFile)
            except:
                print(f"FOLD {fold}: Cannot load file: {InFile}")
            # Train data
            if not len(ui.txtData.currentText()):
                msgBox.setText(f"FOLD {fold}: Please enter train data variable name!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False
            try:
                Xtr = InData[ui.txtData.currentText()]
                if ui.cbScale.isChecked():
                    Xtr = preprocessing.scale(Xtr)
                    print(f"FOLD {fold}: Whole of train data is scaled X~N(0,1).")
            except:
                print(f"FOLD {fold}: Cannot load train data")
                msgBox.setText(f"FOLD {fold}: Cannot load train data!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False
            # Test data
            if not len(ui.txtTeData.currentText()):
                msgBox.setText(f"FOLD {fold}: Please enter test data variable name!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False
            try:
                Xte = InData[ui.txtTeData.currentText()]
                if ui.cbScale.isChecked():
                    Xte = preprocessing.scale(Xte)
                    print(f"FOLD {fold}: Whole of test data is scaled X~N(0,1).")
            except:
                print(f"FOLD {fold}: Cannot load test data")
                msgBox.setText(f"FOLD {fold}: Cannot load train data!")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec_()
                return False
            # Train Label
            if not len(ui.txtLabel.currentText()):
                    msgBox.setText(f"FOLD {fold}: Please enter Label variable name!")
                    msgBox.setIcon(QMessageBox.Critical)
                    msgBox.setStandardButtons(QMessageBox.Ok)
                    msgBox.exec_()
                    return False
            try:
                Ytr = InData[ui.txtLabel.currentText()][0]
            except:
                print(f"FOLD {fold}: Cannot load label")
                return
            # Test Label
            if not len(ui.txtTeLabel.currentText()):
                    msgBox.setText(f"FOLD {fold}: Please enter test Label variable name!")
                    msgBox.setIcon(QMessageBox.Critical)
                    msgBox.setStandardButtons(QMessageBox.Ok)
                    msgBox.exec_()
                    return False
            try:
                Yte = InData[ui.txtTeLabel.currentText()][0]
            except:
                print(f"FOLD {fold}: Cannot load test label")
                return
            # Coordinate
            if Coord is None:
                if not len(ui.txtCol.currentText()):
                    msgBox.setText("Please enter Condition variable name!")
                    msgBox.setIcon(QMessageBox.Critical)
                    msgBox.setStandardButtons(QMessageBox.Ok)
                    msgBox.exec_()
                    return False
                try:
                    Coord = np.transpose(InData[ui.txtCol.currentText()])
                    CoordSize = np.shape(Coord)[0]
                except:
                    print("Cannot load coordinate")
                    return
            print(f"FOLD {fold}: analyzing regions...")
            startIndex = 0
            stepIndex  = int(CoordSize / NumJob) + 1
            ThreadList = list()
            ThreadID   = 1
            while startIndex < CoordSize:
                try:
                    allvars = dict(locals(), **globals())
                    exec(CodeText, allvars, allvars)
                    model = allvars['model']
                except Exception as e:
                    print(f'Cannot generate model\n{e}')
                    msgBox.setText(f'Cannot generate model\n{e}')
                    msgBox.setIcon(QMessageBox.Critical)
                    msgBox.setStandardButtons(QMessageBox.Ok)
                    msgBox.exec_()
                    return False
                if startIndex + stepIndex < CoordSize:
                    endIndex = startIndex + stepIndex
                else:
                    endIndex = CoordSize
                TrainX = Xtr[:, startIndex:endIndex]
                TestX  = Xte[:, startIndex:endIndex]
                T = MultiThreadingVectorClassification(TrX=TrainX,
                                                       Try=Ytr,
                                                       TeX=TestX,
                                                       Tey=Yte,
                                                       startIndex=startIndex,
                                                       model=model,
                                                       processID=ThreadID)
                print("Thread {:5d} is generated for voxels in range from {:15d} to {:15d}. # voxels: {:15d}. # cores: {:5d}. Step size: {:10d}".format(ThreadID, startIndex, endIndex, CoordSize, NumJob, stepIndex))
                ThreadList.append(T)
                ThreadID    += 1
                startIndex  += stepIndex
            print(f"FOLD {fold}: running threads...")
            for tt in ThreadList:
                if not tt.is_alive():
                    tt.start()
            # Waiting the process will be finish
            for tt in ThreadList:
                tt.join()
            print(f"FOLD {fold}: finalizing results...")


            for ttIdx, tt in enumerate(ThreadList):
                for res in tt.Results:
                    try:
                        ResData[res[0]] += res[1]
                    except:
                        ResData[res[0]] = res[1]
                print('FOLD {:5d} and thread {:5d} is done.'.format(fold, ttIdx+1))

        OutData = dict()
        NumFold = FoldTo - FoldFrom + 1
        FinalResult = list()
        FinalAccuracy = list()
        for key in ResData.keys():
            coo = Coord[key, :]
            acc = ResData[key] / NumFold
            FinalResult.append([[coo], [[acc]]])
            FinalAccuracy.append(acc)
        print("Saving ...")
        mainIO_save({"accuracy": reshape_1Dvector(FinalAccuracy),\
                     "results": reshape_1Dvector(FinalResult),\
                     ui.txtCol.currentText():Coord}, \
                    ui.txtOutFile.text())
        # io.savemat(ui.txtOutFile.text(), mdict={"accuracy": FinalAccuracy,
        #                                         "results": FinalResult,
        #                                         ui.txtCol.currentText():Coord})
        print("DONE.")
        msgBox.setText("Wised voxel analysis is done.")
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec_()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    frmAAVoxel.show(frmAAVoxel)
    sys.exit(app.exec_())