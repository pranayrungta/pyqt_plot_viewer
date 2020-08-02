from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt

class Slider:
    def __init__(self, label="p:", vals=['a','b','c']):
        slider = QtWidgets.QSlider(Qt.Horizontal)
        slider.setSingleStep(1)
        slider.setRange(0, len(vals)-1)
        # slider.setFocusPolicy(Qt.NoFocus)
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

    def updateLabel(self, i):
        self.current_value.setText(self.vals[i])
        print( self.vals[ self.slider.value() ] )

    def value(self):
        print(self.slider.value())
        return self.vals[ self.slider.value() ]



class UI(QtWidgets.QMainWindow):
    def __init__(self, p): # parameters
        super().__init__()

        self.comboBox = QtWidgets.QComboBox()
        self.comboBox.addItems(p.keys())
        self.comboBox.activated.connect(self.getComboValue)

        para_layout = QtWidgets.QVBoxLayout()
        para_layout.addStretch()
        para_layout.addWidget(self.comboBox)

        self.sld_wd = {}
        for k, v in p.items():
            self.sld_wd[k] = Slider(k, v)
            para_layout.addLayout(self.sld_wd[k].hbox)

        para_layout.addStretch()
        para_grpBox = QtWidgets.QGroupBox("Parameters")
        para_grpBox.setLayout(para_layout)
        #==============================================================

        self.longrange = QtWidgets.QCheckBox("Plot here...")
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
        horizontalLayout.addWidget(para_grpBox)
        horizontalLayout.addWidget(NbrHd_grpBox)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.setStatusBar(self.statusbar)
        self.statusbar.showMessage('Working...')

    def getComboValue(self):
        print((self.comboBox.currentText(), self.comboBox.currentIndex()))


if __name__ == '__main__':
    p = {'wire': ['static', 'dynamic'],
         'c'   : ['1'],
         'k'   : ['2', '4'],
         'n'   : ['100'],
         'b'   : ['0', '-0.04', '-0.08', '-0.1'],
         'p'   : ['0', '0.1', '0.3', '0.5', '0.7'] }
    import sys
    app = QtWidgets.QApplication(sys.argv)
    form = UI(p)
    form.show()
    app.exec_()
    print('done')
