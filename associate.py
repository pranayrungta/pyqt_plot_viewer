import winreg

def get_cmd_icon():
    import sys, pathlib
    executable = sys.executable
    if executable.endswith('python.exe'):
        executable = executable[:-10] + 'pythonw.exe'
    launch_cmd = f'"{executable}" -m library_name "%1" %*'
    cwd = pathlib.Path(__file__).parent
    icon_path = str(cwd/'icon.ico')
    return launch_cmd, icon_path

def associate():
    SZ = winreg.REG_SZ
    with winreg.CreateKey(winreg.HKEY_CURRENT_USER,
                          r"Software\Classes\.plt") as k:
        winreg.SetValue(k, "", SZ, "phd_plot")
        winreg.SetValueEx(k, "Content Type", 0, SZ, "application/json")
        winreg.SetValueEx(k, "PerceivedType", 0, SZ, "document")
        with winreg.CreateKey(k, "OpenWithProgIds") as openwith:
            winreg.SetValueEx(openwith, "phd_plot", 0, winreg.REG_NONE, b'')

    launch_cmd, icon_path = get_cmd_icon()
    with winreg.CreateKey(winreg.HKEY_CURRENT_USER,
                          r"Software\Classes\phd_plot") as k:
        winreg.SetValue(k, "", SZ, "Plots made during PhD")
        with winreg.CreateKey(k, r"shell\open\command") as launchk:
            winreg.SetValue(launchk, "", SZ, launch_cmd)
        with winreg.CreateKey(k, r"DefaultIcon") as icon:
            winreg.SetValue(icon, "", SZ, launch_cmd)

def notify_window():
    from win32com.shell import shell, shellcon
    shell.SHChangeNotify(shellcon.SHCNE_ASSOCCHANGED,
                         shellcon.SHCNF_IDLIST, None, None)

def remove_association():
    keys = [r'Software\Classes\.plt\OpenWithProgIds',
            r'Software\Classes\.plt',
            r'Software\Classes\phd_plot\shell\open\command',
            r'Software\Classes\phd_plot\shell\open',
            r'Software\Classes\phd_plot\shell',
            r'Software\Classes\phd_plot\DefaultIcon',
            r'Software\Classes\phd_plot',  ]
    for key in keys:
        winreg.DeleteKey(winreg.HKEY_CURRENT_USER, key)

def cli_launch(assoc=True):
    if assoc: associate()
    else: remove_association()
    notify_window()
