# =============================================================================
# scene1_hook.py — Hook / Context (0:10–0:50)
# =============================================================================
# NARRATION:
#   "Here's something strange. I'm going to apply a matrix transformation
#    to several vectors. Watch carefully what happens to their directions.
#    Most of them spin around — their direction completely changes.
#    But look at this one. It stays on the same line.
#    What is so special about it? That question is what this video answers."
#
# VISUAL INTENT:
#   Show four vectors. Apply a transformation. Three change direction, one
#   clearly keeps its line. Label the special one "eigenvector".
# =============================================================================

from manim import *
from .opening import (BG_COLOR, GRID_COLOR, AXIS_COLOR, VEC_ORIG_COLOR,
                       VEC_TRANS_COLOR, EIGEN_COLOR, EIGENVAL_COLOR,
                       VEC2_COLOR, EIGENLINE_COLOR, RESULT_COLOR,
                       MATRIX_COLOR, HIGHLIGHT_COLOR)


class Scene1Hook(Scene):
    """
    Scene 1 — Hook: 0:10 – 0:50 (≈40 s)
    Visual question: 'What if a matrix transforms a vector without changing direction?'
    """

    def construct(self):
        self.camera.background_color = BG_COLOR

        # ------------------------------------------------------------------
        # 1. Fresh coordinate grid
        # ------------------------------------------------------------------
        grid = NumberPlane(
            x_range=[-6, 6, 1], y_range=[-4, 4, 1],
            background_line_style={"stroke_color": GRID_COLOR,
                                   "stroke_width": 1, "stroke_opacity": 0.35},
            axis_config={"stroke_color": AXIS_COLOR, "stroke_width": 1.5},
        )
        self.play(FadeIn(grid), run_time=0.8)

        # ------------------------------------------------------------------
        # 2. Place four generic vectors (non-eigenvectors) + one eigenvector
        # Using matrix A = [[3, 1],[0, 2]]:
        #   Eigenvector for λ=3: [1, 0]; for λ=2: [1, 1]  (approx choices)
        # For the hook we use A = [[2,1],[0,2]] — shear — simpler visuals.
        # Actually, let's keep A = [[2,0],[0,3]] (diagonal), very clear:
        #   Eigenvectors: e1=[1,0] λ=2, e2=[0,1] λ=3
        # ------------------------------------------------------------------
        # We'll show 3 non-eigenvectors and 1 eigenvector
        A = np.array([[2.0, 0.0], [0.0, 3.0]])

        def make_arrow(tip, color, width=4):
            return Arrow(ORIGIN, np.array([tip[0], tip[1], 0]), buff=0,
                         color=color, stroke_width=width,
                         max_tip_length_to_length_ratio=0.18)

        # Non-eigenvectors
        v_tips = [
            ([1.5, 0.8], VEC2_COLOR),
            ([-1.0, 1.2], VEC2_COLOR),
            ([0.8, -1.5], VEC2_COLOR),
        ]
        # Eigenvector: [1, 0]
        eigen_tip = ([1.5, 0.0], EIGEN_COLOR)

        v_arrows = VGroup(*[make_arrow(t, c) for t, c in v_tips])
        e_arrow  = make_arrow(*eigen_tip)

        # Labels
        v_labels = VGroup(
            MathTex("v_1", color=VEC2_COLOR, font_size=28)\
                .next_to(make_arrow(*v_tips[0]).get_end(), UR, buff=0.1),
            MathTex("v_2", color=VEC2_COLOR, font_size=28)\
                .next_to(make_arrow(*v_tips[1]).get_end(), UL, buff=0.1),
            MathTex("v_3", color=VEC2_COLOR, font_size=28)\
                .next_to(make_arrow(*v_tips[2]).get_end(), DR, buff=0.1),
        )
        e_label = MathTex("v_{\\text{e}}", color=EIGEN_COLOR, font_size=28)\
            .next_to(e_arrow.get_end(), UR, buff=0.1)

        self.play(
            LaggedStart(*[GrowArrow(a) for a in v_arrows], lag_ratio=0.2),
            GrowArrow(e_arrow),
            run_time=1.5,
        )
        self.play(
            LaggedStart(*[Write(l) for l in v_labels], lag_ratio=0.2),
            Write(e_label),
            run_time=1.0,
        )
        self.wait(0.5)

        # ------------------------------------------------------------------
        # 3. Apply transformation to non-eigenvectors
        # CAPTION: "Av ≠ λv — direction changes"
        # ------------------------------------------------------------------
        caption_change = Text("Direction changes for most vectors",
                              font_size=26, color=VEC2_COLOR)\
            .to_edge(DOWN, buff=0.6)
        self.play(Write(caption_change), run_time=0.6)

        new_v_arrows = VGroup()
        for t, c in v_tips:
            tip2d = A @ np.array(t)
            new_v_arrows.add(make_arrow(tip2d.tolist(), VEC_TRANS_COLOR))

        for orig, new in zip(v_arrows, new_v_arrows):
            self.play(Transform(orig, new), run_time=0.5)
        self.wait(0.3)

        # Fade the labels (they're now misplaced after transform)
        self.play(FadeOut(v_labels), run_time=0.3)

        # ------------------------------------------------------------------
        # 4. Transform the eigenvector — it stays on the same line!
        # CAPTION: "Av = λv — direction preserved!"
        # ------------------------------------------------------------------
        self.play(FadeOut(caption_change), run_time=0.3)

        caption_eigen = Text("Direction preserved! — Av = λv",
                             font_size=26, color=EIGEN_COLOR)\
            .to_edge(DOWN, buff=0.6)

        # Draw the eigenline first
        eigenline = Line(
            np.array([-6, 0, 0]), np.array([6, 0, 0]),
            color=EIGENLINE_COLOR, stroke_width=1.5, stroke_opacity=0.5,
        )
        self.play(Create(eigenline), run_time=0.5)

        # Transform eigenvector: [1.5,0] → [3.0,0]
        new_e_arrow = make_arrow([3.0, 0.0], VEC_TRANS_COLOR, width=5)
        self.play(
            Transform(e_arrow, new_e_arrow),
            Write(caption_eigen),
            run_time=1.0,
        )

        # Flash a lambda label
        lam_label = MathTex(r"\lambda = 2", color=EIGENVAL_COLOR, font_size=36)\
            .next_to(new_e_arrow.get_end(), UP, buff=0.3)
        self.play(FadeIn(lam_label, scale=1.3), run_time=0.6)
        self.wait(0.4)

        # ------------------------------------------------------------------
        # 5. Big visual question
        # ------------------------------------------------------------------
        self.play(
            FadeOut(VGroup(v_arrows, e_arrow, e_label, lam_label,
                           eigenline, caption_eigen, grid)),
            run_time=0.5,
        )

        question = Text(
            'What if a matrix transforms a vector\nwithout changing its direction?',
            font_size=36, color=RESULT_COLOR, line_spacing=1.3,
        ).move_to(ORIGIN + UP * 0.5)

        answer_eigen = Text("→  Eigenvectors", font_size=40,
                            color=EIGEN_COLOR, weight=BOLD)\
            .next_to(question, DOWN, buff=0.5)
        answer_lam   = Text("→  Eigenvalues",  font_size=40,
                            color=EIGENVAL_COLOR, weight=BOLD)\
            .next_to(answer_eigen, DOWN, buff=0.3)

        self.play(Write(question), run_time=1.2)
        self.wait(0.4)
        self.play(FadeIn(answer_eigen, shift=RIGHT * 0.3), run_time=0.7)
        self.play(FadeIn(answer_lam,   shift=RIGHT * 0.3), run_time=0.7)
        self.wait(1.5)

        # ------------------------------------------------------------------
        # 6. Brief capability list — what a matrix can do
        # ------------------------------------------------------------------
        self.play(FadeOut(VGroup(question, answer_eigen, answer_lam)),
                  run_time=0.5)

        capabilities = BulletedList(
            "Rotate vectors",
            "Stretch vectors",
            "Shrink vectors",
            "Reflect vectors",
            "But certain special directions remain unchanged",
            font_size=30,
            buff=0.35,
        ).move_to(ORIGIN)

        # Colour the last item distinctively
        capabilities[-1].set_color(EIGENLINE_COLOR)

        self.play(LaggedStart(*[Write(item) for item in capabilities],
                              lag_ratio=0.3), run_time=2.0)
        self.wait(1.5)

        self.play(FadeOut(capabilities), run_time=0.8)
