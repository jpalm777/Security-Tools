import socket
import threading
from queue import Queue

def scan_port(target_ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target_ip, port))
        sock.close()
        return result == 0
    except:
        return False

def worker(target_ip, queue, open_ports):
    while not queue.empty():
        port = queue.get()
        if scan_port(target_ip, port):
            print(f"\033[92m[OPEN]   Port {port}\033[0m")
            open_ports.append(port)
        else:
            print(f"\033[91m[CLOSED] Port {port}\033[0m")
        queue.task_done()

def main():
    target = input("Enter target IP: ")
    print(f"\nScanning ports 1-1024 on {target} with 50 threads...\n")
    
    port_queue = Queue()
    open_ports = []
    
    for port in range(1, 1025):
        port_queue.put(port)
    
    threads = []
    for _ in range(50):
        t = threading.Thread(target=worker, args=(target, port_queue, open_ports))
        t.start()
        threads.append(t)
    
    for t in threads:
        t.join()
    
    print(f"\n{'='*50}")
    print(f"SCAN COMPLETE: {len(open_ports)} ports open")
    if open_ports:
        print(f"Open ports: {sorted(open_ports)}")
    print(f"{'='*50}")

if __name__ == "__main__":
    main()
