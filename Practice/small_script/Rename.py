import os
import shutil

def sort_files_by_extension(folder_path):
    files = os.listdir(folder_path)  # Get all items (files & folders) in the directory

    for file in files:  # Loop through each item in the folder
        file_path = os.path.join(folder_path, file)  

        if os.path.isfile(file_path):  # Ignore folders, process only files
            ext = file.split('.')[-1]  # Extract the file extension
            ext_folder = os.path.join(folder_path, ext.upper())  # Convert to uppercase for uniformity

            if not os.path.exists(ext_folder):  # If folder doesn't exist, create it
                os.mkdir(ext_folder)

            shutil.move(file_path, os.path.join(ext_folder, file))  # Move file to its extension folder
            print(f"Moved: {file} ➝ {ext_folder}")

# Example usage
sort_files_by_extension("C:/Users/User/Desktop/TestFolder")
