#Q1. ● Read a text file line by line and display each word separated by a #
# Define a function to read a text file line by line and display each word separated by a #
def process_text_file(file_path):
    try:
        with open(file_path, 'r') as file:
            for line in file:
                # Remove leading/trailing whitespaces and split the line into words
                words = line.strip().split()
                # Join the words with '#' separator and print
                print("#".join(words))
    except FileNotFoundError:
        print("File ", file_path, "not found.")

# Call the function with the available file "sample.txt"
process_text_file("Q1.txt")
