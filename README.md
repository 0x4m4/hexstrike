# HexStrike

HexStrike is an intelligent web & API penetration testing framework that leverages AI and modular command processing (MCP) tools for comprehensive, automated security assessments.

## Features

- Autonomous reconnaissance (tech stack, crawling, endpoint discovery)
- AI-driven testing and payload generation (multi-model via Copilot LM)
- Intelligent exploitation and evidence collection
- Strategic integration of Kali Linux tools (via MCP)
- Real-time web UI with live updates
- Comprehensive reporting and vulnerability database

## Architecture

- **Backend:** Python 3, Flask, Flask-SocketIO, Redis, PyYAML
- **Frontend:** React (Vite or Create React App)
- **Tool Integration:** YAML-based MCP tool definitions (Kali tools, etc.)
- **AI Integration:** Copilot LM (vscode-lm:copilot) for multi-model support

## Project Structure

```
hexstrike/
├── backend/
│   ├── app.py
│   ├── tool_executor.py
│   ├── ai_integration.py
│   ├── requirements.txt
│   └── ...
├── frontend/
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── ...
├── tool_definitions/
│   ├── sqlmap.yaml
│   ├── nmap.yaml
│   └── ...
├── docs/
│   └── usage_guide.md
└── README.md
```

## Quick Start

### Prerequisites

- Python 3.x
- Node.js & npm
- Redis server
- Kali Linux tools (optional, for full tool integration)

### Backend Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
python app.py
```

### Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

### Tool Definitions

Add YAML files for each tool in `tool_definitions/`. Example for SQLMap:

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

## Usage

1. Start backend and frontend servers.
2. Access the web UI to submit targets and view results.
3. Configure and run scans using integrated tools and AI payloads.
4. Review findings and download reports.

## Documentation

- See `docs/usage_guide.md` for detailed usage and API documentation.

## License

MIT
