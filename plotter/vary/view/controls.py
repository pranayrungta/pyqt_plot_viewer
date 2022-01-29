from PyQt5.QtWidgets import (QWidget, QLabel, QComboBox,
                             QHBoxLayout, QVBoxLayout)
from PyQt5.QtCore import pyqtSignal
from plotter.utils.ft import seperate_const, const_label, Slider


class Controls(QWidget):
    newValueSelected = pyqtSignal()

    def __init__(self, p, *args, **kwargs):#parameters
        super(Controls, self).__init__(*args, **kwargs)

        self.constants, var = seperate_const(p)
        self.const_label = QLabel( const_label(self.constants) )
        self.vary = QComboBox()
        self.vary.addItems(var.keys())
        self.sld_wd = {}
        for k, vals in var.items():
            self.sld_wd[k] = Slider(k, vals)

        self.variable = self.vary.currentText()
        # self.on_change_callback = lambda:None
        self.vary.activated.connect(self.change_vary)
        for sld in self.sld_wd.values():
            sld.slider.valueChanged.connect(self.newValueSelected.emit)
        self.change_vary()
        self.setup_layout()

    def setup_layout(self):
        para_layout = QVBoxLayout()
        para_layout.addWidget(self.const_label)
        para_layout.addSpacing(15)
        vary_lbl = QLabel( 'vary:' )
        vary_layout = QHBoxLayout()
        vary_layout.addWidget(vary_lbl)
        vary_layout.addWidget(self.vary, stretch=True)
        para_layout.addLayout(vary_layout)
        para_layout.addSpacing(15)
        for sld in self.sld_wd.values():
            para_layout.addWidget(sld)
            para_layout.addSpacing(15)
        self.setLayout(para_layout)

    def change_vary(self):
        var = self.vary.currentText()
        self.sld_wd[self.variable].show()
        self.sld_wd[var].hide()
        self.variable = var
        self.newValueSelected.emit()

    def get_values(self):
        const = self.constants.copy()
        const.update( { k:slider.value() for k, slider in
                        self.sld_wd.items() }  )
        var = self.vary.currentText()
        const.pop(var)
        variable = (var, self.sld_wd[var].vals)
        return variable, const


if __name__ == '__main__':
    p = {'c'   : ['1'],
         'n'   : ['700'],
         'wire': ['static', 'dynamic'],
         'k'   : ['2', '4'],
         'b'   : ['0', '-0.04', '-0.08', '-0.1'],
         'p'   : ['0', '0.1', '0.3', '0.5', '0.7'] }
    s = Controls(p)
    s.newValueSelected.connect(lambda: print(s.get_values()) )
    s.show()
