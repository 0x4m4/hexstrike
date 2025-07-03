import os
import yaml
import subprocess

TOOL_DEFINITIONS_DIR = os.path.join(os.path.dirname(__file__), '..', 'tool_definitions')

def load_tool_definition(tool_name):
    path = os.path.join(TOOL_DEFINITIONS_DIR, f"{tool_name}.yaml")
    if not os.path.exists(path):
        raise FileNotFoundError(f"Tool definition not found: {tool_name}")
    with open(path, 'r') as f:
        return yaml.safe_load(f)

def build_command(tool_def, params):
    cmd = [tool_def['base_command']]
    for param in tool_def.get('parameters', []):
        name = param['name']
        value = params.get(name)
        if value is not None:
            fmt = param['cli_format']
            cmd.append(fmt.replace("{value}", str(value)))
    return cmd

def execute_tool(tool_name, params):
    tool_def = load_tool_definition(tool_name)
    cmd = build_command(tool_def, params)
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
        return {
            "command": " ".join(cmd),
            "stdout": result.stdout,
            "stderr": result.stderr,
            "returncode": result.returncode
        }
    except Exception as e:
        return {"error": str(e)}
