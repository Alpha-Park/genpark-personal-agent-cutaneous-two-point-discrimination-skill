# Cutaneous Two-Point Discrimination (2PD) Skill

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Zero Dependencies](https://img.shields.io/badge/dependencies-0-brightgreen.svg)](https://github.com/alphaparkinc/genpark-personal-agent-cutaneous-two-point-discrimination-skill)
[![OpenClaw Ready](https://img.shields.io/badge/OpenClaw-Compatible-purple.svg)](https://github.com/alphaparkinc/genpark-personal-agent-cutaneous-two-point-discrimination-skill)
[![MCP Protocol](https://img.shields.io/badge/MCP-Standard-orange.svg)](https://modelcontextprotocol.io/)

A sovereign personal agent capability for computational tactile psychophysics, evaluating static and moving cutaneous two-point discrimination (2PD in mm), Merkel/Meissner spatial receptive density, and peripheral nerve health.

## Architecture

```mermaid
flowchart TD
    TouchData["Tactile Discrimination Trials: Discriminated Distance (mm) & Success Ratio"] --> WeberEngine["Weber Static 2PD Classification Engine (Normal <= 5mm, Fair 6-10mm, Poor 11-15mm)"]
    TouchData --> MovingEngine["Dellon Dynamic Moving 2PD vs Static Dissociation Engine"]
    WeberEngine & MovingEngine --> STAS["Spatial Tactile Acuity Score (STAS: 0 - 100)"]
    STAS --> ErgonomicPrescription["OpenClaw / Hermes Carpal Tunnel Ergonomics & Sensory Training"]
```

## Quickstart

```python
from client import TwoPointDiscriminationClient

client = TwoPointDiscriminationClient()

# Assess static 2PD threshold at fingertip
res = client.evaluate_static_2pd(
    smallest_discriminated_distance_mm=3.2,
    anatomical_site="fingertip_pulp",
    correct_response_ratio=0.875
)

print("Discriminated Distance:", res["discriminated_distance_mm"], "mm")
print("Acuity Score:", res["spatial_tactile_acuity_score"], "/ 100")
print("Classification:", res["classification"])
print("Guidance:", res["actionable_guidance"])
```

## MCP Server Integration

Add to your `claude_desktop_config.json` or OpenClaw tool registry:

```json
{
  "mcpServers": {
    "two-point-discrimination": {
      "command": "python",
      "args": ["/path/to/genpark-personal-agent-cutaneous-two-point-discrimination-skill/mcp_server.py"]
    }
  }
}
```

## License
MIT License.
