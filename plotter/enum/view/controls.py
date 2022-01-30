from PyQt5.QtWidgets import (QWidget, QLabel, QVBoxLayout)
from PyQt5.QtCore import pyqtSignal
from plotter.utils.ft import seperate_const, const_label, Slider

class Controls(QWidget):
    newValueSelected = pyqtSignal()

    def __init__(self, p, *args, **kwargs):#parameters
        super(Controls, self).__init__(*args, **kwargs)

        self.constants, var = seperate_const(p)
        self.const_label = QLabel( const_label(self.constants) )
        self.sld_wd = {}
        for k, vals in var.items():
            self.sld_wd[k] = Slider(k, vals)
        for sld in self.sld_wd.values():
            sld.slider.valueChanged.connect(self.newValueSelected.emit)
        self.setup_layout()

    def setup_layout(self):
        layout = QVBoxLayout()
        layout.addWidget(self.const_label)
        layout.addSpacing(15)
        for sld in self.sld_wd.values():
            layout.addWidget(sld)
            layout.addSpacing(15)
        self.setLayout(layout)

    def get_values(self):
        const = self.constants.copy()
        const.update( { k:slider.value() for k, slider in
                        self.sld_wd.items() }  )
        return const

if __name__ == '__main__':
    p = {'wire': ['static', 'dynamic', 'regular'],
         'c'   : ['1'],
         'k'   : ['2'],
         'n'   : ['100'],
         'b'   : ['-0.035'],
         'p'   : ['0', '0.8'],
         'N1'  : ['1', '30']}
    s = Controls(p)
    s.newValueSelected.connect(lambda: print(s.get_values()) )
    s.show()
