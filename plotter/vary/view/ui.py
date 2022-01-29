from plotter.vary.view.controls import Controls
from plotter.vary.view.plot import Plotter
from plotter.utils.ft import BaseUI

class UI(BaseUI):
    def __init__(self, p, plot_param):
        controls = Controls(p)
        plotter = Plotter(plot_param)
        super(UI, self).__init__(controls, plotter)

if __name__ == '__main__':
    from plotter.test.vary import p, plot_param
    ui = UI(p, plot_param)
    ui.newValueSelected.connect(lambda:
            print(ui.controls.get_values()) )
    ui.show()
