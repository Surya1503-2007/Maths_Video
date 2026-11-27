# =============================================================================
# scene6_summary.py — Summary & Credits (4:40–5:00)
# =============================================================================
# NARRATION:
#   "Let's bring it all together. The core equation is Av equals lambda v.
#    To find eigenvalues, solve the characteristic equation det(A minus
#    lambda I) equals zero. For each eigenvalue, solve (A minus lambda I)v
#    equals zero to find the eigenvectors.
#    Eigenvalues tell us how much. Eigenvectors tell us in which direction."
#
# VISUAL INTENT:
#   Three boxed key results on a clean dark background.
#   A visual chain: Matrix → Transformation → Invariant Directions →
#   Eigenvectors → Eigenvalues = Scaling Factors.
#   Final quote fades in. Credits roll.
# =============================================================================

from manim import *
from .opening import (BG_COLOR, GRID_COLOR, AXIS_COLOR, VEC_ORIG_COLOR,
                       VEC_TRANS_COLOR, EIGEN_COLOR, EIGENVAL_COLOR,
                       VEC2_COLOR, EIGENLINE_COLOR, RESULT_COLOR,
                       MATRIX_COLOR, HIGHLIGHT_COLOR)


class Scene6Summary(Scene):
    """
    Scene 6 — Summary & Credits: 4:40 – 5:00 (≈20 s) + credits (~10 s)
    """

    def construct(self):
        self.camera.background_color = BG_COLOR

        # ------------------------------------------------------------------
        # 1. Three core takeaways
        # ------------------------------------------------------------------
        title = Text("Summary: The Big Picture",
                     font_size=34, color=EIGEN_COLOR).to_edge(UP, buff=0.4)
        self.play(Write(title), run_time=0.7)

        # Takeaway 1
        tk1_label = Text("1. Definition", font_size=22,
                          color=GRID_COLOR, weight=BOLD)
        tk1_eq    = MathTex(r"\boxed{Av = \lambda v}", font_size=42,
                             color=RESULT_COLOR)
        tk1_desc  = Text("Eigenvectors keep their direction under the transformation.",
                         font_size=20, color=MATRIX_COLOR)
        tk1 = VGroup(tk1_label, tk1_eq, tk1_desc)\
            .arrange(DOWN, buff=0.2, aligned_edge=LEFT)

        # Takeaway 2
        tk2_label = Text("2. Finding Eigenvalues", font_size=22,
                          color=GRID_COLOR, weight=BOLD)
        tk2_eq    = MathTex(r"\boxed{\det(A - \lambda I) = 0}", font_size=38,
                             color=EIGENVAL_COLOR)
        tk2_desc  = Text("Solve the characteristic equation to obtain eigenvalues.",
                         font_size=20, color=MATRIX_COLOR)
        tk2 = VGroup(tk2_label, tk2_eq, tk2_desc)\
            .arrange(DOWN, buff=0.2, aligned_edge=LEFT)

        # Takeaway 3
        tk3_label = Text("3. Finding Eigenvectors", font_size=22,
                          color=GRID_COLOR, weight=BOLD)
        tk3_eq    = MathTex(r"\boxed{(A - \lambda I)v = 0}", font_size=38,
                             color=EIGEN_COLOR)
        tk3_desc  = Text("For each eigenvalue, solve for its eigenvector.",
                         font_size=20, color=MATRIX_COLOR)
        tk3 = VGroup(tk3_label, tk3_eq, tk3_desc)\
            .arrange(DOWN, buff=0.2, aligned_edge=LEFT)

        all_tks = VGroup(tk1, tk2, tk3)\
            .arrange(DOWN, buff=0.45, aligned_edge=LEFT)\
            .next_to(title, DOWN, buff=0.5)\
            .to_edge(LEFT, buff=1.0)

        self.play(
            LaggedStart(
                FadeIn(tk1, shift=RIGHT * 0.3),
                FadeIn(tk2, shift=RIGHT * 0.3),
                FadeIn(tk3, shift=RIGHT * 0.3),
                lag_ratio=0.4,
            ),
            run_time=2.0,
        )
        self.wait(1.2)

        # ------------------------------------------------------------------
        # 2. Visual chain (right side)
        # ------------------------------------------------------------------
        chain_items = [
            ("Matrix  A",              MATRIX_COLOR),
            ("Transformation",          VEC_TRANS_COLOR),
            ("Invariant Directions",    EIGENLINE_COLOR),
            ("Eigenvectors",            EIGEN_COLOR),
            ("Eigenvalues = Scaling",   EIGENVAL_COLOR),
        ]
        chain_texts = VGroup(*[
            Text(label, font_size=22, color=col)
            for label, col in chain_items
        ]).arrange(DOWN, buff=0.28)

        arrows_chain = VGroup(*[
            Arrow(chain_texts[i].get_bottom(),
                  chain_texts[i+1].get_top(),
                  buff=0.08, color=GRID_COLOR, stroke_width=2,
                  max_tip_length_to_length_ratio=0.3)
            for i in range(len(chain_texts)-1)
        ])
        chain_group = VGroup(chain_texts, arrows_chain)\
            .to_edge(RIGHT, buff=1.0)\
            .shift(DOWN * 0.3)

        self.play(
            LaggedStart(
                *[FadeIn(t, shift=DOWN * 0.2) for t in chain_texts],
                lag_ratio=0.3,
            ),
            run_time=1.5,
        )
        self.play(
            LaggedStart(*[GrowArrow(a) for a in arrows_chain], lag_ratio=0.3),
            run_time=1.0,
        )
        self.wait(1.0)

        # ------------------------------------------------------------------
        # 3. Final quote
        # ------------------------------------------------------------------
        self.play(
            FadeOut(VGroup(all_tks, chain_group, title)),
            run_time=0.6,
        )

        final_quote = Text(
            '"Eigenvalues tell us how much.\nEigenvectors tell us in which special directions."',
            font_size=36, color=RESULT_COLOR, line_spacing=1.4,
        ).move_to(ORIGIN)
        self.play(Write(final_quote), run_time=1.5)
        self.wait(2.0)
        self.play(FadeOut(final_quote), run_time=0.8)

        # ------------------------------------------------------------------
        # 4. Credits
        # ------------------------------------------------------------------
        credits_title = Text("References & Credits",
                              font_size=34, color=EIGEN_COLOR)\
            .to_edge(UP, buff=0.4)
        self.play(Write(credits_title), run_time=0.6)

        refs = Text(
            "1. Gilbert Strang — Introduction to Linear Algebra\n"
            "2. 3Blue1Brown — Essence of Linear Algebra\n"
            "3. MIT OpenCourseWare — Linear Algebra\n"
            "4. Standard M3 Linear Algebra Course Material",
            font_size=22, color=MATRIX_COLOR, line_spacing=1.4,
        ).next_to(credits_title, DOWN, buff=0.5).to_edge(LEFT, buff=1.0)

        music_credit = Text(
            "Music: None",
            font_size=20, color=GRID_COLOR,
        ).next_to(refs, DOWN, buff=0.5).to_edge(LEFT, buff=1.0)

        ai_disclosure = Text(
            "AI Tool Disclosure:\n"
            "AI-assisted development was used for code generation,\n"
            "debugging, mathematical visualization planning, and\n"
            "animation workflow assistance using Antigravity IDE / AI tools.\n"
            "All mathematical content was reviewed and verified before rendering.",
            font_size=18, color=GRID_COLOR, line_spacing=1.3,
        ).next_to(music_credit, DOWN, buff=0.4).to_edge(LEFT, buff=1.0)

        self.play(
            LaggedStart(
                FadeIn(refs, shift=UP * 0.2),
                FadeIn(music_credit, shift=UP * 0.2),
                FadeIn(ai_disclosure, shift=UP * 0.2),
                lag_ratio=0.4,
            ),
            run_time=2.0,
        )
        self.wait(3.0)
        self.play(FadeOut(VGroup(credits_title, refs, music_credit,
                                  ai_disclosure)),
                  run_time=1.0)
