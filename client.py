"""
Cutaneous Two-Point Discrimination (2PD) & Spatial Tactile Acuity Engine.
Provides deterministic, zero-dependency calculation of static and moving two-point discrimination thresholds,
Merkel/Meissner mechanoreceptive density, and peripheral sensory nerve regeneration.
"""

from typing import Dict, Any, List, Optional


class TwoPointDiscriminationClient:
    """
    Deterministic client for analyzing static and moving two-point discrimination (2PD) in millimeters.
    Pure Python standard library implementation based on Weber, Moberg, and Dellon hand surgery standards.
    """

    def __init__(self):
        pass

    def evaluate_static_2pd(
        self,
        smallest_discriminated_distance_mm: float,
        anatomical_site: str = "fingertip_pulp",
        correct_response_ratio: float = 0.875
    ) -> Dict[str, Any]:
        """
        Evaluates static two-point discrimination (2PD) threshold in mm.
        anatomical_site: 'fingertip_pulp', 'distal_phalanx', 'palm', or 'forearm'.
        correct_response_ratio: fraction of correct responses out of application trials (e.g. 7/8 = 0.875).
        """
        if smallest_discriminated_distance_mm <= 0:
            return {"error": "Discriminated distance must be positive"}

        dist = smallest_discriminated_distance_mm

        # Site-specific normative thresholds (Weber classification for fingertip):
        # Normal: < 6 mm (ideal 2-4 mm)
        # Fair: 6 - 10 mm
        # Poor: 11 - 15 mm
        # Protective: > 15 mm
        if anatomical_site == "fingertip_pulp":
            norm_max = 5.0
            if dist <= 4.0:
                tier = "NORMAL_EXCELLENT_SPATIAL_ACUITY"
                interpretation = f"Superior Merkel cell (SA-I) spatial innervation density ({dist} mm threshold); exceptional fine stereognosis."
                advice = "Tactile spatial resolution is optimal. Full capacity for microscopic tactile discrimination."
            elif dist <= 6.0:
                tier = "NORMAL_INTACT_SENSIBILITY"
                interpretation = f"Normal static spatial threshold ({dist} mm); intact peripheral innervation."
                advice = "Tactile spatial acuity is healthy. Maintain routine ergonomics."
            elif dist <= 10.0:
                tier = "FAIR_SENSIBILITY_ATTENUATION"
                interpretation = f"Attenuated spatial discrimination ({dist} mm); suggests subclinical compression neuropathy (e.g. median/ulnar) or digital ischemia."
                advice = "Check for repetitive keyboard strain, wrist flexion compression, or digital cold exposure."
            elif dist <= 15.0:
                tier = "POOR_TACTILE_DISCRIMINATION"
                interpretation = f"Significant mechanoreceptor loss ({dist} mm); impaired fine motor manipulation and stereognosis."
                advice = "Implement sensory re-education protocols and clinical nerve conduction review."
            else:
                tier = "ANESTHETIC_OR_PROTECTIVE_ONLY"
                interpretation = f"Severe sensory loss ({dist} mm > 15 mm); only crude protective pain/temperature perception remains."
                advice = "High injury risk due to sensory deficit. Avoid direct heat/sharp object contact."

            # Acuity score (0 - 100)
            if dist <= 4.0:
                stas = min(100.0, 90.0 + (4.0 - dist) * 5.0)
            elif dist <= 6.0:
                stas = 75.0 + ((6.0 - dist) / 2.0) * 14.0
            elif dist <= 10.0:
                stas = 45.0 + ((10.0 - dist) / 4.0) * 29.0
            else:
                stas = max(5.0, 45.0 - (dist - 10.0) * 3.5)
        else:
            # Proximal sites have larger physiological receptive fields (e.g. palm 8-12 mm, forearm 30-40 mm)
            tier = "PROXIMAL_SITE_ASSESSMENT"
            interpretation = f"Recorded 2PD of {dist} mm at {anatomical_site}."
            advice = "Compare against contralateral anatomical landmark."
            stas = 70.0

        stas_score = round(min(100.0, max(5.0, stas * min(1.0, correct_response_ratio / 0.75))), 1)

        return {
            "anatomical_site": anatomical_site,
            "discriminated_distance_mm": dist,
            "correct_response_ratio": correct_response_ratio,
            "spatial_tactile_acuity_score": stas_score,
            "classification": tier,
            "physiological_interpretation": interpretation,
            "actionable_guidance": advice
        }

    def evaluate_moving_vs_static_acuity(
        self,
        static_2pd_mm: float,
        moving_2pd_mm: float
    ) -> Dict[str, Any]:
        """
        Compares Moving 2PD (Meissner RA-I afferents) vs Static 2PD (Merkel SA-I afferents).
        In nerve regeneration or mild compression, moving 2PD recovers/preserves several weeks before static 2PD.
        """
        diff = round(static_2pd_mm - moving_2pd_mm, 2)
        moving_better = moving_2pd_mm <= static_2pd_mm

        is_normal_dynamic = moving_2pd_mm <= 3.0

        return {
            "static_2pd_mm": static_2pd_mm,
            "moving_2pd_mm": moving_2pd_mm,
            "acuity_difference_mm": diff,
            "moving_acuity_preserved": is_normal_dynamic,
            "regeneration_phase": (
                "Normal physiology: rapidly adapting Meissner units provide enhanced dynamic spatial edge resolution."
                if (is_normal_dynamic and static_2pd_mm <= 5.0) else
                "Dissociated pattern: moving sensibility preserved while static is impaired; typical of early nerve regeneration or partial entrapment."
                if (is_normal_dynamic and static_2pd_mm > 6.0) else
                "Dual mechanoreceptive impairment across both static and dynamic channels."
            )
        }
