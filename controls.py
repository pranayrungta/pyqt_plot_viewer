from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt

class Slider(QtWidgets.QWidget):
    def __init__(self, label="p:", vals=['a','b','c'], *args, **kwargs):
        super(Slider, self).__init__(*args, **kwargs)
        slider = QtWidgets.QSlider(Qt.Horizontal)
        slider.setSingleStep(1)
        slider.setRange(0, len(vals)-1)
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
        self.setLayout(self.hbox)

    def updateLabel(self, i):
        self.current_value.setText(self.vals[i])
        print( self.vals[ self.slider.value() ] )

    def value(self):
        print(self.slider.value())
        return self.vals[ self.slider.value() ]



class Controls(QtWidgets.QWidget):
    def __init__(self, p, *args, **kwargs):#parameters
        super(Controls, self).__init__(*args, **kwargs)
        self.comboBox = QtWidgets.QComboBox()
        self.comboBox.addItems(p.keys())
        self.comboBox.activated.connect(self.getComboValue)

        para_layout = QtWidgets.QVBoxLayout()
        para_layout.addWidget(self.comboBox)
        para_layout.addSpacing(15)
        self.sld_wd = {}
        for k, v in p.items():
            self.sld_wd[k] = Slider(k, v)
            para_layout.addWidget(self.sld_wd[k])
            para_layout.addSpacing(15)
        self.setLayout(para_layout)

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
    # form = UI(p)
    # form.show()
    s = Controls(p)
    s.show()
    app.exec_()
    print('done')
