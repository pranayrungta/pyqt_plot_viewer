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
    except Exception:
        import traceback
        print(traceback.format_exc())
        input()


def plot(wd, config):
    from plot_viewer.controller import interactive_plot
    interactive_plot(wd, config)

# {action : function} map
links = {'plot': plot}


if __name__ == '__main__':
    main(links)
