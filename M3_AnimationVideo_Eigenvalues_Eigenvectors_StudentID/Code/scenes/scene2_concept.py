# =============================================================================
# scene2_concept.py — Concept Introduction (0:50–1:40)
# =============================================================================
# NARRATION:
#   "Let's make this precise. The defining equation of an eigenvector is:
#    A times v equals lambda times v.
#    Here, A is our matrix, v is the eigenvector, and lambda is a scalar —
#    the eigenvalue. The left side transforms the vector through the matrix.
#    The right side just scales the same vector. They're equal.
#    So the transformation acts as pure scaling along that direction.
#    When lambda is 3, the vector triples in length.
#    When lambda is negative 2, the vector reverses and doubles."
#
# VISUAL INTENT:
#   Build Av = λv piece by piece with MathTex animations.
#   Show geometric demos of λ=3 (stretch) and λ=-2 (reverse+stretch).
# =============================================================================

from manim import *
from .opening import (BG_COLOR, GRID_COLOR, AXIS_COLOR, VEC_ORIG_COLOR,
                       VEC_TRANS_COLOR, EIGEN_COLOR, EIGENVAL_COLOR,
                       VEC2_COLOR, EIGENLINE_COLOR, RESULT_COLOR,
                       MATRIX_COLOR, HIGHLIGHT_COLOR)


class Scene2Concept(Scene):
    """
    Scene 2 — Concept: 0:50 – 1:40 (≈50 s)
    Introduces Av = λv with geometric and algebraic build-up.
    """

    def construct(self):
        self.camera.background_color = BG_COLOR

        # ------------------------------------------------------------------
        # 1. Build the equation step by step
        # ------------------------------------------------------------------
        # Step A: show Av
        eq_Av = MathTex(r"Av", font_size=72, color=VEC_ORIG_COLOR)
        label_Av = Text("Matrix transforms the vector",
                        font_size=24, color=GRID_COLOR)\
            .next_to(eq_Av, DOWN, buff=0.4)

        self.play(Write(eq_Av), run_time=1.0)
        self.play(FadeIn(label_Av, shift=DOWN * 0.2), run_time=0.6)
        self.wait(0.8)

        # Step B: transform to Av = λv
        eq_full = MathTex(
            r"A", r"v", r"=", r"\lambda", r"v",
            font_size=72,
        )
        eq_full[0].set_color(MATRIX_COLOR)
        eq_full[1].set_color(EIGEN_COLOR)
        eq_full[2].set_color(RESULT_COLOR)
        eq_full[3].set_color(EIGENVAL_COLOR)
        eq_full[4].set_color(EIGEN_COLOR)

        label_lv = Text("Vector scaled by λ",
                        font_size=24, color=GRID_COLOR)\
            .next_to(eq_full, DOWN, buff=0.4)

        self.play(
            TransformMatchingTex(eq_Av, eq_full),
            Transform(label_Av, label_lv),
            run_time=1.4,
        )
        self.wait(0.5)

        # Step C: Box the result
        box = SurroundingRectangle(eq_full, color=EIGENLINE_COLOR,
                                   buff=0.25, stroke_width=2)
        self.play(Create(box), run_time=0.6)

        # Component labels
        comp_A    = Text("A = square matrix",   font_size=20, color=MATRIX_COLOR)
        comp_v    = Text("v = eigenvector",      font_size=20, color=EIGEN_COLOR)
        comp_lam  = Text("λ = eigenvalue",       font_size=20, color=EIGENVAL_COLOR)
        comp_Av   = Text("Av = transformed vector", font_size=20, color=VEC_TRANS_COLOR)
        comp_lv   = Text("λv = scaled original",    font_size=20, color=EIGEN_COLOR)

        components = VGroup(comp_A, comp_v, comp_lam, comp_Av, comp_lv)\
            .arrange(DOWN, aligned_edge=LEFT, buff=0.22)\
            .to_edge(RIGHT, buff=0.5)\
            .shift(DOWN * 0.5)

        self.play(
            LaggedStart(*[FadeIn(c, shift=RIGHT * 0.2) for c in components],
                        lag_ratio=0.2),
            run_time=1.5,
        )
        self.wait(1.0)

        # Clear equation and labels
        self.play(FadeOut(VGroup(eq_full, box, label_lv, label_Av, components)),
                  run_time=0.6)

        # ------------------------------------------------------------------
        # 2. Learning Objective
        # ------------------------------------------------------------------
        objective = Text(
            "By the end of this video, you will understand what eigenvectors\n"
            "and eigenvalues represent geometrically and how to find them\n"
            "from a matrix.",
            font_size=28, color=RESULT_COLOR, line_spacing=1.3,
        ).move_to(ORIGIN + UP * 0.5)

        self.play(Write(objective), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(objective), run_time=0.5)

        # ------------------------------------------------------------------
        # 3. Geometric demos — λ = 3 (stretch) and λ = -2 (reverse)
        # Set up mini coordinate plane on the left
        # ------------------------------------------------------------------
        mini_grid = NumberPlane(
            x_range=[-4, 4, 1], y_range=[-4, 4, 1],
            x_length=6, y_length=6,
            background_line_style={"stroke_color": GRID_COLOR,
                                   "stroke_width": 0.8, "stroke_opacity": 0.3},
            axis_config={"stroke_color": AXIS_COLOR, "stroke_width": 1},
        ).shift(LEFT * 0.5)
        self.play(FadeIn(mini_grid), run_time=0.6)

        # --- Demo 1: λ = 3 ---
        # CAPTION: "Av = 3v — vector triples in length"
        demo_title1 = MathTex(r"Av = 3v", font_size=42, color=EIGENVAL_COLOR)\
            .to_corner(UR, buff=0.5)
        self.play(Write(demo_title1), run_time=0.6)

        v_orig1 = Arrow(ORIGIN, np.array([1, 0, 0]), buff=0, color=EIGEN_COLOR,
                        stroke_width=4, max_tip_length_to_length_ratio=0.2)
        v_lab1 = MathTex(r"v", color=EIGEN_COLOR, font_size=28)\
            .next_to(v_orig1.get_end(), UP, buff=0.15)
        self.play(GrowArrow(v_orig1), Write(v_lab1), run_time=0.7)

        # Animate to 3v
        v_trans1 = Arrow(ORIGIN, np.array([3, 0, 0]), buff=0,
                         color=VEC_TRANS_COLOR, stroke_width=4,
                         max_tip_length_to_length_ratio=0.2)
        v_tlab1 = MathTex(r"3v", color=EIGENVAL_COLOR, font_size=28)\
            .next_to(v_trans1.get_end(), UP, buff=0.15)

        caption1 = Text("Direction: same   |   Length: ×3",
                        font_size=24, color=GRID_COLOR).to_edge(DOWN, buff=0.6)
        self.play(Write(caption1), run_time=0.4)
        self.play(
            Transform(v_orig1, v_trans1),
            Transform(v_lab1, v_tlab1),
            run_time=1.2,
        )
        self.wait(0.8)

        # --- Demo 2: λ = -2 ---
        # CAPTION: "Av = -2v — reverses and doubles"
        self.play(FadeOut(VGroup(v_orig1, v_lab1, demo_title1, caption1)),
                  run_time=0.4)

        demo_title2 = MathTex(r"Av = -2v", font_size=42, color=EIGENVAL_COLOR)\
            .to_corner(UR, buff=0.5)
        self.play(Write(demo_title2), run_time=0.6)

        v_orig2 = Arrow(ORIGIN, np.array([1.5, 0, 0]), buff=0,
                        color=EIGEN_COLOR, stroke_width=4,
                        max_tip_length_to_length_ratio=0.2)
        v_lab2  = MathTex(r"v", color=EIGEN_COLOR, font_size=28)\
            .next_to(v_orig2.get_end(), UP, buff=0.15)
        self.play(GrowArrow(v_orig2), Write(v_lab2), run_time=0.7)

        v_trans2 = Arrow(ORIGIN, np.array([-3, 0, 0]), buff=0,
                         color=VEC_TRANS_COLOR, stroke_width=4,
                         max_tip_length_to_length_ratio=0.2)
        v_tlab2  = MathTex(r"-2v", color=EIGENVAL_COLOR, font_size=28)\
            .next_to(v_trans2.get_end(), UP, buff=0.15)

        caption2 = Text("Direction: reversed   |   Length: ×2",
                        font_size=24, color=VEC2_COLOR).to_edge(DOWN, buff=0.6)
        self.play(Write(caption2), run_time=0.4)
        self.play(
            Transform(v_orig2, v_trans2),
            Transform(v_lab2, v_tlab2),
            run_time=1.2,
        )
        self.wait(1.0)

        self.play(FadeOut(VGroup(mini_grid, v_orig2, v_lab2,
                                  demo_title2, caption2)),
                  run_time=0.8)
