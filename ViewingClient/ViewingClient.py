from connection_service import ConnectionService

HOST = "127.0.0.1"
PORT = 80
VIEW_CLIENT =  f"client_type:1".encode()



def main():
    connection_service = ConnectionService(HOST, PORT, VIEW_CLIENT)
    connection_service.connect(VIEW_CLIENT)

                                            # Get available hubs / cameras
    # Request footage from hub + camera                                         # Set motion detect on hub + camera
    # Receive stream and display                                                # Receive push notification on detection
    while True:
        user_input = input("Enter something:")

        if user_input == "s":
            if (connection_service.is_connected()):
                connection_service.send_message("send:test_hub:1".encode())
            else:
                print ("Not connected..")

        if user_input == "x":
            if (connection_service.is_connected()):
                connection_service.send_message("stop:test_hub:1".encode())
            else:
                print ("Not connected..")

        if user_input == "c":
            connection_service.connect(VIEW_CLIENT)

        if user_input == "quit":
            break

if __name__ == '__main__':
    main()
    
