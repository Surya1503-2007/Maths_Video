# =============================================================================
# scene4_worked_example.py — Worked Example (2:35–4:10)
# =============================================================================
# NARRATION:
#   "Now let's find eigenvalues and eigenvectors for a concrete matrix:
#    A = [[4,1],[2,3]].
#    We start from Av = λv, rearrange to (A − λI)v = 0.
#    For a non-trivial solution, A − λI must be singular, meaning its
#    determinant is zero. This gives us the characteristic equation.
#    Solving it yields our eigenvalues. Then we substitute each eigenvalue
#    back to find the corresponding eigenvector."
#
# VISUAL INTENT:
#   Step-by-step equation build using TransformMatchingTex.
#   Amber highlights on eigenvalues, green on verification.
#   Each step fades to make room for the next.
# =============================================================================

from manim import *
from .opening import (BG_COLOR, GRID_COLOR, AXIS_COLOR, VEC_ORIG_COLOR,
                       VEC_TRANS_COLOR, EIGEN_COLOR, EIGENVAL_COLOR,
                       VEC2_COLOR, EIGENLINE_COLOR, RESULT_COLOR,
                       MATRIX_COLOR, HIGHLIGHT_COLOR)


def step_header(text, color=EIGEN_COLOR, size=28):
    return Text(text, font_size=size, color=color)


class Scene4WorkedExample(Scene):
    """
    Scene 4 — Worked Example: 2:35 – 4:10 (≈95 s)
    Full derivation for A = [[4,1],[2,3]].
    """

    def construct(self):
        self.camera.background_color = BG_COLOR

        # ══════════════════════════════════════════════════════════════════
        # STEP 0 — Set up and announce the matrix
        # ══════════════════════════════════════════════════════════════════
        scene_title = Text("Worked Example: Finding Eigenvalues & Eigenvectors",
                           font_size=28, color=EIGEN_COLOR).to_edge(UP, buff=0.3)
        mat_tex = MathTex(
            r"A = \begin{bmatrix} 4 & 1 \\ 2 & 3 \end{bmatrix}",
            font_size=48, color=MATRIX_COLOR,
        ).next_to(scene_title, DOWN, buff=0.5)

        self.play(Write(scene_title), Write(mat_tex), run_time=1.2)
        self.wait(0.5)

        # Starting equation
        eq0 = MathTex(r"Av = \lambda v", font_size=48, color=RESULT_COLOR)\
            .next_to(mat_tex, DOWN, buff=0.5)
        self.play(Write(eq0), run_time=0.8)
        self.wait(0.4)

        # ══════════════════════════════════════════════════════════════════
        # STEP 1 — Rearrange: Av − λv = 0 → (A − λI)v = 0
        # ══════════════════════════════════════════════════════════════════
        eq1 = MathTex(r"Av - \lambda v = 0", font_size=48, color=RESULT_COLOR)\
            .next_to(mat_tex, DOWN, buff=0.5)
        self.play(TransformMatchingTex(eq0, eq1), run_time=1.0)
        self.wait(0.3)

        eq2 = MathTex(r"(A - \lambda I)v = 0", font_size=48, color=RESULT_COLOR)\
            .next_to(mat_tex, DOWN, buff=0.5)
        self.play(TransformMatchingTex(eq1, eq2), run_time=1.0)
        self.wait(0.4)

        explain = Text(
            "For a non-zero eigenvector v,  (A − λI) must be singular:",
            font_size=23, color=GRID_COLOR,
        ).next_to(eq2, DOWN, buff=0.4)
        self.play(FadeIn(explain), run_time=0.6)

        eq3 = MathTex(r"\det(A - \lambda I) = 0", font_size=48,
                       color=EIGENVAL_COLOR)\
            .next_to(explain, DOWN, buff=0.4)
        box_eq3 = SurroundingRectangle(eq3, color=EIGENLINE_COLOR,
                                        buff=0.2, stroke_width=2)
        self.play(Write(eq3), Create(box_eq3), run_time=0.9)
        self.wait(0.8)

        self.play(FadeOut(VGroup(eq2, explain, eq3, box_eq3,
                                  mat_tex, scene_title)),
                  run_time=0.5)

        # ══════════════════════════════════════════════════════════════════
        # STEP 2 — Construct A − λI
        # ══════════════════════════════════════════════════════════════════
        hdr2 = step_header("Step 1: Construct  A − λI").to_edge(UP, buff=0.4)
        self.play(Write(hdr2), run_time=0.6)

        mat_diff_full = MathTex(
            r"A - \lambda I "
            r"= \begin{bmatrix} 4 & 1 \\ 2 & 3 \end{bmatrix}"
            r"- \begin{bmatrix} \lambda & 0 \\ 0 & \lambda \end{bmatrix}",
            font_size=38, color=MATRIX_COLOR,
        ).next_to(hdr2, DOWN, buff=0.5)
        self.play(Write(mat_diff_full), run_time=1.2)
        self.wait(0.5)

        mat_diff_result = MathTex(
            r"= \begin{bmatrix} 4-\lambda & 1 \\ 2 & 3-\lambda \end{bmatrix}",
            font_size=42, color=MATRIX_COLOR,
        ).next_to(mat_diff_full, DOWN, buff=0.4)
        # Highlight the diagonal entries
        mat_diff_result[0][1:8].set_color(EIGENVAL_COLOR)   # 4-λ
        mat_diff_result[0][11:16].set_color(EIGENVAL_COLOR)  # 3-λ

        self.play(Write(mat_diff_result), run_time=1.0)
        self.wait(0.8)
        self.play(FadeOut(VGroup(hdr2, mat_diff_full, mat_diff_result)),
                  run_time=0.5)

        # ══════════════════════════════════════════════════════════════════
        # STEP 3 — Characteristic Equation
        # ══════════════════════════════════════════════════════════════════
        hdr3 = step_header("Step 2: Characteristic Equation").to_edge(UP, buff=0.4)
        self.play(Write(hdr3), run_time=0.6)

        char_eq = MathTex(
            r"\det \begin{bmatrix} 4-\lambda & 1 \\ 2 & 3-\lambda \end{bmatrix} = 0",
            font_size=38, color=RESULT_COLOR,
        ).next_to(hdr3, DOWN, buff=0.5)
        self.play(Write(char_eq), run_time=1.0)
        self.wait(0.4)

        expand1 = MathTex(
            r"(4-\lambda)(3-\lambda) - (1)(2) = 0",
            font_size=38, color=RESULT_COLOR,
        ).next_to(char_eq, DOWN, buff=0.5)
        self.play(Write(expand1), run_time=0.9)
        self.wait(0.4)

        expand2 = MathTex(
            r"12 - 7\lambda + \lambda^2 - 2 = 0",
            font_size=38, color=RESULT_COLOR,
        ).next_to(expand1, DOWN, buff=0.4)
        self.play(Write(expand2), run_time=0.9)
        self.wait(0.3)

        expand3 = MathTex(
            r"\lambda^2 - 7\lambda + 10 = 0",
            font_size=42, color=EIGENVAL_COLOR,
        ).next_to(expand2, DOWN, buff=0.4)
        self.play(Write(expand3), run_time=0.8)
        self.wait(0.3)

        factored = MathTex(
            r"(\lambda - 5)(\lambda - 2) = 0",
            font_size=42, color=EIGENVAL_COLOR,
        ).next_to(expand3, DOWN, buff=0.4)
        self.play(TransformMatchingTex(expand3.copy(), factored), run_time=1.0)
        self.wait(0.4)

        # Eigenvalue results
        eigenvals = MathTex(
            r"\boxed{\lambda_1 = 5}, \quad \boxed{\lambda_2 = 2}",
            font_size=46, color=EIGENVAL_COLOR,
        ).next_to(factored, DOWN, buff=0.5)
        self.play(Write(eigenvals), run_time=0.8)
        self.wait(1.0)

        self.play(FadeOut(VGroup(hdr3, char_eq, expand1, expand2,
                                  factored, eigenvals)),
                  expand3.animate.to_edge(UP, buff=0.4).set_color(GRID_COLOR),
                  run_time=0.7)

        # ══════════════════════════════════════════════════════════════════
        # STEP 4 — Eigenvector for λ = 5
        # ══════════════════════════════════════════════════════════════════
        hdr4 = step_header("Step 3: Eigenvector for  λ₁ = 5",
                            color=EIGENVAL_COLOR).next_to(expand3, DOWN, buff=0.3)
        self.play(Write(hdr4), run_time=0.6)

        sys1_mat = MathTex(
            r"(A - 5I)v = 0 \quad \Rightarrow \quad"
            r"\begin{bmatrix} -1 & 1 \\ 2 & -2 \end{bmatrix}"
            r"\begin{bmatrix} x \\ y \end{bmatrix}"
            r"= \begin{bmatrix} 0 \\ 0 \end{bmatrix}",
            font_size=34, color=RESULT_COLOR,
        ).next_to(hdr4, DOWN, buff=0.4)
        self.play(Write(sys1_mat), run_time=1.2)
        self.wait(0.4)

        sys1_eq = MathTex(r"-x + y = 0 \quad \Rightarrow \quad y = x",
                           font_size=36, color=RESULT_COLOR)\
            .next_to(sys1_mat, DOWN, buff=0.4)
        self.play(Write(sys1_eq), run_time=0.8)
        self.wait(0.3)

        v1_result = MathTex(
            r"\text{Choose } x=1: \quad"
            r"\boxed{v_1 = \begin{bmatrix} 1 \\ 1 \end{bmatrix}}",
            font_size=38, color=EIGEN_COLOR,
        ).next_to(sys1_eq, DOWN, buff=0.4)
        self.play(Write(v1_result), run_time=0.9)
        self.wait(1.0)

        self.play(FadeOut(VGroup(hdr4, sys1_mat, sys1_eq)),
                  v1_result.animate.to_corner(DL, buff=0.4).scale(0.8),
                  run_time=0.6)

        # ══════════════════════════════════════════════════════════════════
        # STEP 5 — Eigenvector for λ = 2
        # ══════════════════════════════════════════════════════════════════
        hdr5 = step_header("Step 4: Eigenvector for  λ₂ = 2",
                            color=EIGENVAL_COLOR).next_to(expand3, DOWN, buff=0.3)
        self.play(Write(hdr5), run_time=0.6)

        sys2_mat = MathTex(
            r"(A - 2I)v = 0 \quad \Rightarrow \quad"
            r"\begin{bmatrix} 2 & 1 \\ 2 & 1 \end{bmatrix}"
            r"\begin{bmatrix} x \\ y \end{bmatrix}"
            r"= \begin{bmatrix} 0 \\ 0 \end{bmatrix}",
            font_size=34, color=RESULT_COLOR,
        ).next_to(hdr5, DOWN, buff=0.4)
        self.play(Write(sys2_mat), run_time=1.2)
        self.wait(0.4)

        sys2_eq = MathTex(r"2x + y = 0 \quad \Rightarrow \quad y = -2x",
                           font_size=36, color=RESULT_COLOR)\
            .next_to(sys2_mat, DOWN, buff=0.4)
        self.play(Write(sys2_eq), run_time=0.8)
        self.wait(0.3)

        v2_result = MathTex(
            r"\text{Choose } x=1: \quad"
            r"\boxed{v_2 = \begin{bmatrix} 1 \\ -2 \end{bmatrix}}",
            font_size=38, color=EIGEN_COLOR,
        ).next_to(sys2_eq, DOWN, buff=0.4)
        self.play(Write(v2_result), run_time=0.9)
        self.wait(1.0)

        self.play(FadeOut(VGroup(hdr5, sys2_mat, sys2_eq)),
                  v2_result.animate.to_corner(DR, buff=0.4).scale(0.8),
                  run_time=0.6)

        # ══════════════════════════════════════════════════════════════════
        # STEP 6 — Verification
        # ══════════════════════════════════════════════════════════════════
        self.play(FadeOut(expand3), run_time=0.3)

        hdr6 = step_header("Step 5: Verification", color=EIGENLINE_COLOR,
                            size=30).to_edge(UP, buff=0.4)
        self.play(Write(hdr6), run_time=0.6)

        # Verify v1
        ver1 = MathTex(
            r"Av_1 = \begin{bmatrix}4&1\\2&3\end{bmatrix}"
            r"\begin{bmatrix}1\\1\end{bmatrix}"
            r"= \begin{bmatrix}5\\5\end{bmatrix}",
            font_size=34, color=RESULT_COLOR,
        ).next_to(hdr6, DOWN, buff=0.4)
        ver1_check = MathTex(
            r"5v_1 = \begin{bmatrix}5\\5\end{bmatrix}"
            r"\quad \Rightarrow \quad \boxed{Av_1 = 5v_1} \checkmark",
            font_size=34, color=EIGENLINE_COLOR,
        ).next_to(ver1, DOWN, buff=0.3)

        self.play(Write(ver1), run_time=1.0)
        self.play(Write(ver1_check), run_time=0.9)
        self.wait(0.6)

        # Verify v2
        ver2 = MathTex(
            r"Av_2 = \begin{bmatrix}4&1\\2&3\end{bmatrix}"
            r"\begin{bmatrix}1\\-2\end{bmatrix}"
            r"= \begin{bmatrix}2\\-4\end{bmatrix}",
            font_size=34, color=RESULT_COLOR,
        ).next_to(ver1_check, DOWN, buff=0.4)
        ver2_check = MathTex(
            r"2v_2 = \begin{bmatrix}2\\-4\end{bmatrix}"
            r"\quad \Rightarrow \quad \boxed{Av_2 = 2v_2} \checkmark",
            font_size=34, color=EIGENLINE_COLOR,
        ).next_to(ver2, DOWN, buff=0.3)

        self.play(Write(ver2), run_time=1.0)
        self.play(Write(ver2_check), run_time=0.9)
        self.wait(1.2)

        self.play(FadeOut(VGroup(hdr6, ver1, ver1_check, ver2, ver2_check,
                                  v1_result, v2_result)),
                  run_time=0.8)
