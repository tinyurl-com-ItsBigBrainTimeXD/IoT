import os
import json
from dotenv import load_dotenv
from socket import socket, AF_INET, SOCK_STREAM


# Load the .env file into python
load_dotenv()

# Get the required variables
HOST = "192.168.43.32"
PORT = 12345

def form_packet(protocol: str, host: str, ext: str, content:dict):
    """Form the packets"""
    # Convert the data to json
    data = json.dumps(content)
    packet = f"""{protocol} {ext} HTTP/1.1\r\nHost: {host}\r\nContent-type: application/json\r\nContent-Length:{len(data)}\r\n\r\n{data}"""
    return packet

def send_data(data: str):
    """Send the data to the host and the port"""
    sock = socket(AF_INET, SOCK_STREAM)
    response = []

    try: 
        # Try to connect to the server
        sock.connect((HOST, PORT))
        
        # Post the data to the website
        sock.send(data.encode('utf-8'))

        # Get response from the server
        response.append(sock.recv(2048).decode('utf-8'))
        response.append(sock.recv(2048).decode('utf-8'))
        response.append(sock.recv(2048).decode('utf-8'))

    except Exception as e:
        print(f"Error connecting to the server: {e}")

    finally:
        sock.close()
        return response

if __name__ == "__main__":
    pkt = form_packet('GET', "localhost", '/frontend', {"type": 1})
    data = send_data(pkt)
    print("\n".join(data))
