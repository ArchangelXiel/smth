def write_list_to_file(filename, data):
    with open(filename, 'w', encoding='utf-8') as file:
            for item in data:
                        file.write(f"{item}\n")

                        data = ["Apple", "Banana", "Cherry"]
                        filename = "output.txt"
                        write_list_to_file(filename, data)