from queue import Queue

# initialize patient queue
patient_queue = Queue()

# Menu-driven program for desk manager
while True:
    print("Desk Manager - Patient Registration and Appointment System") 
    print("1. Register Patient")
    print("2. Remove Patient after Meeting Doctor")
    print("3. Display Patient Queue")
    print("4. Exit")

    choice = input("Enter your choice (just enter the option number): ")

    if choice == '1':
         # Register Patient
        patient_name = input("Enter patient name: ")
        patient_queue.put(patient_name)
        print(f"Patient (patient_name) registered.")

    elif choice == '2':
        # Remove patient after meeting doctor
        if not patient_queue.empty():
            removed_patient = patient_queue.get()
            print(f"Patient (removed_patient) removed after meeting the doctor.")
        else:
            print("No patients in the queue.")

    elif choice == '3':
        # Display Patient Queue
        if not patient_queue.empty():
            print("Current Patient Queue: ")
            for patient in list(patient_queue.queue):
                print(patient)
            print()
        else:
            print("Patient queue is empty.")
    
    elif choice == '4':
        print("Exiting program...")
        break

    else:
        print("Invaild choice! Please enter a valid option.")