

import csv


def write_into_csv(info_list):
    with open('student_info.csv', 'a', newline='')as csv.file:
        writer = csv.writer(csv.file)

        if csv.file.tell() == 0:
           writer.writerow(["Name", "Age", "Contact Number", "Email ID"])
        writer.writerow(info_list)

if __name__ == '__main__':

   condition = True
   student_num =1

   while (condition):
      student_info = input("Enter some information for student #{} in the following format (Name Age Contact_Number E-mail_Id) : "
                           .format(student_num))
      print('Enter Information:', student_info)
      student_info_list = student_info.split(' ')
      print("Enter split up information list is :", student_info_list)


      print("\nThe entered information is - \nName: {}\n Age: {}\nContact_number: {}\nE-Mail ID: {}"
            .format(student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3]))


      choise_check =input("Is the enterd information correct? yes?no : ")
      if choise_check == "yes":
           write_into_csv(student_info_list)

           condition_check = input("If you want to enter some another student information (Yes/No): ")
           if condition_check == "yes":
               condition = True
               student_num =student_num+1
           elif condition_check == "no":
               condition = False

      elif choise_check == "no":
         print("\n Please re-enter the values")

          
          
          
