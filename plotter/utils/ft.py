from PyQt5.QtWidgets import QWidget, QLabel, QSlider, QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets

def seperate_const(p):
    var, const = {}, {}
    for k,v in p.items():
        if len(v)==1:
            const[k] = v[0]
        elif len(v)>1: var[k]=v
    return const, var

def const_label(const={'c': '1', 'n': '100'}):
    const_label = ["Constants:"]
    const_label.extend( f'{k} = {v}'
                        for k,v in const.items())
    const_label = '\n\t'.join(const_label)
    return const_label


class Slider(QWidget):
    def __init__(self, label="p:", vals=['a','b','c'], *args, **kwargs):
        super(Slider, self).__init__(*args, **kwargs)

        self.vals=vals
        self.label = QLabel(label)
        slider = QSlider(Qt.Horizontal)
        slider.setSingleStep(1)
        slider.setRange(0, len(vals)-1)
        slider.valueChanged.connect(lambda i:
                self.current_value.setText(self.vals[i]))
        self.slider = slider
        self.current_value = QLabel(vals[0])

        hbox = QHBoxLayout()
        hbox.addWidget(self.label)
        hbox.addWidget(self.slider)
        hbox.addWidget(self.current_value)
        self.setLayout(hbox)

    def hide(self):
        self.label.hide()
        self.slider.hide()
        self.current_value.hide()

    def show(self):
        self.label.show()
        self.slider.show()
        self.current_value.show()

    def value(self):
        return self.vals[ self.slider.value() ]


class BaseUI(QtWidgets.QDialog):
    def __init__(self, controls, plotter):
        super(BaseUI, self).__init__()
        self.controls = controls
        self.plotter = plotter
        self.newValueSelected = self.controls.newValueSelected
        self.set_style()

    def set_style(self):
        para_layout = QtWidgets.QVBoxLayout()
        para_layout.addStretch()
        para_layout.addWidget(self.controls)
        para_layout.addStretch()
        param = QtWidgets.QWidget()
        param.setLayout(para_layout)
        param.setFixedWidth(200)

        horizontalLayout = QtWidgets.QHBoxLayout()
        horizontalLayout.addWidget(param)
        horizontalLayout.addWidget(self.plotter)
        self.setWindowTitle("Plot Viewer")
        self.setGeometry(100,50,1200,650)
        self.setLayout(horizontalLayout)
