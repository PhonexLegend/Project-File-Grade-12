#Create a binary file with name and roll number. Search for a given roll number and display the name, if not found display appropriate message. 

import struct

def create_binary_file(file_name, data):
    with open(file_name, 'wb') as file:
        for name, roll_number in data.items():
            name_length = len(name)
            file.write(struct.pack('I', name_length))
            file.write(struct.pack(f'{name_length}s', name.encode()))
            file.write(struct.pack('I', roll_number))

def search_roll_number(file_name, roll_number):
    with open(file_name, 'rb') as file:
        while True:
            name_length_data = file.read(4)
            if not name_length_data:
                break
            name_length = struct.unpack('I', name_length_data)[0]
            name = struct.unpack(f'{name_length}s', file.read(name_length))[0].decode()
            current_roll_number = struct.unpack('I', file.read(4))[0]
            if current_roll_number == roll_number:
                return name
    return None

# Data to be written to the binary file
data = {
    "Ram": 101,
    "Sham": 102,
    "Ghanshyam": 103,
    "Atmaram": 104,
    "Ramalaingum": 105
}

# Create the binary file
create_binary_file("Q4.bin", data)

# Search for a roll number
roll_number_to_search = 103
found_name = search_roll_number("Q4.bin", roll_number_to_search)
if found_name:
    print(f"Name associated with roll number {roll_number_to_search}: {found_name}")
else:
    print(f"No record found for roll number {roll_number_to_search}")
