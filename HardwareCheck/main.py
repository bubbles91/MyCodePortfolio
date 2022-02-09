import math
import platform
import psutil
import cpuinfo
import tkinter.messagebox as tkmb
import wmi

def write_slogan():
    c = wmi.WMI()
    systeminfogpu = c.Win32_VideoController()[0]
    systeminfoboard = c.Win32_BaseBoard()[0]
    message=str((f"Computer Name: {platform.node()}\n") + str(f"Platform: {platform.platform()}\n") +
        str(f'CPU Brand Info: {cpuinfo.get_cpu_info()["brand_raw"]}\n') + str(f"CPU cores: {psutil.cpu_count()}\n") +
        str(f"Ram installed: {math.ceil(psutil.virtual_memory().total/1073741824)} GB\n") +
        str(f"GPU: {systeminfogpu.Name}\n") + str(f"MotherBoard: {systeminfoboard.Product} {systeminfoboard.Manufacturer}\n"))


    tkmb.showinfo("Output", message)

write_slogan()