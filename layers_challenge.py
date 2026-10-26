# Layers 1 & 2 Challenge

def check_layer_knowledge():
    print("=== Layers 1 & 2 Python Challenge ===")
    
    # Question 1: Which layer does the ARP protocol operate in?
    arp_layer = "Data Link" # <-- You can change this if needed
    
    # Question 2: What does a Switch do when it gets an unknown MAC destination?
    switch_action = "Flooding" # <-- You can change this if needed
    
    # Question 3: In which layer is data converted to bits passing through physical media?
    physical_layer_name = "Physical" # <-- You can change this if needed

    # Verification
    score = 0
    
    if "Link" in arp_layer or "2" in arp_layer:
        print("[V] Question 1: Correct! ARP is in Layer 2 (Data Link).")
        score += 1
    else:
        print("[X] Question 1: Incorrect. ARP belongs to Layer 2.")

    if "Flood" in switch_action:
        print("[V] Question 2: Correct! Unknown MAC causes a Switch Flooding.")
        score += 1
    else:
        print("[X] Question 2: Incorrect. A Switch does Flooding.")

    if "Phys" in physical_layer_name or "1" in physical_layer_name:
        print("[V] Question 3: Correct! Bits and physical media belong to Layer 1.")
        score += 1
    else:
        print("[X] Question 3: Incorrect. Physical layer is Layer 1.")

    print(f"\nYour Final Score: {score}/3")

if __name__ == "__main__":
    check_layer_knowledge()