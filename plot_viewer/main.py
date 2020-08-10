def read_config(filename='plot.cfg'):
    import configparser
    config = configparser.ConfigParser()
    config.read(filename)
    config = config._sections
    for section,key_val in config.items():
        for k,v in key_val.items():
            key_val[k] = eval(v)
    return config

def main():
    import sys
    try:
        filename = sys.argv[1]
        config = read_config(filename)
        p = config['Parameters']
        plot_param = config['Plot_Paramters']
    except:
        print('File not recognised')
        exit(1)
    from controller import interactive_plot
    interactive_plot(p, plot_param)

if __name__ == '__main__':
    main()

