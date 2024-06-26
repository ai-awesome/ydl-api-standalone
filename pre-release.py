import os
import shutil

from helper import ZIP_FILE

if __name__ == "__main__":
    if os.path.exists("dist"):
        temp_zip_file = "temp_" + ZIP_FILE
        shutil.make_archive(temp_zip_file, "zip", "dist")
        shutil.move(temp_zip_file + ".zip", "dist/" + ZIP_FILE + ".zip")
    else:
        print("dist folder not exist, please build first")

