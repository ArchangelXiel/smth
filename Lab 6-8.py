import os

def check_path(path):
    if os.path.exists(path):
            return os.path.dirname(path), os.path.basename(path)
                return "Path does not exist"

                path = "example.txt"  # Specify your path here
                result = check_path(path)

                if isinstance(result, tuple):
                    print("Directory:", result[0])
                        print("Filename:", result[1])
                        else:
                            print(result)