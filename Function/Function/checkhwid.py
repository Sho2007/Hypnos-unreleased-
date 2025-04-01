import subprocess
import platform

def get_hwid():
    if platform.system() == "Windows":
        # Use the Windows Management Instrumentation Command (wmic)
        try:
            hwid = subprocess.check_output("wmic csproduct get uuid", shell=True)
            hwid = hwid.decode().split("\n")[1].strip()
            return hwid
        except Exception as e:
            return f"Error retrieving HWID: {e}"
    elif platform.system() == "Linux":
        # Retrieve the DMI board serial number (works on most Linux distros)
        try:
            hwid = subprocess.check_output("cat /sys/class/dmi/id/product_uuid", shell=True)
            return hwid.decode().strip()
        except Exception as e:
            return f"Error retrieving HWID: {e}"
    elif platform.system() == "Darwin":
        # Use system_profiler on macOS to get hardware UUID
        try:
            hwid = subprocess.check_output("system_profiler SPHardwareDataType | grep 'Hardware UUID'", shell=True)
            return hwid.decode().split(":")[1].strip()
        except Exception as e:
            return f"Error retrieving HWID: {e}"
    else:
        return "Unsupported Operating System"

if __name__ == "__main__":
    hwid = get_hwid()
    print(f"HWID: {hwid}")
