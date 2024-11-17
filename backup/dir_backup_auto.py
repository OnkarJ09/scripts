import schedule
import shutil
import time
import os

def backup_folder(src_dir, dest_dir):
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    for file in os.listdir(src_dir):
        full_file_name = os.path.join(src_dir, file)
        if os.path.isfile(full_file_name):
            shutil.copy(full_file_name, dest_dir)
            print(f"Backed up {file} to {dest_dir}")

# Back up folder's location
source = "main_folder"
destination = "destination_folder"

# Schedule the backup for every 1 hour
schedule.every(1).hours.do(backup_folder(source, destination))
try:
    while True:
        schedule.run_pending()
        time.sleep(1)
except KeyboardInterrupt:
    print("Scheduler stopped.")
