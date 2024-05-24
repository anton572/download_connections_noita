import subprocess
import sys
def im(name):
    try:
        return __import__(name)
    except ImportError:
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", name])
            return __import__(name)
        except Exception as e:
            print(f"Failed to install and import {name}: {e}")
            return None
