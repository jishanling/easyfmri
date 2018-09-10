import sys
from PyQt5.QtWidgets import *
import PyQt5.QtCore as QtCore


class frmLayer(QDialog):
    def __init__(self):
        super().__init__()
        self.func = None
        self.unit = None
        self.isAdd = False
        self.title = 'Add a Layer'
        self.left = 0
        self.top = 0
        self.width = 300
        self.height = 150
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.label1 = QLabel()
        self.label1.setText("Function type:")
        self.cbType = QComboBox()
        self.cbType.addItem("ReLu", "relu")
        self.cbType.addItem("Sigmoid", "sigmoid")
        self.cbType.addItem("Tanh", "tanh")
        self.cbType.addItem("Soft Max", "softmax")
        self.cbType.addItem("Soft Min", "softmin")
        self.cbType.addItem("None", "none")
        self.label2 = QLabel()
        self.label2.setText("Number of Unit:")
        self.txtUnit = QSpinBox()
        self.txtUnit.setMinimum(1)
        self.txtUnit.setMaximum(100000)
        self.txtUnit.setValue(1)
        self.btnAdd = QPushButton()
        self.btnAdd.setText("Add")
        self.btnAdd.clicked.connect(self.btnAdd_onclick)
        self.btnExit = QPushButton()
        self.btnExit.setText("Exit")
        self.btnExit.clicked.connect(self.btnExit_onclick)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label1)
        self.layout.addWidget(self.cbType)
        self.layout.addWidget(self.label2)
        self.layout.addWidget(self.txtUnit)
        self.layout.addWidget(self.btnAdd)
        self.layout.addWidget(self.btnExit)
        self.setLayout(self.layout)
        self.exec_()

    def btnExit_onclick(self):
        self.close()

    def btnAdd_onclick(self):
        self.func = self.cbType.currentData()
        self.unit = self.txtUnit.value()
        self.isAdd = True
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    frmlayer = frmLayer()
    if frmlayer.isAdd:
        print(frmlayer.func)
        print(frmlayer.unit)