import os
from pathlib import Path
import subprocess
import sys

APP_DIR = Path(os.path.abspath(os.path.dirname(__file__)))
APP_NAME = "ydl_api_ng"
APP_PATH = APP_DIR / APP_NAME
PARAM_PATH = APP_PATH / "params"
DIST_PATH = APP_PATH / "dist"
ZIP_FILE = APP_NAME + "_dist"
FILE_NAME = "main"
FILE_MAIN = FILE_NAME + ".py"
