from time import sleep
import prettytable
from datetime import datetime

database = prettytable.PrettyTable(
    ['Student #', 'First Name', 'Middle Name', 'Last Name', 'DOB', 'Gender', 'Dept', 'Email', 'Emergency contact',
     'Courses', 'Fees', 'Awards & Financial aid', 'Final grades'])
time_table = prettytable.PrettyTable(["Student #", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"])
special_characters = ['~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`',
                      '}', '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/']

student_number = 1999  # Student number starts from 2000 keeps increasing as students are added

# Lists used for adding students
list_firstName = []
list_middleName = []
list_lastName = []
list_dob = []
list_gender = []
list_department = []
list_email = []
list_emgyDetails = []
list_CoursesOpted = []
list_Fees = []
list_Awards = []
list_FinalGrade = []
studentnum = []
monday_day = " "
tuesday_day = " "
wednesday_day = " "
thursday_day = " "
friday_day = " "
monday_tup = ("")
monday_tup = str(monday_tup)
tuesday_tup = ("")
tuesday_tup = str(tuesday_tup)
wednesday_tup = ("")
wednesday_tup = str(wednesday_tup)
thursday_tup = ("")
thursday_tup = str(thursday_tup)
friday_tup = ("")
friday_tup = str(friday_tup)


def addSchedule():
    # makes a time table based on the student's Schedule
    global student_number, monday_tup, tuesday_tup, wednesday_tup, thursday_tup, friday_tup
    student_number += 1
    days = ["monday", "tuesday", "wednesday", "thursday", "friday"]
    end_time = 0
    start_time = 0

    while True:
        #program keeps looping until stoped
        print("\nEnter 'done' at any point to exit")
        time_flag = True
        sleep(0.2)
        student_class = input("Enter the course name: ")
        if student_class == "done":
            break
        else:
            while time_flag == True:
                sleep(0.2)
                start_time = input("Please enter the start time in the HH:MM format: ")
                if start_time == "done":
                    # when user types done it stops the function
                    break
                else:
                    try:
                        #gets the start time of the class from the user
                        start_time = datetime.strptime(start_time, "%H:%M")
                        start_time = start_time.strftime("%H:%M")
                    except ValueError:
                        # tells the user if the date they entered has an invalid format
                        print("Invalid time format!")
                #gets the start time of the class from the user
                sleep(0.2)
                end_time = input("Please enter the end time in the HH:MM format: ")

                if end_time == "done":
                    break
                else:
                    try:
                        end_time = datetime.strptime(end_time, "%H:%M")
                        end_time = end_time.strftime("%H:%M")
                    except ValueError:
                        print("Invalid time format!")
                if (end_time <= start_time):
                    # checks to make sure that the class dosen't end before it starts
                    print("Invalid end time! class cant end before or at the same time it starts.")
                    time_flag = True
                else:
                    time_flag = False
            if time_flag == False:
                sleep(0.2)
                day = input("What day is the class on: ")
                if day == "done":
                    break
                else:
                    day = day.lower()
                    if day not in days:
                        #sees if the day entered is a week day
                        print("Course not added")
                        print("invalid day! please choose a week day.")

                    elif day == "monday":
                        student_class = str(student_class)
                        end_time = str(end_time)
                        start_time = str(start_time)
                        monday_day =(start_time + "-" + end_time + " " + student_class)
                        monday_tup += (" | " + monday_day)

                    elif day == "tuesday":
                        student_class = str(student_class)
                        end_time = str(end_time)
                        tuesday_day =(start_time + "-" + end_time + " " + student_class)
                        tuesday_tup += (" | " + tuesday_day)


                    elif day == "wednesday":
                        student_class = str(student_class)
                        end_time = str(end_time)
                        wednesday_day =(start_time + "-" + end_time + " " + student_class)
                        wednesday_tup += (" | " + wednesday_day)


                    elif day == "thursday":
                        student_class = str(student_class)
                        end_time = str(end_time)
                        thursday_day =(start_time + "-" + end_time + " " + student_class)
                        thursday_tup += (" | " + thursday_day)


                    elif day == "friday":
                        end_time = str(end_time)
                        start_time = str(start_time)
                        friday_day =(start_time + "-" + end_time + " " + student_class)
                        friday_tup += (" | " + friday_day)


def search():
    """Function used to Search for Students"""
    global list_firstName, list_middleName, list_lastName, list_dob, list_gender, list_department, list_email, list_emgyDetails, list_CoursesOpteds, list_Fees, list_FinalGrade, studentnum
    Location_x = []
    Location_y = []
    firstname = input("\nEnter the student's First name: ").lower()
    sleep(0.2)
    lastname = input("Enter the student's Last name: ").lower()
    for x in range(len(list_firstName)):
        if firstname == list_firstName[x].lower():
            Location_x.append(x)
    for y in range(len(list_lastName)):
        if lastname == list_lastName[y].lower():
            Location_y.append(y)
    if len(Location_x) == 0 and len(Location_y) == 0:
        print("Student does not exist in Database!")
        MainMenu()
    elif len(Location_x) == 0:
        print("First name does not exist in Database!")
        MainMenu()
        return
    elif len(Location_y) == 0:
        print("Last name does not exist in Database!")
        MainMenu()
        return
    else:
        for s in (Location_x):
            for t in (Location_y):
                if t == s:
                    print(database.get_string(start=(s), end=(s + 1)))
                    print(time_table.get_string(start=(s), end=(s + 1)))
                    return
                else:
                    continue
        print("Student does not exist in database!")


def login():
    '''Function used for Login Authentication'''
    i = 4  # Counter for Username Attempts on Login
    j = 4  # Counter for Password Attempts on Login
    a = True  # Flag to determine if Username is correct
    b = True  # Flag to determine if Password is correct
    print("       " + '\033[1;4m' + "Admin Login" + '\033[0m' + "       ")
    sleep(0.2)
    while i > 0:
        i -= 1
        if i == 0:
            print("you're locked out ! please contact your administrator.")
            break
        else:
            user = input("Enter username: ")
            if any(i in special_characters for i in user):
                print("no special character allowed")
            elif user == "Admin":
                a = False
                break
            elif user != "Admin":
                print("User dose not exist !")

    if a == False:
        sleep(0.2)
        while j > 0:
            j -= 1
            if j == 0:
                print("you're locked out ! please contact your administrator.")
                break
            else:
                password = input("Enter password: ")
                if any(i in special_characters for i in password):
                    print("no special character allowed")
                elif password == "password":
                    b = False
                    break
                elif password != "password":
                    print("Incorrect password !")
    if not a and not b:
        print("Login Successful")
        MainMenu()


def MainMenu():
    '''Main Function that runs the Code'''
    global student_number
    while True:
        print("\n       " + '\033[1;4m' + "Student Ledger" + '\033[0m' + "       ")
        sleep(0.2)
        print(" [1] Add a student", '\n', "[2] Display student database", '\n', "[3] Search student details", '\n',
              "[4] Exit")
        sleep(0.2)
        choice = input("Select an option: ")

        if choice == "1":
            AddStudent()

        elif choice == "2":
            print("\n       " + '\033[1;4m' + "Student Database" + '\033[0m' + "       ")
            if student_number == 1999:  # Display's no database if there is no student available
                print("No data available. Please add a student")
                try:
                    choice = int(input("\nEnter Choice: \n[1] Main Menu\n[2] Exit\n>"))
                except ValueError:
                    print("Option entered not listed, Exiting to Main Menu")
                    MainMenu()
            elif student_number > 1999:
                print(database)
                print(time_table)
                if choice == 1:
                    continue
                elif choice == 2:
                    break
            elif student_number > 0:
                print(database)
                sleep(0.2)

        elif choice == "3":
            search()

        elif choice == "4":
            print("\nUser Signed out\n")
            return


def AddStudent():
    '''Used to add a Student to the Student Database'''
    global list_firstName, list_middleName, list_lastName, list_dob, list_gender, list_department, list_email, list_emgyDetails, list_CoursesOpteds, list_Fees, list_FinalGrade
    global student_number, monday_tup, tuesday_tup, wednesday_tup, thursday_tup, friday_tup

    while True:
        firstName = (input("\nPlease Enter First name: "))
        sleep(0.2)
        middleName = (input("Please Enter Middle name: "))
        sleep(0.2)
        lastName = (input("Please Enter Last name: "))
        sleep(0.2)
        dob = (input("Please Enter Date of Birth: "))
        sleep(0.2)
        gender = (input("Please Enter Gender: "))
        sleep(0.2)
        department = (input("Please Enter Department: "))
        sleep(0.2)
        email = (input("Please Enter Email: "))
        sleep(0.2)
        emgyDetails = (input("Please Enter emergency contact details: "))
        sleep(0.2)
        coursesOpted = (input("Please Enter Courses Opted: "))
        sleep(0.2)
        fees = (input("Please Enter Information about Fees: "))
        sleep(0.2)
        awards = (input("Please Enter Awards and Financial Aid: "))
        sleep(0.2)
        finalGrade = (input("Please Enter Final Grades: "))
        sleep(0.2)
        addSchedule()
        save = input("Save the details: Y/N: ").lower()

        if save == "y" or save == "yes":  # Saves all information about the students to the database

            studentnum.append(student_number)
            list_firstName.append(firstName)
            list_middleName.append(middleName)
            list_lastName.append(lastName)
            list_dob.append(dob)
            list_gender.append(gender)
            list_department.append(department)
            list_email.append(email)
            list_emgyDetails.append(emgyDetails)
            list_CoursesOpted.append(coursesOpted)
            list_Fees.append(fees)
            list_Awards.append(awards)
            list_FinalGrade.append(finalGrade)
            database.add_row(
                [student_number, firstName, middleName, lastName, dob, gender, department, email, emgyDetails,
                 coursesOpted, fees, awards, finalGrade])
            time_table.add_row([student_number, monday_tup, tuesday_tup, wednesday_tup, thursday_tup, friday_tup])
            print("Student", student_number, "has been successfully added to the database.")
            monday_tup = ("")
            monday_tup = str(monday_tup)
            tuesday_tup = ("")
            tuesday_tup = str(tuesday_tup)
            wednesday_tup = ("")
            wednesday_tup = str(wednesday_tup)
            thursday_tup = ("")
            thursday_tup = str(thursday_tup)
            friday_tup = ("")
            friday_tup = str(friday_tup)

        else:
            monday_tup = ("")
            monday_tup = str(monday_tup)
            tuesday_tup = ("")
            tuesday_tup = str(tuesday_tup)
            wednesday_tup = ("")
            wednesday_tup = str(wednesday_tup)
            thursday_tup = ("")
            thursday_tup = str(thursday_tup)
            friday_tup = ("")
            friday_tup = str(friday_tup)
            print("Student Data not saved")
        redo = input("Add more students Y/N: ").lower()  # repeat the function if user wants to add more students

        if redo == "y" or redo == "yes":
            continue
        elif redo == "n" or redo == "no":
            break
        else:
            print("Invalid Input! Returning to Main Menu")
            break

    return database, student_number


login()  # runs the program from login function

"""END OF PROGRAM"""
