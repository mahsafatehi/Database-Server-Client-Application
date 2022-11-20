import socket

PORT = 9999  # Port to listen on (as required by assignment 9999)
HOST = "127.0.0.1"  # Standard loopback interface address (localhost)

with socket.socket() as s:

    # Now bind to the port
    s.bind((HOST, PORT))
    print(f"Socket is bound to {PORT}")

    # Put the socket into listening mode
    s.listen()
    print("Socket is listening")

    c, addr = s.accept()
    print(f"Connection from {addr}")

    # Establish connection with client
    while True:  # A loop until we interrupt or there is an error
        data = c.recv(9999).decode()
        print("from connected user: " + str(data))
        db = open("data.txt", "r+")
        data_base = db.readlines()

        if not data:
            break

        if data == "1":  # Receive customer's name and send their information
            counter = 0
            name = c.recv(9999).decode()
            print("from connected user: " + str(name))
            for line in data_base:
                values = line.split("|")
                if name == values[0].strip():
                    counter = 1
                    data = line
            if counter == 1:
                c.send(data.encode())
            else:
                data = f"{name} not found in database."
                c.send(data.encode())

        elif data == "2":  # Receive customers information and update the database and send confirmation
            counter = 0
            name = c.recv(9999).decode()
            print("from connected user: " + str(name))
            for line in data_base:
                values = line.split("|")
                if name == values[0].strip():
                    counter = 1
                    break
            if counter == 0:
                age = c.recv(9999).decode()
                street = c.recv(9999).decode()
                tel = c.recv(9999).decode()
                db = db.write(f"\n{name}|{age}|{street}|{tel}")
                data = "Customer has been added."
                c.send(data.encode())
            else:
                data = "Customer already exists."
                c.send(data.encode())

        elif data == "3":  # Receive customers and delete it from database and send confirmation
            counter = 0
            name = c.recv(9999).decode()
            print("from connected user: " + str(name))
            with open("data.txt", "w") as db_write:
                for line in data_base:
                    values = line.split("|")
                    if name != values[0].strip():
                        db_write.write(line)
                    else:
                        counter = 1
            if counter == 1:
                data = "Customer has been deleted."
                c.send(data.encode())
            else:
                data = "Customer does not exist."
                c.send(data.encode())

        elif data == "4":  # Receive customers name and new age and update database and send confirmation
            counter = 0
            name = c.recv(9999).decode()
            print("from connected user: " + str(name))
            with open("data.txt", "w") as db_write:
                for line in data_base:
                    values = line.split("|")
                    if name == values[0].strip():
                        new_number = c.recv(9999).decode()
                        db_write.write(line.replace(values[1], new_number))
                        counter = 1
                    else:
                        db_write.write(line)
                if counter == 1:
                    data = f"Age for {name} has been updated."
                    c.send(data.encode())
                else:
                    data = "Customer not found."
                    c.send(data.encode())

        elif data == "5":  # Receive customers name and new address and update database and send confirmation
            counter = 0
            name = c.recv(9999).decode()
            print("from connected user: " + str(name))
            with open("data.txt", "w") as db_write:
                for line in data_base:
                    values = line.split("|")
                    if name == values[0].strip():
                        new_address = c.recv(9999).decode()
                        db_write.write(line.replace(values[2], new_address))
                        counter = 1
                    else:
                        db_write.write(line)
                if counter == 1:
                    data = f"Address for {name} has been updated."
                    c.send(data.encode())
                else:
                    data = "Customer not found."
                    c.send(data.encode())

        elif data == "6":  # Receive customers name and new phone number and update database and send confirmation
            counter = 0
            name = c.recv(9999).decode()
            print("from connected user: " + str(name))
            with open("data.txt", "w") as db_write:
                for line in data_base:
                    values = line.split("|")
                    if name == values[0].strip():
                        new_number = c.recv(9999).decode()
                        db_write.write(line.replace(values[3], new_number))
                        counter = 1
                    else:
                        db_write.write(line)
                if counter == 1:
                    data = f"Phone number for {name} has been updated"
                    c.send(data.encode())
                else:
                    data = "Customer not found"
                    c.send(data.encode())

        elif data == "7":  # Send the report of the database to client
            data = "\n** Python DB contents **\n"
            for line in data_base:
                data = data + f"\n{line}"
            c.send(data.encode())

    c.close()
