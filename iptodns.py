import socket
import threading

HEADER = 64 
port = 5050
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"

SERVER = socket.gethostbyname(socket.gethostname())
print(SERVER)
ADDR = (SERVER, port)


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        conn.recv(1000).decode('utf-8') # should receive request from client. (GET ....)
        conn.send('HTTP/1.0 200 OK\n'.encode('utf-8'))
        conn.send('Content-Type: text/html\n'.encode('utf-8'))
        conn.send('\n'.encode('utf-8')) # header and body should be separated by additional newline
        conn.send("""
            <html>
            <body>
            <h1>Hello World</h1> this is my server!
            </body>
            </html>
        """.encode('utf-8')) # Use triple-quote string.
        connected = False

    conn.close()

    

def start():
    server.listen()
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn,addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount()-1}")

print("[STARTING] Server is starting")
start()