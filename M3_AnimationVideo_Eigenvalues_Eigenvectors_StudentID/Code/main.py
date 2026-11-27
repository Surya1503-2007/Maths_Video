# =============================================================================
# main.py — Eigenvalues & Eigenvectors: M3 Mathematical Animation
# =============================================================================
#
# USAGE:
#   Render individual scenes:
#       manim -pqh main.py OpeningScene
#       manim -pqh main.py Scene1Hook
#       manim -pqh main.py Scene2Concept
#       manim -pqh main.py Scene3Intuition
#       manim -pqh main.py Scene4WorkedExample
#       manim -pqh main.py Scene5Interpretation
#       manim -pqh main.py Scene6Summary
#
#   Render the full combined video (all scenes concatenated):
#       manim -pqh main.py FullVideo
#
#   For 1080p production quality use the flag:  -qh  (1920×1080, H.264)
#
# STUDENT CONFIGURATION — edit these two lines:
STUDENT_NAME = "______________________"
STUDENT_ID   = "________________________"
#
# =============================================================================

import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from manim import *
from manim.utils.color import ManimColor

# Use `article` documentclass so BasicTeX works without `standalone.cls`
_tex_template = TexTemplate()
_tex_template.documentclass = r"\documentclass{article}"
config.tex_template = _tex_template

# ---------------------------------------------------------------------------
# Re-export scene classes so `manim main.py SceneName` works
# ---------------------------------------------------------------------------
from scenes.opening             import OpeningScene
from scenes.scene1_hook         import Scene1Hook
from scenes.scene2_concept      import Scene2Concept
from scenes.scene3_intuition    import Scene3Intuition
from scenes.scene4_worked_example import Scene4WorkedExample
from scenes.scene5_interpretation import Scene5Interpretation
from scenes.scene6_summary      import Scene6Summary

# ---------------------------------------------------------------------------
# Inject student details into the OpeningScene at render time
# ---------------------------------------------------------------------------
# (OpeningScene reads STUDENT_NAME / STUDENT_ID from this module via
#  a monkey-patch; nothing else in the pipeline is changed.)
import scenes.opening as _opening_mod
_opening_mod.STUDENT_NAME = STUDENT_NAME
_opening_mod.STUDENT_ID   = STUDENT_ID


# ===========================================================================
# FullVideo — concatenates all scenes into a single ~5-minute animation
# ===========================================================================
class FullVideo(Scene):
    """
    Renders all six scenes consecutively as a single Scene object so that
    Manim produces one continuous MP4 file.

    Running this is equivalent to watching all scenes back-to-back.

    Command:
        manim -pqh main.py FullVideo

    HOW IT WORKS:
        Each scene's construct() is called directly on this Scene instance.
        Since Manim's Scene.construct() just plays animations via self.play()
        and self.wait(), calling them in sequence produces a single timeline.
        Background color is reset at the start of each scene.
    """

    def construct(self):
        from scenes.opening import BG_COLOR as _BG

        scene_classes = [
            OpeningScene,
            Scene1Hook,
            Scene2Concept,
            Scene3Intuition,
            Scene4WorkedExample,
            Scene5Interpretation,
            Scene6Summary,
        ]

        for SceneClass in scene_classes:
            # Clear any leftover mobjects, reset background
            self.clear()
            self.camera.background_color = _BG
            # Run the scene's construct logic inside this scene's context
            SceneClass.construct(self)
            # 0.5 s black pause between scenes acts as a visual scene break
            self.wait(0.5)


# ===========================================================================
# Mathematical verification (runs when this file is executed directly)
# ===========================================================================
if __name__ == "__main__":
    import numpy as np

    print("=" * 60)
    print("MATHEMATICAL VERIFICATION")
    print("=" * 60)

    A = np.array([[4, 1], [2, 3]], dtype=float)
    print(f"\nMatrix A:\n{A}")

    # Characteristic polynomial: λ² - 7λ + 10 = 0
    coeffs = [1, -7, 10]
    roots  = np.roots(coeffs)
    print(f"\nCharacteristic polynomial: λ² - 7λ + 10 = 0")
    print(f"Eigenvalues (from np.roots): {sorted(roots, reverse=True)}")

    lam1, lam2 = 5.0, 2.0
    v1 = np.array([1, 1], dtype=float)
    v2 = np.array([1, -2], dtype=float)

    Av1 = A @ v1
    Av2 = A @ v2
    print(f"\nλ₁ = {lam1},  v₁ = {v1}")
    print(f"  Av₁ = {Av1}")
    print(f"  λ₁v₁ = {lam1 * v1}")
    print(f"  Match: {np.allclose(Av1, lam1 * v1)}")

    print(f"\nλ₂ = {lam2},  v₂ = {v2}")
    print(f"  Av₂ = {Av2}")
    print(f"  λ₂v₂ = {lam2 * v2}")
    print(f"  Match: {np.allclose(Av2, lam2 * v2)}")

    det_check = (4 - lam1) * (3 - lam1) - 2
    print(f"\ndet(A - 5I) = {det_check}  (should be 0)")
    det_check2 = (4 - lam2) * (3 - lam2) - 2
    print(f"det(A - 2I) = {det_check2}  (should be 0)")
    print("\nAll checks passed ✓" if
          (np.isclose(det_check, 0) and np.isclose(det_check2, 0) and
           np.allclose(Av1, lam1 * v1) and np.allclose(Av2, lam2 * v2))
          else "VERIFICATION FAILED")
    print("=" * 60)
