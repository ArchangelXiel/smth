def copy_file(source, destination):
    with open(source, 'r', encoding='utf-8') as src, open(destination, 'w', encoding='utf-8') as dest:
            dest.write(src.read())

            source_file = "source.txt"
            destination_file = "destination.txt"
            copy_file(source_file, destination_file)