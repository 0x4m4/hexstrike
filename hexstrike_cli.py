#!/usr/bin/env python3

import socket

SERVER_HOST = input("Enter HexStrike server IP (Kali/WSL): ").strip()
SERVER_PORT = 50505

def main():
    print("HexStrike CLI - Automated Pentesting Platform")
    print("Type 'exit' to quit.")
    while True:
        try:
            command = input("hexstrike> ").strip()
            if not command:
                continue
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((SERVER_HOST, SERVER_PORT))
                s.recv(4096)  # Welcome message
                s.sendall(command.encode())
                result = s.recv(65536).decode(errors='replace')
                print(result.strip())
            if command.lower() == 'exit':
                break
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
