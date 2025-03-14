import os

def list_contents(path):
    directories = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
        files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
            return directories, files

            path = "."  # Specify your path here
            dirs, files = list_contents(path)

            print("Directories:", dirs)
            print("Files:", files)
            print("All:", dirs + files)