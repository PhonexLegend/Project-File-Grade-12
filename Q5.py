#  Create a binary file with roll number, name and marks. Input a roll number andupdate the marks.      
import pickle

def write_student_details():
    """
    Writes student details (roll number, name, and marks) to a binary file using pickle.
    """
    try:
        with open(".dat", 'wb') as f:
            while True:
                roll_no = int(input("Enter Roll no: "))
                name = input("Enter Name: ")
                marks = int(input("Enter Marks: "))
                record = [roll_no, name, marks]
                pickle.dump(record, f)
                choice = input("Do you want to enter more? (Y/N): ")
                if choice.lower() != 'y':
                    break
    except Exception as e:
        print(f"Error occurred: {e}")

def read_student_details():
    """
    Reads student details from the binary file and prints them.
    """
    try:
        with open(".dat", 'rb') as f:
            while True:
                try:
                    record = pickle.load(f)
                    print(record)
                except EOFError:
                    break
    except Exception as e:
        print(f"Error occurred: {e}")

def update_student_marks():
    """
    Updates the marks of a student based on roll number.
    """
    try:
        roll_no = int(input("Enter roll no whose marks you want to update: "))
        with open("Q5.dat", 'rb+') as f:
            while True:
                try:
                    pos = f.tell()
                    record = pickle.load(f)
                    if record[0] == roll_no:
                        updated_marks = int(input("Enter updated marks: "))
                        record[2] = updated_marks
                        f.seek(pos)
                        pickle.dump(record, f)
                        break
                except EOFError:
                    break
    except Exception as e:
        print(f"Error occurred: {e}")

# Write student details to the file
write_student_details()

# Read and print student details from the file
read_student_details()

# Update student marks
update_student_marks()

# Read and print updated student details
read_student_details()
