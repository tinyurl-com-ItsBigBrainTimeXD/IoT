import json
from socket import socket, AF_INET, SOCK_STREAM

# Get the required variables
HOST = "192.168.43.32"
PORT = 12345

def form_packet(host):
    """Form the packets"""
    # Convert the data to json
    packet = f"""GET /device HTTP/1.1
Host: {host}
Connection: close

"""
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
        for _ in range(3):
            response.append(sock.recv(2048).decode('utf-8'))

    except Exception as e:
        print(f"Error connecting to the server: {e}")

    finally:
        sock.close()
        return response

if __name__ == "__main__":
    pkt = form_packet("192.168.43.32:12345")
    _,_,content = send_data(pkt)
    print(content, type(content))
