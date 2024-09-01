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

# Function to extract the data from the file
def read_data_from_file(file_name: str, student_data: list):
    try:
        file = open(file_name, "r")
        student_data = json.load(file)
        for row in student_data:
            print(f"FirstName: {row['FirstName']}, LastName: {row['LastName']}, Course Name: {row['CourseName']}")
        file.close()
    except Exception as e:
        print("Error: There was a problem with reading the file.")
        print("Please check that the file exists and that it is in a json format.")
        print("-- Technical Error Message -- ")
        print(e.__doc__)
        print(e.__str__())
    finally:
        if file.closed == False:
            file.close()
    return student_data


# Function to save the data to a file
def write_data_to_file(file_name: str, student_data: list):
    try:
        file = open(file_name, "w")
        json.dump(student_data, file)
        file.close()
        print("The following data was saved to file!")
        for row in student_data:
            print(f'Student {row["FirstName"]} '
                  f'{row["LastName"]} is enrolled in {row["CourseName"]}')
    except Exception as e:
        if file.closed == False:
            file.close()
        print("Error: There was a problem with writing to the file.")
        print("Please check that the file is not open by another program.")
        print("-- Technical Error Message -- ")
        print(e.__doc__)
        print(e.__str__())


# Present and Process the data
# Function to output the menu
def output_menu(menu: str):
    print()  # Adding extra space to make it look nicer.
    print(menu)
    print()  # Adding extra space to make it look nicer.


# Function to input the menu choice
def input_menu_choice(menu: str):
    menu_choice = input("Enter your menu choice number: ")
    print()  # Adding extra space to make it look nicer.
    return menu_choice


# Function to input the student data
def input_student_data(student_data: list):
    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            course_name = input("Please enter the name of the course: ")
            student_data = {"FirstName": student_first_name,
                            "LastName": student_last_name,
                            "CourseName": course_name}
            students.append(student_data)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
            print(e)  # Prints the custom message
            print("-- Technical Error Message -- ")
            print(e.__doc__)
            print(e.__str__())
        except Exception as e:
            print("Error: There was a problem with your entered data.")
            print("-- Technical Error Message -- ")
            print(e.__doc__)
            print(e.__str__())


# Present the current data
def output_student_courses(student_data: list):
    print("-" * 50)
    for student in student_data:
        print(f'Student {student["FirstName"]} '
              f'{student["LastName"]} is enrolled in {student["CourseName"]}')
    print("-" * 50)

# Main Body of Script  ---------------------------------------------------- #
students= read_data_from_file(file_name=FILE_NAME, student_data=students)
while True:
    output_menu(MENU)
    menu_choice = input_menu_choice(MENU)
    if menu_choice == "1":
        input_student_data(student_data=students)
        continue
    elif menu_choice == "2":
        output_student_courses(student_data=students)
        continue
    elif menu_choice == "3":
        write_data_to_file(file_name=FILE_NAME,student_data=students)
        continue
    elif menu_choice == "4":
        print("Exiting program.")
        break
    else:
        print("Please only choose option 1, 2, 3, or 4")

print("Program Ended")