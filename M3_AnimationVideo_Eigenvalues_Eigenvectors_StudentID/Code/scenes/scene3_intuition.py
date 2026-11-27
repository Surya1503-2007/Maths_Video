# =============================================================================
# scene3_intuition.py — Visual Intuition (1:40–2:35)
# =============================================================================
# NARRATION:
#   "Let's see the most visually clear example. Take the diagonal matrix
#    A = [[2,0],[0,3]]. It stretches space: 2× horizontally, 3× vertically.
#    A general vector like [1,1] gets mapped to [2,3] — its direction changes.
#    But [1,0] maps to [2,0]. Same line, just doubled. Lambda equals 2.
#    And [0,1] maps to [0,3]. Same line, just tripled. Lambda equals 3.
#    These two special directions — the x-axis and y-axis — are the
#    eigenvector directions. They survive the transformation unchanged."
#
# VISUAL INTENT:
#   Animate an actual linear transformation of the grid.
#   Show general vector changing direction. Show eigenvectors staying put.
#   Animate eigenline overlays. Show pos/neg/zero eigenvalue demos.
# =============================================================================

from manim import *
from .opening import (BG_COLOR, GRID_COLOR, AXIS_COLOR, VEC_ORIG_COLOR,
                       VEC_TRANS_COLOR, EIGEN_COLOR, EIGENVAL_COLOR,
                       VEC2_COLOR, EIGENLINE_COLOR, RESULT_COLOR,
                       MATRIX_COLOR, HIGHLIGHT_COLOR)


class Scene3Intuition(Scene):
    """
    Scene 3 — Visual Intuition: 1:40 – 2:35 (≈55 s)
    Diagonal matrix A = [[2,0],[0,3]] — eigenlines are the axes.
    """

    def construct(self):
        self.camera.background_color = BG_COLOR

        # Scene title
        scene_title = Text("Visual Intuition: Invariant Directions",
                            font_size=32, color=EIGEN_COLOR)\
            .to_edge(UP, buff=0.3)
        self.play(Write(scene_title), run_time=0.8)

        # ------------------------------------------------------------------
        # 1. Build grid and show the matrix
        # ------------------------------------------------------------------
        grid = NumberPlane(
            x_range=[-5, 5, 1], y_range=[-4, 4, 1],
            x_length=10, y_length=8,
            background_line_style={"stroke_color": GRID_COLOR,
                                   "stroke_width": 0.8, "stroke_opacity": 0.4},
            axis_config={"stroke_color": AXIS_COLOR, "stroke_width": 1.5},
        )
        self.play(FadeIn(grid), run_time=0.7)

        mat_label = MathTex(
            r"A = \begin{bmatrix} 2 & 0 \\ 0 & 3 \end{bmatrix}",
            font_size=38, color=MATRIX_COLOR,
        ).to_corner(UR, buff=0.4)
        self.play(Write(mat_label), run_time=0.8)

        # ------------------------------------------------------------------
        # 2. General vector [1,1] → Av = [2,3]  (direction changes)
        # CAPTION: "General vector changes direction"
        # ------------------------------------------------------------------
        v_gen = Arrow(ORIGIN, np.array([1, 1, 0]), buff=0, color=VEC_ORIG_COLOR,
                      stroke_width=4, max_tip_length_to_length_ratio=0.2)
        v_gen_lbl = MathTex(r"v=\begin{bmatrix}1\\1\end{bmatrix}",
                             font_size=28, color=VEC_ORIG_COLOR)\
            .next_to(v_gen.get_end(), UR, buff=0.1)

        self.play(GrowArrow(v_gen), Write(v_gen_lbl), run_time=0.8)

        v_gen_t = Arrow(ORIGIN, np.array([2, 3, 0]), buff=0,
                        color=VEC_TRANS_COLOR, stroke_width=4,
                        max_tip_length_to_length_ratio=0.2)
        v_gen_t_lbl = MathTex(r"Av=\begin{bmatrix}2\\3\end{bmatrix}",
                               font_size=28, color=VEC_TRANS_COLOR)\
            .next_to(v_gen_t.get_end(), UR, buff=0.1)

        cap1 = Text("Direction changes — not an eigenvector",
                    font_size=23, color=VEC2_COLOR).to_edge(DOWN, buff=0.5)
        self.play(Write(cap1), run_time=0.4)
        self.play(
            Transform(v_gen, v_gen_t),
            Transform(v_gen_lbl, v_gen_t_lbl),
            run_time=1.2,
        )
        self.wait(0.8)
        self.play(FadeOut(VGroup(v_gen, v_gen_lbl, cap1)), run_time=0.5)

        # ------------------------------------------------------------------
        # 3. Eigenvector 1: [1,0] → [2,0] = 2·[1,0]   λ = 2
        # ------------------------------------------------------------------
        # Draw x-axis eigenline
        eline1 = Line(np.array([-5, 0, 0]), np.array([5, 0, 0]),
                      color=EIGENLINE_COLOR, stroke_width=2, stroke_opacity=0.6)
        self.play(Create(eline1), run_time=0.5)

        v1 = Arrow(ORIGIN, np.array([1, 0, 0]), buff=0, color=EIGEN_COLOR,
                   stroke_width=5, max_tip_length_to_length_ratio=0.2)
        v1_lbl = MathTex(r"v_1=\begin{bmatrix}1\\0\end{bmatrix}",
                          font_size=28, color=EIGEN_COLOR)\
            .next_to(v1.get_end(), UP, buff=0.3)
        self.play(GrowArrow(v1), Write(v1_lbl), run_time=0.8)

        v1_t = Arrow(ORIGIN, np.array([2, 0, 0]), buff=0,
                     color=VEC_TRANS_COLOR, stroke_width=5,
                     max_tip_length_to_length_ratio=0.2)

        eq1 = MathTex(r"Av_1 = \begin{bmatrix}2\\0\end{bmatrix} = 2v_1",
                       font_size=30, color=VEC_TRANS_COLOR)\
            .to_edge(DOWN, buff=0.9)
        lam1_box = MathTex(r"\boxed{\lambda_1 = 2}",
                            font_size=32, color=EIGENVAL_COLOR)\
            .to_edge(DOWN, buff=0.3)

        self.play(
            Transform(v1, v1_t),
            Write(eq1),
            run_time=1.0,
        )
        self.play(Write(lam1_box), run_time=0.5)
        self.wait(0.8)
        self.play(FadeOut(VGroup(v1, v1_lbl, eq1, lam1_box)), run_time=0.4)

        # ------------------------------------------------------------------
        # 4. Eigenvector 2: [0,1] → [0,3] = 3·[0,1]   λ = 3
        # ------------------------------------------------------------------
        eline2 = Line(np.array([0, -4, 0]), np.array([0, 4, 0]),
                      color=EIGENLINE_COLOR, stroke_width=2, stroke_opacity=0.6)
        self.play(Create(eline2), run_time=0.5)

        v2 = Arrow(ORIGIN, np.array([0, 1, 0]), buff=0, color=EIGEN_COLOR,
                   stroke_width=5, max_tip_length_to_length_ratio=0.2)
        v2_lbl = MathTex(r"v_2=\begin{bmatrix}0\\1\end{bmatrix}",
                          font_size=28, color=EIGEN_COLOR)\
            .next_to(v2.get_end(), RIGHT, buff=0.3)
        self.play(GrowArrow(v2), Write(v2_lbl), run_time=0.8)

        v2_t = Arrow(ORIGIN, np.array([0, 3, 0]), buff=0,
                     color=VEC_TRANS_COLOR, stroke_width=5,
                     max_tip_length_to_length_ratio=0.2)

        eq2 = MathTex(r"Av_2 = \begin{bmatrix}0\\3\end{bmatrix} = 3v_2",
                       font_size=30, color=VEC_TRANS_COLOR)\
            .to_edge(DOWN, buff=0.9)
        lam2_box = MathTex(r"\boxed{\lambda_2 = 3}",
                            font_size=32, color=EIGENVAL_COLOR)\
            .to_edge(DOWN, buff=0.3)

        self.play(Transform(v2, v2_t), Write(eq2), run_time=1.0)
        self.play(Write(lam2_box), run_time=0.5)
        self.wait(0.8)
        self.play(FadeOut(VGroup(v2, v2_lbl, eq2, lam2_box)), run_time=0.4)

        # ------------------------------------------------------------------
        # 5. Apply the actual linear transformation to the grid
        # VISUAL INTENT: Grid stretches 2× horizontally, 3× vertically;
        #                eigenlines stay fixed.
        # ------------------------------------------------------------------
        cap_transform = Text("Applying A: horizontal ×2, vertical ×3",
                             font_size=24, color=GRID_COLOR)\
            .to_edge(DOWN, buff=0.5)
        self.play(Write(cap_transform), run_time=0.4)

        A_mat = [[2, 0], [0, 3]]
        self.play(
            grid.animate.apply_matrix(A_mat),
            run_time=2.0,
            rate_func=smooth,
        )
        self.wait(0.5)
        self.play(FadeOut(cap_transform), run_time=0.3)

        # Key callout
        callout = Text(
            "Eigenvectors are directions that survive the\n"
            "transformation unchanged — except for scaling.",
            font_size=28, color=RESULT_COLOR, line_spacing=1.3,
        ).to_corner(DL, buff=0.4)
        self.play(Write(callout), run_time=1.2)
        self.wait(1.0)

        # ------------------------------------------------------------------
        # 6. Three eigenvalue sign demos (compact, below the grid)
        # ------------------------------------------------------------------
        self.play(FadeOut(VGroup(grid, eline1, eline2, mat_label,
                                  callout, scene_title)),
                  run_time=0.6)

        # --- Positive ---
        pos_title = MathTex(r"\lambda > 0", color=EIGENVAL_COLOR, font_size=36)\
            .shift(LEFT * 4.5 + UP * 1.5)
        pos_arr   = Arrow(ORIGIN + LEFT*4.5, np.array([-4.5+2, 0, 0]),
                          buff=0, color=EIGEN_COLOR, stroke_width=4,
                          max_tip_length_to_length_ratio=0.2)
        pos_cap   = Text("Keeps direction", font_size=20, color=EIGEN_COLOR)\
            .next_to(pos_arr, DOWN, buff=0.2)

        # --- Negative ---
        neg_title = MathTex(r"\lambda < 0", color=VEC2_COLOR, font_size=36)\
            .shift(UP * 1.5)
        neg_arr   = Arrow(ORIGIN + RIGHT*0.5, np.array([-1.0, 0, 0]),
                          buff=0, color=EIGEN_COLOR, stroke_width=4,
                          max_tip_length_to_length_ratio=0.2)
        neg_cap   = Text("Reverses direction", font_size=20, color=VEC2_COLOR)\
            .next_to(neg_arr, DOWN, buff=0.2)

        # --- Zero ---
        zero_title = MathTex(r"\lambda = 0", color=GRID_COLOR, font_size=36)\
            .shift(RIGHT * 4.5 + UP * 1.5)
        zero_dot  = Dot(np.array([4.5, 0, 0]), color=VEC2_COLOR, radius=0.12)
        zero_cap  = Text("Collapses to origin", font_size=20, color=GRID_COLOR)\
            .next_to(zero_dot, DOWN, buff=0.2)

        self.play(
            LaggedStart(
                Write(pos_title), GrowArrow(pos_arr), Write(pos_cap),
                Write(neg_title), GrowArrow(neg_arr), Write(neg_cap),
                Write(zero_title), FadeIn(zero_dot), Write(zero_cap),
                lag_ratio=0.3,
            ),
            run_time=3.0,
        )
        self.wait(1.5)
        self.play(FadeOut(VGroup(pos_title, pos_arr, pos_cap,
                                  neg_title, neg_arr, neg_cap,
                                  zero_title, zero_dot, zero_cap)),
                  run_time=0.8)
