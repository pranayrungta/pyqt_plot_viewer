def read_config(filename='plot.plt'):
    import configparser
    config = configparser.ConfigParser()
    config.read(filename)
    config = config._sections
    for section,key_val in config.items():
        for k,v in key_val.items():
            key_val[k] = eval(v)
    config.update(config.pop('Program'))
    return config

def default_action(wd, config):
    raise KeyError('Action not found')

def main(links):
    import sys
    try:
        filename = sys.argv[1]
        config = read_config(filename)
        from pathlib import Path
        wd = Path(filename).resolve().parent
    except:
        print('File not recognised :', sys.argv[1:])
        return
    try:
        action = links.get(config['action'], default_action)
        action(wd, config)
    except:
        import traceback
        print(traceback.format_exc())
        input('Press enter to exit !!!')
        input()

def plot(wd, config):
    from plotter.vary.main import interactive_plot
    interactive_plot(wd, config)

def plot_spt(wd, config):
    from plotter.spt.main import interactive_plot
    interactive_plot(wd, config)

def plot_enum(wd, config):
    from plotter.enum.main import interactive_plot
    interactive_plot(wd, config)

# {action : function} map
links = {'plot': plot,
         'plot-spt': plot_spt,
         'plot-enum': plot_enum }


if __name__ == '__main__':
    main(links)
    pass
