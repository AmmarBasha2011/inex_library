import platform
import os
import subprocess
   
class System:
    """
    A class for managing system operations.
    """
    
    @staticmethod
    def hibernate():
        """
        Hibernate the system.

        Raises:
        - NotImplementedError: If the OS is not supported (only Windows is supported).
        """
        system = platform.system()
        if system == "Windows":
            os.system("shutdown /h")
        else:
            raise NotImplementedError("Unsupported OS")

    @staticmethod
    def restart():
        """
        Restart the system.

        Raises:
        - NotImplementedError: If the OS is not supported (only Windows is supported).
        """
        system = platform.system()
        if system == "Windows":
            os.system("shutdown /r /t 1")
        else:
            raise NotImplementedError("Unsupported OS")

    @staticmethod
    def shutdown():
        """
        Shutdown the system.

        Raises:
        - NotImplementedError: If the OS is not supported (Windows, Linux, and macOS are supported).
        """
        system = platform.system()
        if system == "Windows":
            subprocess.run(["shutdown", "/s", "/t", "1"])
        elif system == "Linux" or system == "Darwin":
            subprocess.run(["sudo", "shutdown", "-h", "now"])
        else:
            raise NotImplementedError("Unsupported OS")
        
    @staticmethod
    def log_off():
        """
        Log off the current user.

        Raises:
        - NotImplementedError: If the OS is not supported (only Windows is supported).
        """
        system = platform.system()
        if system == "Windows":
            os.system("shutdown /l")
        else:
            raise NotImplementedError("Unsupported OS")
