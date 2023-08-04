import os

def is_hidden(file_path):
    return file_path.startswith('.')

def rename_files_from_text(file_list_path, folder_path):
    with open(file_list_path, 'r') as file_list:
        new_names = file_list.readlines()

    file_list.close()

    files_to_rename = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f)) and not is_hidden(f)]
    files_to_rename.sort()

    if len(files_to_rename) - 1 != len(new_names):  # Subtract 1 to exclude file_names.txt
        print("Error: The number of files and names in the text document do not match.")
        return

    file_names_txt = "file_names.txt"
    if file_names_txt in files_to_rename:
        files_to_rename.remove(file_names_txt)

    for i, file_name in enumerate(files_to_rename):
        old_path = os.path.join(folder_path, file_name)
        new_name = new_names[i].strip()  # Remove newline characters from the name
        new_path = os.path.join(folder_path, new_name)

        try:
            os.rename(old_path, new_path)
            print(f"Renamed {file_name} to {new_name}.")
        except Exception as e:
            print(f"Failed to rename {file_name}: {e}")

if __name__ == "__main__":
    folder_path = "./"  # Change this to your folder's path
    file_list_path = os.path.join(folder_path, "file_names.txt")  # Change this to your text document's name

    rename_files_from_text(file_list_path, folder_path)
