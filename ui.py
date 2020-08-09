from PyQt5 import QtWidgets
from controls import Controls
from plot import Plotter

class UI(QtWidgets.QDialog):
    def __init__(self, p, plot_param): # parameters
        super(UI, self).__init__()
        self.controls = Controls(p)
        self.plotter = Plotter()

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

        self.controls.on_change_callback=self.plot_interactive
        self.plot_param = plot_param
        self.plot_interactive()

    def plot_interactive(self):
        from model import get_data
        variable, const = self.controls.get_values()
        dfs, title = get_data(variable, const)
        self.plotter.set_data(dfs, self.plot_param, title)


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
