import hospital
print("************************ Hosiptal Queue Management System ******************************")
print()
print()
print()
print('''This Tool will 
1. Take the name of the patient along with his/her age and create a patient ID for the patient.
2. Insert the patient id in the priority list based on the age of the patient.
3. Display the next patient ID in line to meet the doctor
Note:the rule is that the oldest patient is seen first by the doctor''')
print()
print()
print()
print("Data is stored in Double linked list and uses max heaps as data structure!...patient information is stored in objects of class patient!")
print()
print()
print()
print()
print("Here are list of option available - please enter valid inputs!")
print()
print()


def menuOptions():
    print("*******************************************************************************************************")
    print()
    print("Menu")
    print("1. Import Patients from file.")
    print("2. Enter new patient information")
    print("3. Display next patient in line")
    print("4. Output current patient waiting list")
    print("5. Show Menu")
    print("6. Exit")
    print()
    print("*******************************************************************************************************")
    print()


if __name__ == "__main__":
    
    entity = hospital.Hospital()
    menuOptions()
    while True:
        command = input("Please provide your input> ")
        print()
        print("*******************************************************************************************************")
        print()
        if command == '1':
            # add default functonality 
            filename = input("Enter file name (default : input.txt)>") or "input.txt"
            file1 = open(filename, "r")
            data = file1.read()
            # print(data)
            data = data.split()
            for i in range(0, len(data), 2):
                name = data[i]
                age = data[i+1]
                entity.registerPatient(name, age)

        elif command == '2':
            name = input("Enter Patient Name > ")
            age = input("Enter Patient Age > ")
            while True:
                if not age.isnumeric() and age not in range(0,120):
                    age = input("Age (re-enter valid age)> ")
                else:
                    age = int(age)
                    break
            entity.registerPatient(name, age)
        elif command == '3':
            # display next patient in line
            entity.showNext()
        elif command == '4':
            print("> Waiting List->")
            entity.showPatients()
            entity.showPatientsDDL()
        elif command == '5':
            menuOptions()
        elif command == '6':
            print("> exiting......")
            break
        else:
            print("> Enter a valid choice")
        print()
        print("*******************************************************************************************************")
        print()




