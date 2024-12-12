#N0.2(i)

student_name=input("Enter student name: ")
student_number= input("Enter student number: ")
programing = int(input("Enter marks in programing: "))
data_science = int(input("Enter marks for data science: "))
computer_applications = int(input("Enter marks for computer applications: "))
#programming = 90, data_science = 87, computer_applications = 77 
sum = programing + data_science + computer_applications
average = (sum)/3
print(f" average = {average:.3f} ")
print(f"{student_name} with {student_number} and marks for exams {sum} has an average mark of {average:.3f}.")


#N0.2(ii)
def miles_per_gallons_used():
    miles_driven=int(input("Enter miles driven: "))
    gallons_used=int(input("Enter gallons  used: "))
    MPG=miles_driven / gallons_used
    print("Car's miles_per_gallons_used = " ,MPG)
miles_per_gallons_used()    


#N0.2(iii)
def odd_numbers():
    for odd_numbers in range(1,100,2):
        print(odd_numbers)
odd_numbers()    