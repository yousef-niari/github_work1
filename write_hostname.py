import socket

hostname = socket.gethostname()

with open("hostname.txt","w") as file:
    file.write(f"Hostname: {hostname}\n")
    print("Hostname: {hostname}")
