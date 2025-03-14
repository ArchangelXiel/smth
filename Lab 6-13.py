import os

def delete_file(path):
    if os.path.exists(path) and os.access(path, os.W_OK):
            os.remove(path)
                    print("File deleted successfully.")
                        else:
                                print("File does not exist or cannot be deleted.")

                                file_path = "example.txt"  # Specify your file here
                                delete_file(file_path)