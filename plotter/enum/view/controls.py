from PyQt5.QtWidgets import (QWidget, QLabel, QVBoxLayout,
                             QRadioButton, QButtonGroup)
from PyQt5.QtCore import pyqtSignal
from plotter.utils.ft import seperate_const, const_label, Slider

class Controls(QWidget):
    newValueSelected = pyqtSignal()

    def __init__(self, p):#parameters
        super(Controls, self).__init__()
        self.p = p['values']
        self.text = [self.get_val_text(i) for i in self.p]
        self.buts = [QRadioButton(i) for i in self.text]
        self.grp = QButtonGroup()
        for i in self.buts:
            self.grp.addButton(i)
            i.clicked.connect(self.select)
        self.setup_layout()
        self.i=0

    def select(self):
        self.newValueSelected.emit()

    def get_val_text(self, val):
        t, vals = val
        l = [t]
        for title, param in vals.items():
            param = ' '.join(f'{k}={v}' for k,v in param.items())
            l.append(f'{title} : {param}')
        l = '\n\t'.join(l)
        return l


    def setup_layout(self):
        layout = QVBoxLayout()
        for but in self.buts:
            layout.addWidget(but)
            layout.addSpacing(15)
        self.setLayout(layout)

    def get_values(self):
        s = self.grp.checkedButton().text()
        i = self.text.index(s)
        return self.p[i]

if __name__ == '__main__':
    p = {'values': [
  ('plot title1', {'title1': {'id': 1}, 'title2': {'id': 1}, 'title3': {'id': 1}}),
  ('plot title2', {'title1': {'id': 1}, 'title2': {'id': 1}, 'title3': {'id': 1}}),
  ('plot title3', {'title1': {'id': 1}, 'title2': {'id': 1}, 'title3': {'id': 1}})]}
    s = Controls(p)
    s.newValueSelected.connect(lambda: print(s.get_values()) )
    s.show()
    s.buts[0].click()
