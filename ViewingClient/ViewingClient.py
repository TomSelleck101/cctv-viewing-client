from connection_service import ConnectionService

import multiprocessing
import cv2
import time
import base64
import numpy as np

HOST = "127.0.0.1"
PORT = 80
VIEW_CLIENT =  f"client_type:1".encode()


def display_frame(frame_data):
    try:
        if frame_data is not None:
            # Display the resulting frame
            jpg_original = base64.b64decode(frame_data)

            jpg_as_np = np.frombuffer(jpg_original, dtype=np.uint8)
    
            image_buffer = cv2.imdecode(jpg_as_np, flags=1)

            cv2.imshow('ViewingClient', image_buffer)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                raise SystemExit("Exiting...")

    except Exception as e:
        print ("Type error displaying image...")
        print (e)
        pass

def display_frame_func(connection_service):
    while True:
        if not connection_service.is_connected():
            pass
        message = connection_service.get_message()
        display_frame(message)

def main():
    connection_service = ConnectionService(HOST, PORT, VIEW_CLIENT)
    connection_service.connect(VIEW_CLIENT)

    display_frame_thread = multiprocessing.Process(target=display_frame_func, args=(connection_service,))
    display_frame_thread.start()

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
    
