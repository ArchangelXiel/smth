def count_lines(filename):
        with open(filename, 'r', encoding='utf-8') as file:
                return sum(1 for _ in file):

                filename = "example.txt"  # Specify your file here⁰00000000ⁿ
                print("Number of lines:", count_lines(filename))