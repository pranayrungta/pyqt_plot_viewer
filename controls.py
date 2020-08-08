from PyQt5.QtWidgets import (QWidget, QLabel, QSlider, QComboBox,
                             QHBoxLayout, QVBoxLayout, QApplication)
from PyQt5.QtCore import Qt

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

class Controls(QWidget):
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
        self.on_change_callback = lambda:None
        self.vary.activated.connect(self.change_vary)
        for sld in self.sld_wd.values():
            sld.slider.valueChanged.connect(self.call_on_change)
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
        self.call_on_change()

    def get_values(self):
        const = self.constants.copy()
        const.update( { k:slider.value() for k, slider in
                        self.sld_wd.items() }  )
        var = self.vary.currentText()
        const.pop(var)
        variable = (var, self.sld_wd[var].vals)
        return variable, const

    def call_on_change(self):
        print(self.get_values())
        self.on_change_callback()


if __name__ == '__main__':
    p = {'wire': ['static', 'dynamic'],
         'c'   : ['1'],
         'k'   : ['2', '4'],
         'n'   : ['700'],
         'b'   : ['0', '-0.04', '-0.08', '-0.1'],
         'p'   : ['0', '0.1', '0.3', '0.5', '0.7'] }
    import sys
    app = QApplication(sys.argv)
    # form = UI(p)
    # form.show()
    s = Controls(p)
    s.show()
    app.exec_()
    print('done')
