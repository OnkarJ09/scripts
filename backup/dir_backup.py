import shutil
import os

def backup_folder(src_dir, dest_dir):
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    for file in os.listdir(src_dir):
        full_file_name = os.path.join(src_dir, file)
        if os.path.isfile(full_file_name):
            shutil.copy(full_file_name, dest_dir)
            print(f"Backed up {file} to {dest_dir}")

source = "save/"
destination = "~/Downloads"

backup_folder(source, destination)
