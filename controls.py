from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt

class Slider(QtWidgets.QWidget):
    def __init__(self, label="p:", vals=['a','b','c'], *args, **kwargs):
        super(Slider, self).__init__(*args, **kwargs)

        self.vals=vals
        self.label = QtWidgets.QLabel(label)
        slider = QtWidgets.QSlider(Qt.Horizontal)
        slider.setSingleStep(1)
        slider.setRange(0, len(vals)-1)
        slider.valueChanged.connect(lambda i:
                self.current_value.setText(self.vals[i]))
        self.slider = slider
        self.current_value = QtWidgets.QLabel(vals[0])

        hbox = QtWidgets.QHBoxLayout()
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



class Controls(QtWidgets.QWidget):
    def __init__(self, p, *args, **kwargs):#parameters
        super(Controls, self).__init__(*args, **kwargs)

        const = ["Constants:"]
        self.constants = {}
        self.vary = QtWidgets.QComboBox()
        self.sld_wd = {}
        for k, v in p.items():
            if len(v)>1:
                self.sld_wd[k] = Slider(k, v)
            elif len(v)==1:
                const.append( f'{k} = {v[0]}' )
                self.constants[k] = v[0]
        self.vary.addItems(self.sld_wd.keys())
        const = '\n'.join(const)
        const = QtWidgets.QLabel(const)

        self.variable = self.vary.currentText()
        self.on_change_callback = lambda:None

        para_layout = QtWidgets.QVBoxLayout()
        para_layout.addWidget(const)
        para_layout.addSpacing(15)
        para_layout.addWidget(self.vary)
        para_layout.addSpacing(15)
        for sld in self.sld_wd.values():
            para_layout.addWidget(sld)
            para_layout.addSpacing(15)
        self.setLayout(para_layout)

        self.vary.activated.connect(self.change_vary)
        for sld in self.sld_wd.values():
            sld.slider.valueChanged.connect(self.call_on_change)
        self.change_vary()

    def change_vary(self):
        var = self.vary.currentText()
        self.sld_wd[self.variable].show()
        self.sld_wd[var].hide()
        self.variable = var
        self.call_on_change()

    def get_values(self):
        const = self.constants.copy()
        const.update({k:self.sld_wd[k].value()
                      for k in self.sld_wd})
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
