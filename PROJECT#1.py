# PROJECT 1: Basic School Administration tool

# TO import csv file
import  csv

# Function to write in csv file
def write_into_csv(info_list):
    with open('student_info.csv', 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        
        #To print headings one time
        if csv_file.tell() == 0:
            writer.writerow(["Name", "Age", "Contact_Number", "E-mail"])
        
        writer.writerow(info_list)
# To get the input from the user in a format 
if __name__ == '__main__': 
    condition = True
    student_num = 1 
    
    while(condition):
        student_info = input("Enter student Details for student #{} in the following format(Name Age Contact_Number Email):".format(student_num))
       
        # using split
        student_info_list = student_info.split(' ')
        
        print("\nThe entered details is -\nName: {}\nAge: {}\nContact_Number: {}\nE-mail: {}".format(student_info_list[0], student_info_list[1], student_info_list[2], student_info_list[3]))
        
        # For the user to use if there is any correction in values
        choice_check = input("Is the entered details correct? (yes/no): ")
        
        if choice_check == "yes":
           # Calling the function
           write_into_csv(student_info_list)
          
            # Using condition check to add more details
           condition_check = input("Do you want to add more details?(yes/no)")
        
           if condition_check == "yes":
                condition = True
                student_num = student_num + 1
           elif condition_check == "no":
                condition = False
        
        elif choice_check == "no":
            print("Please Re-enter the Valus!") 
