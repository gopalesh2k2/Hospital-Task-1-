import hospital

def menuOptions():
    print("Menu")
    print("1. Import Patients from file.")
    print("2. Enter new patient information")
    print("3. Display next patient in line")
    print("4. Output current patient waiting list")
    print("5. Show Menu")
    print("6. Exit")


if __name__ == "__main__":
    
    entity = hospital.Hospital()
    menuOptions()
    while True:
        command = input("> ")
        if command == '1':
            # add default functonality 
            filename = input("Enter file name (default : input.txt)>") or "input.txt"
            file1 = open("HMS\\"+filename, "r")
            data = file1.read()
            # print(data)
            data = data.split()
            for i in range(0, len(data), 2):
                name = data[i]
                age = data[i+1]
                entity.registerPatient(name, age)
        elif command == '2':
            name = input("Name > ")
            age = input("Age > ")
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
            print("> Waiting List(in order of token)->")
            entity.showPatients()
        elif command == '5':
            menuOptions()
        elif command == '6':
            print("> exiting......")
            break
        else:
            print("> Enter a valid choice")



