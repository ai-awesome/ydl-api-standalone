import os
import shutil

from helper import ZIP_FILE

if __name__ == "__main__":
    if os.path.exists("dist"):
        shutil.make_archive("dist/" + ZIP_FILE, "zip", "dist")
    else:
        print("dist folder not exist, please build first")

