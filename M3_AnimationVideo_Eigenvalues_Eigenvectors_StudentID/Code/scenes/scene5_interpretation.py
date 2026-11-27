# =============================================================================
# scene5_interpretation.py — Interpretation (4:10–4:40)
# =============================================================================
# NARRATION:
#   "Let's return to the coordinate plane and see what we just found.
#    The vector [1,1] is an eigenvector with eigenvalue 5.
#    The matrix stretches it to [5,5] — five times as long, same direction.
#    The vector [1,-2] is an eigenvector with eigenvalue 2.
#    The matrix stretches it to [2,-4] — twice as long, same direction.
#    But a standard vector like [1,0] maps to [4,2] — it rotates away.
#    The eigenvector directions are the backbone of the transformation."
#
# VISUAL INTENT:
#   Plot v1, v2 on a coordinate plane.
#   Animate the matrix transformation for each.
#   Draw eigenlines, label scaling factors.
#   Show a non-eigenvector changing direction as contrast.
# =============================================================================

from manim import *
from .opening import (BG_COLOR, GRID_COLOR, AXIS_COLOR, VEC_ORIG_COLOR,
                       VEC_TRANS_COLOR, EIGEN_COLOR, EIGENVAL_COLOR,
                       VEC2_COLOR, EIGENLINE_COLOR, RESULT_COLOR,
                       MATRIX_COLOR, HIGHLIGHT_COLOR)


class Scene5Interpretation(Scene):
    """
    Scene 5 — Interpretation: 4:10 – 4:40 (≈30 s)
    Geometric visualization of the two eigenvectors of A = [[4,1],[2,3]].
    """

    def construct(self):
        self.camera.background_color = BG_COLOR

        # ------------------------------------------------------------------
        # 1. Build coordinate grid
        # ------------------------------------------------------------------
        grid = NumberPlane(
            x_range=[-2, 6, 1], y_range=[-5, 6, 1],
            x_length=10, y_length=9,
            background_line_style={"stroke_color": GRID_COLOR,
                                   "stroke_width": 0.8, "stroke_opacity": 0.35},
            axis_config={"stroke_color": AXIS_COLOR, "stroke_width": 1.5},
        ).shift(DOWN * 0.3)
        self.play(FadeIn(grid), run_time=0.8)

        mat_label = MathTex(
            r"A = \begin{bmatrix} 4 & 1 \\ 2 & 3 \end{bmatrix}",
            font_size=30, color=MATRIX_COLOR,
        ).to_corner(UR, buff=0.4)
        self.play(Write(mat_label), run_time=0.6)

        # ------------------------------------------------------------------
        # 2. Plot and transform v1 = [1,1]  → [5,5]   λ=5
        # ------------------------------------------------------------------
        # Eigenline for v1 (direction [1,1])
        eline1 = Line(np.array([-2, -2, 0]), np.array([6, 6, 0]),
                      color=EIGENLINE_COLOR, stroke_width=1.5, stroke_opacity=0.5)
        self.play(Create(eline1), run_time=0.5)

        v1 = Arrow(grid.get_origin(), grid.c2p(1, 1), buff=0,
                   color=EIGEN_COLOR, stroke_width=5,
                   max_tip_length_to_length_ratio=0.15)
        v1_lbl = MathTex(r"v_1 = \begin{bmatrix}1\\1\end{bmatrix}",
                          font_size=26, color=EIGEN_COLOR)\
            .next_to(grid.c2p(1, 1), UR, buff=0.1)
        self.play(GrowArrow(v1), Write(v1_lbl), run_time=0.8)

        # Animate to Av1 = [5,5]
        v1_t = Arrow(grid.get_origin(), grid.c2p(5, 5), buff=0,
                     color=VEC_TRANS_COLOR, stroke_width=5,
                     max_tip_length_to_length_ratio=0.15)
        v1_t_lbl = MathTex(r"Av_1 = \begin{bmatrix}5\\5\end{bmatrix}",
                            font_size=26, color=VEC_TRANS_COLOR)\
            .next_to(grid.c2p(5, 5), UR, buff=0.1)

        lam1_cap = Text("×5 along the same direction", font_size=22,
                        color=EIGENVAL_COLOR).to_edge(DOWN, buff=0.5)
        self.play(Write(lam1_cap), run_time=0.4)
        self.play(
            Transform(v1, v1_t),
            Transform(v1_lbl, v1_t_lbl),
            run_time=1.2,
        )
        self.wait(0.6)
        self.play(FadeOut(lam1_cap), run_time=0.3)

        # ------------------------------------------------------------------
        # 3. Plot and transform v2 = [1,-2] → [2,-4]  λ=2
        # ------------------------------------------------------------------
        # Eigenline for v2 (direction [1,-2])
        eline2 = Line(np.array([-1, 2, 0]), np.array([5, -10, 0]),
                      color=EIGENLINE_COLOR, stroke_width=1.5, stroke_opacity=0.5)
        self.play(Create(eline2), run_time=0.5)

        v2 = Arrow(grid.get_origin(), grid.c2p(1, -2), buff=0,
                   color=EIGEN_COLOR, stroke_width=5,
                   max_tip_length_to_length_ratio=0.15)
        v2_lbl = MathTex(r"v_2 = \begin{bmatrix}1\\-2\end{bmatrix}",
                          font_size=26, color=EIGEN_COLOR)\
            .next_to(grid.c2p(1, -2), RIGHT, buff=0.15)
        self.play(GrowArrow(v2), Write(v2_lbl), run_time=0.8)

        v2_t = Arrow(grid.get_origin(), grid.c2p(2, -4), buff=0,
                     color=VEC_TRANS_COLOR, stroke_width=5,
                     max_tip_length_to_length_ratio=0.15)
        v2_t_lbl = MathTex(r"Av_2 = \begin{bmatrix}2\\-4\end{bmatrix}",
                            font_size=26, color=VEC_TRANS_COLOR)\
            .next_to(grid.c2p(2, -4), RIGHT, buff=0.15)

        lam2_cap = Text("×2 along the same direction", font_size=22,
                        color=EIGENVAL_COLOR).to_edge(DOWN, buff=0.5)
        self.play(Write(lam2_cap), run_time=0.4)
        self.play(
            Transform(v2, v2_t),
            Transform(v2_lbl, v2_t_lbl),
            run_time=1.2,
        )
        self.wait(0.6)
        self.play(FadeOut(lam2_cap), run_time=0.3)

        # ------------------------------------------------------------------
        # 4. Contrast: non-eigenvector [1,0] → [4,2]  (direction changes)
        # ------------------------------------------------------------------
        v_non = Arrow(grid.get_origin(), grid.c2p(1, 0), buff=0,
                      color=VEC2_COLOR, stroke_width=4,
                      max_tip_length_to_length_ratio=0.2)
        v_non_lbl = MathTex(r"\begin{bmatrix}1\\0\end{bmatrix}",
                             font_size=24, color=VEC2_COLOR)\
            .next_to(grid.c2p(1, 0), DOWN, buff=0.15)
        self.play(GrowArrow(v_non), Write(v_non_lbl), run_time=0.7)

        v_non_t = Arrow(grid.get_origin(), grid.c2p(4, 2), buff=0,
                        color=VEC2_COLOR, stroke_width=4, stroke_opacity=0.6,
                        max_tip_length_to_length_ratio=0.2)
        v_non_t_lbl = MathTex(r"\begin{bmatrix}4\\2\end{bmatrix}",
                               font_size=24, color=VEC2_COLOR)\
            .next_to(grid.c2p(4, 2), UR, buff=0.1)
        non_cap = Text("Direction changed — not an eigenvector",
                       font_size=22, color=VEC2_COLOR).to_edge(DOWN, buff=0.5)
        self.play(Write(non_cap), run_time=0.4)
        self.play(
            Transform(v_non, v_non_t),
            Transform(v_non_lbl, v_non_t_lbl),
            run_time=1.0,
        )
        self.wait(0.6)
        self.play(FadeOut(non_cap), run_time=0.3)

        # ------------------------------------------------------------------
        # 5. Main insight text
        # ------------------------------------------------------------------
        self.play(
            FadeOut(VGroup(grid, eline1, eline2, mat_label,
                           v1, v1_lbl, v2, v2_lbl, v_non, v_non_lbl)),
            run_time=0.6,
        )

        insight1 = Text(
            '"An eigenvector is not just a vector with a special value.\n'
            ' It is a direction that the transformation preserves."',
            font_size=30, color=RESULT_COLOR, line_spacing=1.3,
        ).move_to(ORIGIN + UP * 0.5)
        insight2 = MathTex(
            r"Av = \lambda v \quad \Leftrightarrow \quad"
            r"\text{vector stays on its own line}",
            font_size=30, color=EIGEN_COLOR,
        ).next_to(insight1, DOWN, buff=0.6)

        self.play(Write(insight1), run_time=1.5)
        self.play(Write(insight2), run_time=1.0)
        self.wait(1.5)

        self.play(FadeOut(VGroup(insight1, insight2)), run_time=0.8)
