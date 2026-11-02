"""
Example usage for Cutaneous Two-Point Discrimination (2PD) Skill.
Demonstrates analyzing fingertip static 2PD and moving vs static differential acuity.
"""

from client import TwoPointDiscriminationClient


def main():
    client = TwoPointDiscriminationClient()

    print("=== 1. Evaluating Static Two-Point Discrimination (Index Fingertip) ===")
    res_static = client.evaluate_static_2pd(
        smallest_discriminated_distance_mm=3.2,
        anatomical_site="fingertip_pulp",
        correct_response_ratio=0.875
    )

    print(f"Anatomical Site: {res_static['anatomical_site']}")
    print(f"Discriminated Distance: {res_static['discriminated_distance_mm']} mm (Normative: < 6 mm)")
    print(f"Spatial Tactile Acuity Score: {res_static['spatial_tactile_acuity_score']} / 100")
    print(f"Classification: {res_static['classification']}")
    print(f"Interpretation: {res_static['physiological_interpretation']}")
    print(f"Guidance: {res_static['actionable_guidance']}")

    print("\n=== 2. Evaluating Moving vs Static Acuity (Carpal Tunnel Screening) ===")
    res_comp = client.evaluate_moving_vs_static_acuity(
        static_2pd_mm=7.0,
        moving_2pd_mm=2.8
    )

    print(f"Static 2PD: {res_comp['static_2pd_mm']} mm | Moving 2PD: {res_comp['moving_2pd_mm']} mm")
    print(f"Acuity Difference: {res_comp['acuity_difference_mm']} mm")
    print(f"Moving Acuity Preserved: {res_comp['moving_acuity_preserved']}")
    print(f"Regeneration / Compression Phase: {res_comp['regeneration_phase']}")


if __name__ == "__main__":
    main()
