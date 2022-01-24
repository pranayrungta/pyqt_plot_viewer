from PyQt5 import QtWidgets
from plot_viewer.view.ui import UI
from plot_viewer.model import get_data
from pathlib import Path

class MyApp(UI):
    def __init__(self, p, plot_param, filename): # parameters
        super(MyApp, self).__init__(p, plot_param)
        self.wd = Path(filename).resolve().parent
        self.newValueSelected.connect(self.plot_interactive)
        self.plot_interactive()

    def plot_interactive(self):
        variable, const = self.controls.get_values()
        dfs, title = get_data(variable, const, self.wd)
        self.plotter.set_data(dfs, title)


def interactive_plot(p, plot_param, filename):
    app = QtWidgets.QApplication([])
    ui = MyApp(p, plot_param, filename)
    ui.show()
    app.exec_()
