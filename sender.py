import cv2
import socket
import pickle
import struct

# Sender's IP address and port
SENDER_IP = "192.168.110.118"  # Replace with the sender's IP address
PORT = 2000  # Replace with the desired port

# Create a socket connection to the receiver
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SENDER_IP, PORT))

# Initialize the webcam
cap = cv2.VideoCapture(0)

while True:
    # Capture a frame from the webcam
    ret, frame = cap.read()

    # Serialize the frame
    data = pickle.dumps(frame)
    message_size = struct.pack("L", len(data))

    # Send the message size and frame data to the receiver
    client_socket.sendall(message_size + data)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close the socket
cap.release()
client_socket.close()