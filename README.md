# HexStrike

HexStrike is an automated penetration testing platform that leverages AI and MCP (Model Context Protocol) to orchestrate security tools on Kali Linux from a CLI client running on Windows. HexStrike enables efficient, automated pentesting by letting AI select and execute the right tools for each task.

## Features

- **Automated Pentesting:** AI-driven selection and execution of Kali Linux tools.
- **Cross-Platform:** CLI client for Windows, server component for Kali Linux.
- **MCP Integration:** Uses MCP to securely communicate and control pentesting tools.
- **Modular Design:** Easily extendable to support more tools and workflows.
- **Secure Communication:** Ensures safe data transfer between client and server.

## Architecture

```
+-------------------+         Secure MCP         +-------------------+
|  Windows Machine  |  <--------------------->  |   Kali Linux VM   |
|   HexStrike CLI   |                           |  HexStrike Server |
+-------------------+                           +-------------------+
        |                                               |
        |             [AI decides tools]                |
        |---------------------------------------------->|
        |                                               |
        |        [Results returned to CLI]              |
        |<----------------------------------------------|
```

- **Client:** CLI app for Windows. Sends pentest requests, receives results.
- **Server:** Runs on Kali Linux. Executes tools (e.g., nmap, nikto, hydra) as instructed by AI.

## Installation

### Server (Kali Linux)

1. Clone the repository and navigate to the server directory.
2. Install required dependencies (Python 3.x, MCP server, pentesting tools).
3. Run the server script:
   ```bash
   python3 hexstrike_server.py
   ```

### Client (Windows)

1. Clone the repository and navigate to the client directory.
2. Install required dependencies (Python 3.x, MCP client).
3. Run the CLI:
   ```bash
   python hexstrike_cli.py
   ```

## Usage

1. Start the server on Kali Linux.
2. Run the CLI on Windows.
3. Use CLI commands to initiate pentests:
   ```
   hexstrike scan --target 192.168.1.10
   hexstrike brute --service ssh --target 192.168.1.10
   ```

## Supported Tools

- nmap
- nikto
- hydra
- gobuster
- sqlmap
- (and more, extensible via MCP)

## Security

- Ensure network communication is secured (VPN, SSH tunnel, or TLS).
- Run only in controlled, authorized environments.

## Contributing

Contributions are welcome! Please open issues or submit pull requests for new features, bug fixes, or documentation improvements.

## License

MIT License. See [LICENSE](LICENSE) for details.
