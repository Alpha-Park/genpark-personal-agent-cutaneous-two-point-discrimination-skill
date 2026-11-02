"""
MCP Server for Cutaneous Two-Point Discrimination (2PD) & Spatial Tactile Acuity.
Exposes JSON-RPC endpoints for evaluating static and moving 2PD spatial thresholds.
"""

import json
import sys
from client import TwoPointDiscriminationClient

client = TwoPointDiscriminationClient()


def handle_request(request: dict) -> dict:
    req_id = request.get("id")
    method = request.get("method")
    params = request.get("params", {})

    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "tools": [
                    {
                        "name": "evaluate_static_2pd",
                        "description": "Evaluates static two-point discrimination (2PD in mm) against Weber hand surgery standards, scoring Spatial Tactile Acuity.",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "smallest_discriminated_distance_mm": {"type": "number", "description": "Smallest distance in mm where 2 points were felt (e.g. 3.5)"},
                                "anatomical_site": {"type": "string", "default": "fingertip_pulp", "description": "Anatomical site tested"},
                                "correct_response_ratio": {"type": "number", "default": 0.875, "description": "Fraction of correct responses (e.g. 7/8 trials)"}
                            },
                            "required": ["smallest_discriminated_distance_mm"]
                        }
                    },
                    {
                        "name": "evaluate_moving_vs_static_acuity",
                        "description": "Compares Moving 2PD (Meissner units) vs Static 2PD (Merkel units) to assess differential sensory nerve recovery and compression stages.",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "static_2pd_mm": {"type": "number", "description": "Static 2PD threshold in mm (e.g. 5.0)"},
                                "moving_2pd_mm": {"type": "number", "description": "Moving 2PD threshold in mm (e.g. 2.5)"}
                            },
                            "required": ["static_2pd_mm", "moving_2pd_mm"]
                        }
                    }
                ]
            }
        }

    elif method == "tools/call":
        tool_name = params.get("name")
        args = params.get("arguments", {})

        if tool_name == "evaluate_static_2pd":
            res = client.evaluate_static_2pd(
                smallest_discriminated_distance_mm=args.get("smallest_discriminated_distance_mm", 3.5),
                anatomical_site=args.get("anatomical_site", "fingertip_pulp"),
                correct_response_ratio=args.get("correct_response_ratio", 0.875)
            )
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}
            }

        elif tool_name == "evaluate_moving_vs_static_acuity":
            res = client.evaluate_moving_vs_static_acuity(
                static_2pd_mm=args.get("static_2pd_mm", 4.5),
                moving_2pd_mm=args.get("moving_2pd_mm", 2.5)
            )
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}
            }

        else:
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "error": {"code": -32601, "message": f"Method {tool_name} not found"}
            }

    return {
        "jsonrpc": "2.0",
        "id": req_id,
        "error": {"code": -32600, "message": "Invalid Request"}
    }


def main():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
            resp = handle_request(req)
            sys.stdout.write(json.dumps(resp) + "\n")
            sys.stdout.flush()
        except Exception as e:
            err = {"jsonrpc": "2.0", "id": None, "error": {"code": -32700, "message": str(e)}}
            sys.stdout.write(json.dumps(err) + "\n")
            sys.stdout.flush()


if __name__ == "__main__":
    main()
