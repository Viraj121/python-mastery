import os

def rename_files(folder_path, prefix):
    print(f"📂 Checking folder: {folder_path}")  # Print folder being processed
    
    if not os.path.exists(folder_path):
        print("❌ Error: The folder does not exist!")
        return
    
    files = os.listdir(folder_path)  # Get all files in the folder
    print(f"📄 Found {len(files)} files: {files}")  # Print number of files

    for index, filename in enumerate(files):
        old_path = os.path.join(folder_path, filename)
        file_extension = os.path.splitext(filename)[1]  # Extract file extension
        new_filename = f"{prefix}_{index}{file_extension}"
        new_path = os.path.join(folder_path, new_filename)

        print(f"🔄 Processing File {index + 1}:")
        print(f"   - Old Name: {filename}")
        print(f"   - New Name: {new_filename}")
        print(f"   - Old Path: {old_path}")
        print(f"   - New Path: {new_path}")

        try:
            os.rename(old_path, new_path)
            print(f"✅ Renamed Successfully: {filename} ➝ {new_filename}\n")
        except Exception as e:
            print(f"❌ Error renaming {filename}: {e}\n")

# Run the function with correct path
rename_files("C:\\Users\\Viraj\\Desktop\\saas_le\\PHASE2", "NewFile")
