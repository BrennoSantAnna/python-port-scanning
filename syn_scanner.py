from scapy.all import IP, TCP, sr1, send

target_ip = input("Enter Target IP: ")
target_port_str = input("Enter Target Port: ")

try:
    target_port_int = int(target_port_str)

    packet = IP(dst=target_ip) / TCP(dport=target_port_int, flags="S")
    print("[*] Sending SYN packet...")

    response = sr1(packet, timeout=2, verbose=0)

    if response is None:
        print(f"Port {target_port_int} is filtered (No response).")
    elif response.haslayer(TCP):

        if response.getlayer(TCP).flags == 0x12:
            print(f"[*] Port {target_port_int} is OPEN.")
            rst_packet = IP(dst=target_ip) / TCP(dport=target_port_int, flags="R")
            send(rst_packet, verbose=0)
        elif response.getlayer(TCP).flags == 0x14:
            print(f"[-] Port {target_port_int} is CLOSED.")

    else:
        print(f"[?] Received a non-TCP response.")

except ValueError:
    print(f"[!] Error: '{target_port_int}' is not a valid port number.")
except Exception as e:
    print(f"[!] An error occurred: {e}")