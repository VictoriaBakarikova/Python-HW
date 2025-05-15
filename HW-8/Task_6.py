TREE = {
    "folder-1": ["file1.txt", "file2.py"],
    "folder-2": {"subfolder": ["notes.txt", "readme.md"]},
}


def extension_finder(tree, extension, path=""):
    found_files = []

    for key, value in tree.items:
        current_path = f"{path}{key}" if path else key
        if isinstance(value, dict):
            found_files.extend(extension_finder(value, extension, current_path))
        else:
            found_files.extend(
                f"{current_path}/{file}"
                for file in value
                if file.endswith(f".{extension}")
            )
        return found_files
