import socket

PORT = 9999  # Port to listen on (as required by assignment 9999)
HOST = "127.0.0.1"  # Standard loopback interface address (localhost)

with socket.socket() as s:
    s.connect((HOST, PORT))
    message = input("\n Choose an option: \n \
                    1. Find customer \n \
                    2. Add customer \n \
                    3. Delete customer \n \
                    4. Update customer age \n \
                    5. Update customer address \n \
                    6. Update customer phone \n \
                    7. Print report \n \
                    8. Exit \n \
                    Select: ")

    # Establish connection with server
    while message != "8":  # A loop until 8 is entered

        if message == "1":  # Input customer's name and receive their information
            s.send(message.encode())
            name = input("Customer Name:")
            s.send(name.encode())
            data = s.recv(9999).decode()
            print("Received from server: " + data)
            message = input("\n Choose an option: \n \
                            1. Find customer \n \
                            2. Add customer \n \
                            3. Delete customer \n \
                            4. Update customer age \n \
                            5. Update customer address \n \
                            6. Update customer phone \n \
                            7. Print report \n \
                            8. Exit \n \
                            Select: ")

        elif message == "2":  # Input customers information to update the database and receive confirmation
            s.send(message.encode())
            name = input("Customer Name:")
            s.send(name.encode())
            age = input("Customer Age:")
            s.send(age.encode())
            street = input("Customer Street Name:")
            s.send(street.encode())
            tel = input("Customer Phone Number:")
            s.send(tel.encode())
            data = s.recv(9999).decode()
            print("Received from server: " + data)
            message = input("\n Choose an option: \n \
                            1. Find customer \n \
                            2. Add customer \n \
                            3. Delete customer \n \
                            4. Update customer age \n \
                            5. Update customer address \n \
                            6. Update customer phone \n \
                            7. Print report \n \
                            8. Exit \n \
                            Select: ")

        elif message == "3":  # Input customers name to be deleted and receive confirmation
            s.send(message.encode())
            name = input("Customer Name:")
            s.send(name.encode())
            data = s.recv(9999).decode()
            print("Received from server: " + data)
            message = input("\n Choose an option: \n \
                            1. Find customer \n \
                            2. Add customer \n \
                            3. Delete customer \n \
                            4. Update customer age \n \
                            5. Update customer address \n \
                            6. Update customer phone \n \
                            7. Print report \n \
                            8. Exit \n \
                            Select: ")

        elif message == "4":  # Input customers name and new age to be updated and receive confirmation
            s.send(message.encode())
            name = input("Customer Name:")
            s.send(name.encode())
            new_age = input("Customer New Age:")
            s.send(new_age.encode())
            data = s.recv(9999).decode()
            print("Received from server: " + data)
            message = input("\n Choose an option: \n \
                            1. Find customer \n \
                            2. Add customer \n \
                            3. Delete customer \n \
                            4. Update customer age \n \
                            5. Update customer address \n \
                            6. Update customer phone \n \
                            7. Print report \n \
                            8. Exit \n \
                            Select: ")

        elif message == "5":  # Input customers name and new address to be updated and receive confirmation
            s.send(message.encode())
            name = input("Customer Name:")
            s.send(name.encode())
            new_address = input("Customer New Address:")
            s.send(new_address.encode())
            data = s.recv(9999).decode()
            print("Received from server: " + data)
            message = input("\n Choose an option: \n \
                            1. Find customer \n \
                            2. Add customer \n \
                            3. Delete customer \n \
                            4. Update customer age \n \
                            5. Update customer address \n \
                            6. Update customer phone \n \
                            7. Print report \n \
                            8. Exit \n \
                            Select: ")

        elif message == "6":  # Input customers name and new phone number to be updated and receive confirmation
            s.send(message.encode())
            name = input("Customer Name:")
            s.send(name.encode())
            new_number = input("Customer New Phone Number:")
            s.send(new_number.encode())
            data = s.recv(9999).decode()
            print("Received from server: " + data)
            message = input("\n Choose an option: \n \
                            1. Find customer \n \
                            2. Add customer \n \
                            3. Delete customer \n \
                            4. Update customer age \n \
                            5. Update customer address \n \
                            6. Update customer phone \n \
                            7. Print report \n \
                            8. Exit \n \
                            Select: ")

        elif message == "7":  # Receive and print the report of the database
            s.send(message.encode())
            data = s.recv(9999).decode()
            print("Received from server: " + data)
            message = input("\n Choose an option: \n \
                            1. Find customer \n \
                            2. Add customer \n \
                            3. Delete customer \n \
                            4. Update customer age \n \
                            5. Update customer address \n \
                            6. Update customer phone \n \
                            7. Print report \n \
                            8. Exit \n \
                            Select: ")

    print("Goodbye!")
    s.close()
