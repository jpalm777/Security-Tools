#!/usr/bin/env python3
"""
Packet Sniffer - Cybersecurity Portfolio Project #2
Captures and analyzes network packets using scapy.
For educational use only. Requires root/sudo.
"""

from scapy.all import sniff, IP, TCP, UDP, ICMP
from datetime import datetime

def analyze_packet(packet):
    """Analyze a single packet and print relevant info."""
    timestamp = datetime.now().strftime("%H:%M:%S")
    
    # Check if packet has IP layer
    if packet.haslayer(IP):
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        protocol = packet[IP].proto
        
        # Determine protocol name
        proto_name = "OTHER"
        if packet.haslayer(TCP):
            proto_name = "TCP"
            src_port = packet[TCP].sport
            dst_port = packet[TCP].dport
            flags = packet[TCP].flags
            
            print(f"[{timestamp}] \033[93m{proto_name}\033[0m {src_ip}:{src_port} -> {dst_ip}:{dst_port} [Flags: {flags}]")
            
        elif packet.haslayer(UDP):
            proto_name = "UDP"
            src_port = packet[UDP].sport
            dst_port = packet[UDP].dport
            
            print(f"[{timestamp}] \033[94m{proto_name}\033[0m {src_ip}:{src_port} -> {dst_ip}:{dst_port}")
            
        elif packet.haslayer(ICMP):
            proto_name = "ICMP"
            icmp_type = packet[ICMP].type
            
            print(f"[{timestamp}] \033[91m{proto_name}\033[0m {src_ip} -> {dst_ip} [Type: {icmp_type}]")
            
        else:
            print(f"[{timestamp}] \033[90m{proto_name}\033[0m {src_ip} -> {dst_ip}")

def main():
    print("╔══════════════════════════════════════════════════════════════╗")
    print("║           PACKET SNIFFER - Cybersecurity Tool                ║")
    print("║           For educational use only                           ║")
    print("╚══════════════════════════════════════════════════════════════╝")
    print("")
    print("Capturing 50 packets... Press Ctrl+C to stop early.")
    print("-" * 60)
    
    try:
        # Capture 50 packets on any interface
        packets = sniff(prn=analyze_packet, count=50, store=False)
        print("-" * 60)
        print(f"Capture complete. Analyzed 50 packets.")
        
    except PermissionError:
        print("\n❌ ERROR: Permission denied.")
        print("   Run with sudo: sudo python3 packet_sniffer.py")
    except KeyboardInterrupt:
        print("\n\nCapture stopped by user.")

if __name__ == "__main__":
    main()
