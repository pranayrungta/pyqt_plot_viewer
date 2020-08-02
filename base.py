from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt

class Slider:
    def __init__(self, label="p:", vals=['a','b','c']):
        slider = QtWidgets.QSlider(Qt.Horizontal)
        slider.setSingleStep(1)
        slider.setRange(0, len(vals)-1)
        slider.setFocusPolicy(Qt.NoFocus)
        slider.valueChanged.connect(self.updateLabel)

        self.vals=vals
        self.label = QtWidgets.QLabel(label)
        self.slider = slider
        self.current_value = QtWidgets.QLabel(vals[0])


        hbox = QtWidgets.QHBoxLayout()
        hbox.addWidget(self.label)
        hbox.addWidget(self.slider)
        hbox.addWidget(self.current_value)
        self.hbox = hbox
        print('sldkfj')

    def updateLabel(self, i):
        self.current_value.setText(self.vals[i])
        print( self.vals[ self.slider.value() ] )

    def value(self):
        print(self.slider.value())
        return self.vals[ self.slider.value() ]



class UI(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.comboBox = QtWidgets.QComboBox()
        self.comboBox.addItems(['wire','p'])
        self.comboBox.activated.connect(self.getComboValue)

        self.prob = Slider('p', ['a', 'ab', 'asa'])

        initPopPara_Layout = QtWidgets.QVBoxLayout()
        initPopPara_Layout.addStretch()
        initPopPara_Layout.addWidget(self.comboBox)
        initPopPara_Layout.addLayout(self.prob.hbox)
        initPopPara_Layout.addStretch()
        InitPop_grpBox = QtWidgets.QGroupBox("Parameters")
        InitPop_grpBox.setLayout(initPopPara_Layout)
        #==============================================================

        self.longrange = QtWidgets.QCheckBox("Long Range Interactions")
        nbrHd_vLayout = QtWidgets.QVBoxLayout()
        nbrHd_vLayout.addWidget(self.longrange)
        nbrHd_vLayout.addStretch()
        NbrHd_grpBox = QtWidgets.QGroupBox("Plot")
        NbrHd_grpBox.setLayout(nbrHd_vLayout)
        #=================================================================

        self.setWindowTitle("Plot Viewer")
        self.centralwidget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.centralwidget)
        horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        horizontalLayout.addWidget(InitPop_grpBox)
        horizontalLayout.addWidget(NbrHd_grpBox)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.setStatusBar(self.statusbar)
        self.statusbar.showMessage('Working...')

    def getComboValue(self):
        print((self.comboBox.currentText(), self.comboBox.currentIndex()))


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    form = UI()
    form.show()
    sys.exit(app.exec_())
