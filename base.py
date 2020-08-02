from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt

def DoubleSpinBox(minimum=0, maximum=1.0, singleStep=0.1):
    box = QtWidgets.QDoubleSpinBox()
    box.setMinimum(minimum)
    box.setMaximum(maximum)
    box.setSingleStep(singleStep)
    return box

def SpinBox(maximum, singleStep, init_value=0):
    box = QtWidgets.QSpinBox()
    box.setMaximum(maximum)
    box.setSingleStep(singleStep)
    box.setProperty("value", init_value)
    return box

def FormLay(label_Field_list):
    formLayout = QtWidgets.QFormLayout()
    for i,(label,field) in enumerate(label_Field_list):
        formLayout.setWidget(i, QtWidgets.QFormLayout.LabelRole, label)
        formLayout.setWidget(i, QtWidgets.QFormLayout.FieldRole, field)
    return formLayout

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
        i0_label = QtWidgets.QLabel("Io:")
        r0_label = QtWidgets.QLabel("Ro:")
        size_label = QtWidgets.QLabel("Size:")
        self.s = Slider('p', ['a', 'ab', 'asa'])
        self.i0 = DoubleSpinBox()
        self.r0 = DoubleSpinBox()
        self.popsize = SpinBox(200, 10)
        self.generatebutton = QtWidgets.QPushButton("Generate")
        self.plot_but = QtWidgets.QPushButton("Plot")

        initPopPara_Layout = QtWidgets.QVBoxLayout()
        initPopPara_Layout.addLayout(self.s.hbox)
        initPopPara_Layout.addLayout(FormLay([[i0_label,   self.i0],
                                              [r0_label,   self.r0],
                                              [size_label, self.popsize]]))
        initPopPara_Layout.addStretch()
        initPopPara_Layout.addWidget(self.generatebutton)
        initPopPara_Layout.addWidget(self.plot_but)
        InitPop_grpBox = QtWidgets.QGroupBox("Initial Population")
        InitPop_grpBox.setLayout(initPopPara_Layout)
        #==============================================================

        self.nbr4 = QtWidgets.QRadioButton("von Neumann(4)")
        self.nbr4.setChecked(True)
        self.nbr8 = QtWidgets.QRadioButton("Moore(8)")
        self.longrange = QtWidgets.QCheckBox("Long Range Interactions")
        self.prob_label = QtWidgets.QLabel("Probability:")
        self.probrewire = QtWidgets.QLineEdit()
        self.freq_label = QtWidgets.QLabel("Frequency:")
        self.freqrewire = QtWidgets.QLineEdit()

        nbrHd_vLayout = QtWidgets.QVBoxLayout()
        nbrHd_vLayout.addWidget(self.nbr4)
        nbrHd_vLayout.addWidget(self.nbr8)
        nbrHd_vLayout.addWidget(self.longrange)
        nbrHd_vLayout.addStretch()
        nbrHd_vLayout.addLayout(FormLay([[self.prob_label,self.probrewire],
                                         [self.freq_label,self.freqrewire]]))
        NbrHd_grpBox = QtWidgets.QGroupBox("Neighbourhood  ")
        NbrHd_grpBox.setLayout(nbrHd_vLayout)
        #=================================================================

        self.setWindowTitle("S I R Model")
        self.centralwidget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.centralwidget)
        horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        horizontalLayout.addWidget(InitPop_grpBox)
        horizontalLayout.addWidget(NbrHd_grpBox)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.setStatusBar(self.statusbar)
        self.statusbar.showMessage('Working...')


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    form = UI()
    form.show()
    sys.exit(app.exec_())
