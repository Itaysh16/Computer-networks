# Network Layers Simulation

def network_stack_simulation():
    print("=== Network Layer Simulation ===")
    
    # Layer 5: Application Layer
    message = input("1. Enter a message to send (e.g. Hello 8200): ")
    print(f"-> [Application Layer] Message created: '{message}'\n")
    
    # Layer 4: Transport Layer (TCP/UDP)
    port = 443
    print(f"-> [Transport Layer] Added Transport Header (Port: {port})\n")
    
    # Layer 3: Network Layer (IP)
    src_ip = "192.168.1.15"
    dst_ip = "172.24.16.1"
    print(f"-> [Network Layer] Added IP Header | Source: {src_ip} | Destination: {dst_ip}\n")
    
    # Layer 2: Data Link Layer (MAC & ARP / Switch)
    src_mac = "aa:bb:cc:dd:ee:ff"
    dst_mac = input("2. Enter Destination MAC address (or press Enter if Switch does not know it): ")
    
    if not dst_mac:
        print("   [!] Switch Flooding! Unknown MAC address, broadcasting to all ports...")
        dst_mac = "ff:ff:ff:ff:ff:ff (Broadcast)"
        
    print(f"-> [Data Link Layer] Added Frame Header | Source MAC: {src_mac} | Dest MAC: {dst_mac}\n")
    
    # Layer 1: Physical Layer
    print("-> [Physical Layer] Converting data to bits (0s and 1s) and transmitting over cable/Wi-Fi!\n")
    
    print("=== Packet Sent Successfully! ===")

if __name__ == "__main__":
    network_stack_simulation()