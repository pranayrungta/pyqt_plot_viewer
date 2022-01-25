from PyQt5 import QtWidgets
from plot_viewer.view.ui import UI
from plot_viewer.model import get_data

class MyApp(UI):
    def __init__(self, wd, config): # parameters
        super(MyApp, self).__init__(config['Parameters'],
                                config['Plot_Paramters'])
        self.wd = wd
        self.newValueSelected.connect(self.plot_interactive)
        self.plot_interactive()

    def plot_interactive(self):
        variable, const = self.controls.get_values()
        dfs, title = get_data(variable, const, self.wd)
        self.plotter.set_data(dfs, title)


def interactive_plot(wd, config):
    app = QtWidgets.QApplication([])
    ui = MyApp(wd, config)
    ui.show()
    app.exec_()
