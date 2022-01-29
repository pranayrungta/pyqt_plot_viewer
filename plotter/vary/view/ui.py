from PyQt5 import QtWidgets
from plotter.vary.view.controls import Controls
from plotter.vary.view.plot import Plotter

class UI(QtWidgets.QDialog):
    def __init__(self, p, plot_param): # parameters
        super(UI, self).__init__()
        self.controls = Controls(p)
        self.plotter = Plotter(plot_param)
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



if __name__ == '__main__':
    from plotter.tests import p, plot_param
    app = QtWidgets.QApplication([])
    ui = UI(p, plot_param)
    ui.newValueSelected.connect(lambda:
            print(ui.controls.get_values()) )
    ui.show()
    app.exec_()
    print('done')
