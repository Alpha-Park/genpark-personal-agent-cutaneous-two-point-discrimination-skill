---
name: genpark-personal-agent-cutaneous-two-point-discrimination-skill
description: Deterministic evaluation of static and moving cutaneous two-point discrimination (2PD in mm), Merkel/Meissner spatial innervation density, and tactile acuity.
version: 1.0.0
author: GenPark Autonomous Agents Ecosystem
license: MIT
tags:
  - personal-agent
  - ai-agent
  - openclaw
  - genpark
  - mcp
  - mcp-server
  - model-context-protocol
  - python
  - zero-dependency
  - wellness
  - productivity
  - production-ready
---

# Cutaneous Two-Point Discrimination (2PD) Skill

## Overview
The `genpark-personal-agent-cutaneous-two-point-discrimination-skill` delivers clinical hand sensory analytics to sovereign personal agents. Two-point discrimination (2PD) tests the spatial innervation density and cortical receptive field mapping of slowly adapting (SA-I, Merkel cell) and rapidly adapting (RA-I, Meissner corpuscle) mechanoreceptive afferents. Based on Weber hand surgery criteria and Dellon moving 2PD paradigms, this skill detects subclinical median/ulnar entrapment, evaluates sensory nerve recovery, and monitors manual dexterity.

## Physiological Model & Mathematics
1. **Weber Static 2PD Classification (Fingertip Pulp)**:
   - **Normal Sensibility**: $\le 5.0\text{ mm}$ (ideal $2.0 - 4.0\text{ mm}$).
   - **Fair Sensibility**: $6.0 - 10.0\text{ mm}$.
   - **Poor Sensibility**: $11.0 - 15.0\text{ mm}$.
   - **Protective Only**: $> 15.0\text{ mm}$.
2. **Moving vs Static 2PD Dissociation**:
   Because rapidly adapting Meissner units regenerate earlier and have dynamic lateral inhibition, moving 2PD ($2.0 - 3.0\text{ mm}$) preserves earlier than static 2PD during compressive recovery.
3. **Spatial Tactile Acuity Score ($STAS$)**:
   Maps threshold distance and trial reliability ratios into a standardized 0 to 100 tactile competence metric.

## Tools & Endpoints
- `evaluate_static_2pd`: Computes Weber threshold category and Spatial Tactile Acuity Score.
- `evaluate_moving_vs_static_acuity`: Compares dynamic RA-I vs static SA-I channel preservation.
