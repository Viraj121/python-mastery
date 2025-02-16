import os

def delete_files_by_extension(folder_path,extension):
    if not os.path.exists(folder_path):
        print(f"Error: folder not found")
        return 
    
    files = os.listdir(folder_path)
    deleted_files = 0

    for file in files:
        file_path= os.path.join(folder_path,file)

        if os.path.isfile(file_path) and file.endswith(extension):
            os.remove(file_path)
            deleted_files+=1
            print(f"Deleted: {file_path}")

    if deleted_files == 0:
        print(f"No files with extension '{extension}' found.")
    else:
        print(f"total {deleted_files} file deleted.")

delete_files_by_extension(r"C:\Users\Viraj Gavas\OneDrive\Desktop\projects\python\learn_python\Learn Python Basic to advance\Practice\small_script\destination",".txt")