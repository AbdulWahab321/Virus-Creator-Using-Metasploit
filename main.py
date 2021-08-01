import sys
import ctypes
import colorama
from termcolor import cprint
colorama.init()
def isAdmin():
    """ Return True/Flase """
    is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    return is_admin

if sys.platform.lower() == "linux":
    import mainProgram
    mainProgram.start()
elif "win" in sys.platform.lower():
    if isAdmin():
        import mainProgramWindows
        mainProgramWindows.start()
    else:
        cprint("Please run command prompt as administrator an run again","red",attrs=["bold"])



