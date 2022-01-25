from PyQt5 import QtWidgets
from plot_viewer.view.ui import UI
from plot_viewer.model import get_data

class MyApp:
    def __init__(self, wd, config): # parameters
        self.wd = wd
        self.ui = UI(config['Parameters'],
                     config['Plot_Paramters'])
        print('running', flush=True)
        self.ui.newValueSelected.connect(self.plot_interactive)
        self.ui.newValueSelected.emit()
        self.ui.show()

    def plot_interactive(self):
        print('called', flush=True)
        variable, const = self.ui.controls.get_values()
        dfs, title = get_data(variable, const, self.wd)
        self.ui.plotter.set_data(dfs, title)


def interactive_plot(wd, config):
    app = QtWidgets.QApplication([])
    myapp = MyApp(wd, config)
    app.exec_()
