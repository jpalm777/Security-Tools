import socket

def scan_ports(target_ip):
    print(f"\nScanning ports 1-1024 on {target_ip}...\n")
    
    for port in range(1, 1025):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target_ip, port))

        if result == 0:
            print(f"\033[92m[OPEN]   Port {port}\033[0m")
        else:
            print(f"\033[91m[CLOSED] Port {port}\033[0m")

        sock.close()

if __name__ == "__main__":
    target = input("Enter target IP: ")
    scan_ports(target)
