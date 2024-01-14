import psutil
import platform
import speedtest
import socket
import wmi
from screeninfo import get_monitors

def get_installed_software():
    return [program.name for program in psutil.process_iter(['name'])]

def get_internet_speed():
    st = speedtest.Speedtest()
    download_speed = st.download() / 1024 / 1024
    upload_speed = st.upload() / 1024 / 1024
    return download_speed, upload_speed

def get_screen_resolution():
    monitors = get_monitors()
    resolutions = [(monitor.width, monitor.height) for monitor in monitors]
    return resolutions

def get_cpu_model():
    return platform.processor()

def get_cpu_info():
    cpu_info = {}
    cpu_info['cores'] = psutil.cpu_count(logical=False)
    cpu_info['threads'] = psutil.cpu_count(logical=True)
    return cpu_info

def get_gpu_info():
    try:
        w = wmi.WMI()
        gpu_info = w.Win32_VideoController()[0].name
        return gpu_info
    except Exception as e:
        return None

def get_ram_size():
    ram_info = psutil.virtual_memory()
    return ram_info.total // (1024**3)

def get_screen_size():
    monitors = get_monitors()
    if monitors:
        return round((monitors[0].width_mm**2 + monitors[0].height_mm**2)**0.5 / 25.4, 2)  # Convert mm to inches
    return None

def get_mac_address(interface='Ethernet'):
    try:
        mac = ':'.join(['{:02x}'.format((int(mac_part, 16))) for mac_part in psutil.net_if_addrs()[interface][0].address.split(':')])
        return mac
    except Exception as e:
        return None

def get_public_ip():
    try:
        public_ip = socket.gethostbyname(socket.gethostname())
        return public_ip
    except Exception as e:
        return None

def get_windows_version():
    return platform.system() + ' ' + platform.version()


print("1. Installed Software:", get_installed_software())
print("2. Internet Speed (Download, Upload):", get_internet_speed())
print("3. Screen Resolution:", get_screen_resolution())
print("4. CPU Model:", get_cpu_model())
print("5. CPU Info (Cores, Threads):", get_cpu_info())
print("6. GPU Info:", get_gpu_info())
print("7. RAM Size (GB):", get_ram_size())
print("8. Screen Size (in inches):", get_screen_size())
print("9. Ethernet Mac Address:", get_mac_address('Ethernet'))
print("10. Public IP Address:", get_public_ip())
print("11. Windows Version:", get_windows_version())
