
import os
import shutil
import subprocess
import sys
from helper import APP_PATH, FILE_MAIN


# clean

shutil.rmtree(os.path.join("dist"), ignore_errors=True)

# build

subprocess.run([sys.executable, "-m", "PyInstaller", os.path.join(APP_PATH, FILE_MAIN), "--onefile", "--clean"])

# copy required files
shutil.copytree(os.path.join(APP_PATH, "params"), os.path.join("dist", "params"))
