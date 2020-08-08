from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from controls import Controls
from plot import Plotter

class UI(QtWidgets.QMainWindow):
    def __init__(self, p, plot_param): # parameters
        super().__init__()
        self.setWindowTitle("Plot Viewer")
        self.centralwidget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.centralwidget)
        self.setGeometry(100,50,1200,650)
        #=================================================================
        self.controls = Controls(p)
        self.plotter = Plotter()
        self.plotter.fig.tight_layout()
        #==============================================================
        para_layout = QtWidgets.QVBoxLayout()
        para_layout.addStretch()
        para_layout.addWidget(self.controls)
        para_layout.addStretch()
        param = QtWidgets.QWidget()
        param.setLayout(para_layout)
        param.setFixedWidth(200)
        #=================================================================
        horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        horizontalLayout.addWidget(param)
        horizontalLayout.addWidget(self.plotter)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.setStatusBar(self.statusbar)
        self.statusbar.showMessage('Working...')
        #=================================================================
        self.controls.on_change_callback=self.plot_interactive
        self.plot_param = plot_param

    def plot_interactive(self):
        # print('running...')
        from model import get_data
        variable, const = self.controls.get_values()
        dfs = get_data(variable, const)
        self.plotter.set_data(dfs, self.plot_param)


if __name__ == '__main__':
    p = {'wire': ['static', 'dynamic'],
         'c'   : ['1'],
         'k'   : ['2', '4'],
         'n'   : ['100'],
         'b'   : ['0', '-0.04', '-0.08', '-0.1'],
         'p'   : ['0', '0.1', '0.3', '0.5', '0.7'] }
    from plot_test import test_get_data
    dfs = test_get_data()
    import sys
    app = QtWidgets.QApplication(sys.argv)
    plot_analyse = UI(p)
    plot_analyse.plotter.set_data(dfs)
    plot_analyse.show()
    app.exec_()
    print('done')
