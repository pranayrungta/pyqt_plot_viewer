from PyQt5 import QtWidgets
from plot_viewer.view.ui import UI
from plot_viewer.model import get_data

class MyApp(UI):
    def __init__(self, p, plot_param): # parameters
        super(MyApp, self).__init__(p, plot_param)
        self.newValueSelected.connect(self.plot_interactive)
        self.plot_interactive()

    def plot_interactive(self):
        variable, const = self.controls.get_values()
        dfs, title = get_data(variable, const)
        self.plotter.set_data(dfs, title)


def interactive_plot(p, plot_param):
    app = QtWidgets.QApplication([])
    ui = MyApp(p, plot_param)
    ui.show()
    app.exec_()
