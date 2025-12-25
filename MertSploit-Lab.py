#!/usr/bin/env python3
# Author: Mertty
# Purpose: Educational Metasploit Workflow Simulator

def banner():
    print("""
====================================
 Metasploit Workflow Simulator
 Author: Mertty
 Purpose: Cybersecurity Education
====================================
""")

def menu():
    print("""
1) Simulate payload selection
2) Simulate handler configuration
3) Exit
""")

def payload_menu():
    print("""
Select Operating System:
1) Windows
2) Linux
3) Android
""")

def simulate_payload(os_choice):
    payloads = {
        "1": "windows/meterpreter/reverse_tcp",
        "2": "linux/x64/meterpreter/reverse_tcp",
        "3": "android/meterpreter/reverse_tcp"
    }
    print("\n[SIMULATION]")
    print(f"Selected payload: {payloads.get(os_choice)}")
    print("No payload is generated. Educational purpose only.\n")

def simulate_handler():
    print("""
[SIMULATION]
use exploit/multi/handler
set PAYLOAD <selected_payload>
set LHOST <your_ip>
set LPORT <your_port>
exploit -j
""")
    print("Handler configuration simulated.\n")

def main():
    banner()
    while True:
        menu()
        choice = input("Select option: ")
        if choice == "1":
            payload_menu()
            os_choice = input("Select OS: ")
            simulate_payload(os_choice)
        elif choice == "2":
            simulate_handler()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()