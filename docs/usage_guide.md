# HexStrike Usage Guide

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/0x4m4/hexstrike.git
   cd hexstrike
   ```

2. **Backend Setup:**
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   pip install -r requirements.txt
   python app.py
   ```

3. **Frontend Setup:**
   ```bash
   cd frontend
   npm install
   npm run dev
   ```

4. **Redis:**
   - Ensure Redis server is running locally (`redis-server`).

5. **Kali Tools:**
   - Install required Kali Linux tools (e.g., sqlmap, nmap) and ensure they are in your PATH.

## Running a Scan

1. Open the frontend in your browser (default: http://localhost:5173).
2. Enter the target URL and click "Scan".
3. Results will appear in real-time as the backend processes the request.

## Tool Definitions

- Tool definitions are YAML files in `tool_definitions/`.
- Example for SQLMap:
  ```yaml
  tool_name: sqlmap
  description: "Automatic SQL injection and database takeover tool."
  base_command: "sqlmap"
  parameters:
    - name: target_url
      type: string
      required: true
      description: "The target URL to test."
      cli_format: "{value}"
    - name: dbms
      type: string
      required: false
      description: "Specify the DBMS to use."
      cli_format: "--dbms={value}"
    - name: risk
      type: string
      required: false
      description: "Risk level (1-3)."
      cli_format: "--risk={value}"
  ```

## Extending HexStrike

- Add new tools by creating YAML files in `tool_definitions/`.
- Implement new backend modules for advanced AI or reporting features.
- Customize the frontend for enhanced user experience.

## Troubleshooting

- Ensure all dependencies are installed.
- Check backend and frontend logs for errors.
- Verify Redis and required tools are running and accessible.

## License

MIT
