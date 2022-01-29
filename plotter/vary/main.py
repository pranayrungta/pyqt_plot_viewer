from PyQt5 import QtWidgets
from plotter.vary.view import UI
from plotter.vary.model import Model

class MyApp:
    def __init__(self, wd, config): # parameters
        # self.wd = wd
        self.ui = UI(config['Parameters'], config['Plot_Paramters'])
        self.model = Model(wd, config['Data_Source'])
        self.ui.newValueSelected.connect(self.plot_interactive)
        self.ui.newValueSelected.emit()
        self.ui.show()

    def plot_interactive(self):
        variable, const = self.ui.controls.get_values()
        dfs, title = self.model.get_data(variable, const)
        self.ui.plotter.set_data(dfs, title)


def interactive_plot(wd, config):
    app = QtWidgets.QApplication([])
    myapp = MyApp(wd, config)
    app.exec_()
