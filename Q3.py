#Remove all the lines that contain the character 'a' in a file and write it to another file. 

# Specify the path of the input file
input_file_path = 'Q3.txt'

# Specify the path of the output file
output_file_path = 'Q3_output.txt'

# Read the content of the input file
with open(input_file_path, 'r') as input_file:
    lines = input_file.readlines()

# Filter out lines containing the character 'a'
filtered_lines = [line for line in lines if 'a' not in line]

# Write the filtered lines to the output file
with open(output_file_path, 'w') as output_file:
    output_file.writelines(filtered_lines)

# Print a success message
print(f"Lines containing 'a' were removed from {input_file_path} and saved to {output_file_path}")
