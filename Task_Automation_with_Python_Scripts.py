# TASK 3: Task Automation with Python Scripts

# Goal: Automate a small, real-life repetitive task.
# Pick One of These Ideas:
# ● Move all .jpg files from a folder to a new folder.
# ● Extract all email addresses from a .txt file and save them to another file.
# ● Scrape the title of a fixed webpage and save it.


import os
import shutil

# input folder
source_folder = input("Enter the folder path: ").strip() 
# check immediately after weather folder exist or not

if not os.path.isdir(source_folder):
    print("Source folder does not exist. Exiting.")
    exit()

# destination folder
dest_folder = input("Enter destination folder path: ").strip() 
os.makedirs(dest_folder, exist_ok=True)

# counters and list
moved_count = 0
moved_files = []
for filename in os.listdir(source_folder):
    if filename.lower().endswith(('.jpg', '.jpeg')):
        source_path = os.path.join(source_folder, filename)
        if os.path.isfile(source_path):
            dest_path = os.path.join(dest_folder, filename)

            # Skip file if already exists in destination
            if os.path.exists(dest_path):
                print(f"Skipped {filename}: already exists in destination.")
                continue

            try:
                shutil.move(source_path, dest_path)
                moved_count +=1
                print(f"Moved : {filename}")

            except Exception as e:
                print(f"Error moving {filename} : {e}")

print("\nFile Moved from Source Folder to Destination Folder")
print(f"Total .jpeg/.jpg files moved : {moved_count}")
