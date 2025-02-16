import os
import shutil

def copy_files(source_folder,destination_folder):

    if not os.path.exists(source_folder):
        print(f"error: source folder {source_folder} does not exist.")
        return
    
    if not os.path.exists(destination_folder):
        os.mkdir(destination_folder)
        print("folder created...")

    files = os.listdir(source_folder)

    for file in files:
        print(f"Files found in source folder: {files}")
        source_path = os.path.join(source_folder,file)
        destination_path = os.path.join(destination_folder,file)

        if os.path.isfile(source_path):
            shutil.copy(source_path,destination_path)
            print(f"copied: {file}->{destination_path}")

    print("all files copied successfully")

copy_files(r"C:\Users\Viraj Gavas\OneDrive\Desktop\projects\python\learn_python\Learn Python Basic to advance\Practice\small_script\Transfer",r"C:\Users\Viraj Gavas\OneDrive\Desktop\projects\python\learn_python\Learn Python Basic to advance\Practice\small_script\destination")