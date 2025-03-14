import string

def generate_files():
    for letter in string.ascii_uppercase:
            with open(f"{letter}.txt", "w", encoding="utf-8") as file:
                        file.write(f"File {letter}.txt")

                        generate_files()