from PyQt5 import QtWidgets
from controls import Controls
from plot import Plotter

class UI(QtWidgets.QDialog):
    def __init__(self, p, plot_param): # parameters
        super(UI, self).__init__()
        self.controls = Controls(p)
        self.plotter = Plotter(plot_param)
        self.set_style()
        self.controls.on_change_callback=self.plot_interactive
        self.plot_interactive()

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

    def plot_interactive(self):
        from model import get_data
        variable, const = self.controls.get_values()
        dfs, title = get_data(variable, const)
        self.plotter.set_data(dfs, title)


def interactive_plot(p, plot_param):
    app = QtWidgets.QApplication([])
    ui = UI(p, plot_param)
    ui.show()
    app.exec_()
