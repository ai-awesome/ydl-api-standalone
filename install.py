import subprocess
import os
import sys

# Clone the repository
subprocess.run(["git", "clone", "https://github.com/Totonyus/ydl_api_ng"])

# Create a virtual environment
subprocess.run([sys.executable, "-m", "venv", "venv"])

# Activate the virtual environment
if os.name == "posix":
    subprocess.run(["source", "venv/bin/activate"])
else:
    subprocess.run(["venv\\Scripts\\activate.bat"])

# Install PyInstaller
subprocess.run([sys.executable, "-m", "pip", "install", "pyinstaller"])

# Install requirements
subprocess.run([sys.executable, "-m", "pip", "install", "-r", "ydl_api_ng/pip_requirements"])

# Install hooks requirements
subprocess.run([sys.executable, "-m", "pip", "install", "-r", "ydl_api_ng/params/hooks_requirements"])
