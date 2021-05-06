import os
import sys
from pastry.core.queue import Queue

print("OS name:", os_name := sys.platform)

venv_command = ". venv/bin/activate" if os_name in ["linux", "darwin"] else "venv\\Scripts\\activate"

def setup_venv():
    python_executable = sys.executable
    print(f"Python executable: {python_executable}")

    if os.path.exists("venv"):
        print("Virtual environment already exists!\n Updating dependencies...")
        os.system(f"{venv_command} && pip install -r requirements.txt")
    else:
        print("Virtual environment not found, creating... ")
        os.system(f'"{python_executable}" -m venv venv && {venv_command} && pip install -r requirements.txt')


if __name__ == "__main__":
    setup_venv()