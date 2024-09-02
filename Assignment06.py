# ------------------------------------------------------------------------------------------ #
# Title: Assignment06
# Desc: This assignment demonstrates using functions
# with structured error handling
# Change Log: (Who, When, What)
#   David Levinson,9/1/2024,Created Script
# ------------------------------------------------------------------------------------------ #
import json

# Define the Data Variables and constants
FILE_NAME: str = "Enrollments.json"
menu_choice: str = ""
students: list = []
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''

# Function to handle output error messages
def output_error_messages(message: str, error: Exception = None):
    """ This function displays error messages to the user
    Parameter Values:
    :param message:  message (string): Any text to be included in the error message to the user.
    :param error: The exception instance containing error details (optional).
    """
    print(message, end="\n\n")
    if error is not None:
        print("-- Technical Error Message -- ")
        print(error, error.__doc__, type(error), sep='\n')


# Function to extract the data from the file
def read_data_from_file(file_name: str):
    """
    Reads student data from a JSON file

    :param file_name: The name of the file to read
    :return: A list of student data from the file
    """
    student_data = []
    try:
        with open(file_name, "r") as file:
            student_data = json.load(file)
    except FileNotFoundError as e:
        output_error_messages("Text file must exist before running this script!", e)
    except Exception as e:
        output_error_messages("There was a non-specific error!", e)
    return student_data

# Function to save the data to a file
def write_data_to_file(file_name: str, student_data: list):
    """
        Writes student data to a JSON file.

        :param file_name: The name of the file to write
        :param student_data: The list of student data
        """
    try:
        with open(file_name, "w") as file:
            json.dump(student_data, file)
        print("The following data was saved to file!")
        for student in student_data:
            print(f'Student {student["FirstName"]} '
                  f'{student["LastName"]} is enrolled in {student["CourseName"]}')
    except TypeError as e:
        output_error_messages("There was a Type Error!", e)
    except Exception as e:
       output_error_messages("There was a non-specific error!", e)

# Function to output the menu
def output_menu(menu: str):
    """
    Outputs the menu

    :param menu: The menu string to display
    """
    print()  # Adding extra space to make it look nicer.
    print(menu)
    print()  # Adding extra space to make it look nicer.

# Function to input the menu choice
def input_menu_choice():
    """
    Prompts the user to input a menu choice

    :return: The user's menu choice
    """
    menu_choice = input("Enter your menu choice number: ")
    print()  # Adding extra space to make it look nicer.
    return menu_choice

# Function to input the student data
def input_student_data(student_data: list):
    """
    Prompts the user to input student data and appends it to the student_data list.

    :param student_data: The list of student data
    :return: The updated list of student data dictionaries
    """
    try:
        student_first_name = input("Enter the student's first name: ")
        if not student_first_name.isalpha():
            raise ValueError("The first name should not contain numbers.")
        student_last_name = input("Enter the student's last name: ")
        if not student_last_name.isalpha():
            raise ValueError("The last name should not contain numbers.")
        course_name = input("Please enter the name of the course: ")
        student_data.append({"FirstName": student_first_name,
                             "LastName": student_last_name,
                             "CourseName": course_name})
        print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
    except ValueError as e:
        output_error_messages("There was a Value error!", e)
    except Exception as e:
        output_error_messages("There was a non-specific error!", e)
    return student_data

# Function to present the current data
def output_student_courses(student_data: list):
    """
    Outputs the current student data to the user

    :param student_data: The list of student data
    """
    print("-" * 50)
    for item in student_data:
        print(f"{item['FirstName']} {item['LastName']} is enrolled in the course: {item['CourseName']}")
    print("-" * 50)

# Main Body of Script  ---------------------------------------------------- #
students = read_data_from_file(FILE_NAME)
while True:
    output_menu(MENU)
    menu_choice = input_menu_choice()
    if menu_choice == "1":
        students = input_student_data(students)
    elif menu_choice == "2":
        output_student_courses(students)
    elif menu_choice == "3":
        write_data_to_file(FILE_NAME, students)
    elif menu_choice == "4":
        print("Exiting program.")
        break
    else:
        print("Please only choose option 1, 2, 3, or 4")

print("Program Ended")