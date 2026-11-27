# =============================================================================
# opening.py — Opening Title Frame (0:00–0:10)
# =============================================================================
# NARRATION:
#   (No narration during the opening title card — let the visuals breathe.)
#
# VISUAL INTENT:
#   Dark coordinate grid fades in. Several vectors appear from the origin.
#   A matrix transformation fires: most vectors rotate, one stays on its line.
#   The title card fades in over the grid.
# =============================================================================

from manim import *
from manim.utils.color import ManimColor

# ---------------------------------------------------------------------------
# Project-wide color constants (import from here to keep consistency)
# ---------------------------------------------------------------------------
BG_COLOR        = ManimColor("#111318")   # deep dark charcoal
GRID_COLOR      = ManimColor("#4A5568")   # muted cool slate
AXIS_COLOR      = ManimColor("#64748B")   # slightly lighter slate

VEC_ORIG_COLOR  = ManimColor("#38BDF8")   # electric blue — original vectors
VEC_TRANS_COLOR = ManimColor("#FBBF24")   # amber/gold   — transformed vectors
EIGEN_COLOR     = ManimColor("#38BDF8")   # bright cyan  — eigenvectors
EIGENVAL_COLOR  = ManimColor("#FBBF24")   # amber/gold   — eigenvalues
VEC2_COLOR      = ManimColor("#F87171")   # coral-red    — comparison vectors
EIGENLINE_COLOR = ManimColor("#34D399")   # emerald green — invariant lines
RESULT_COLOR    = ManimColor("#FFFFFF")   # white        — key results
MATRIX_COLOR    = ManimColor("#E2E8F0")   # light grey   — matrix entries
HIGHLIGHT_COLOR = ManimColor("#A78BFA")   # soft violet  — highlights


class OpeningScene(Scene):
    """
    Opening title card: 0:00 – 0:10
    Shows title, subtitle, student details, and a teaser transformation.
    """

    def construct(self):
        self.camera.background_color = BG_COLOR

        # ------------------------------------------------------------------
        # 1. Build the coordinate grid
        # ------------------------------------------------------------------
        grid = NumberPlane(
            x_range=[-7, 7, 1],
            y_range=[-4, 4, 1],
            background_line_style={
                "stroke_color": GRID_COLOR,
                "stroke_width": 1,
                "stroke_opacity": 0.4,
            },
            axis_config={
                "stroke_color": AXIS_COLOR,
                "stroke_width": 2,
            },
            faded_line_ratio=1,
        )
        self.play(FadeIn(grid, run_time=1.2))

        # ------------------------------------------------------------------
        # 2. Show several vectors from the origin
        # VISUAL INTENT: Multiple vectors fan out — representing arbitrary inputs
        # ------------------------------------------------------------------
        v_data = [
            ([2,  1, 0], VEC_ORIG_COLOR),
            ([1,  2, 0], VEC2_COLOR),
            ([-1, 1, 0], VEC2_COLOR),
            ([1, -1, 0], VEC2_COLOR),
        ]
        arrows = VGroup(*[
            Arrow(ORIGIN, np.array(d), buff=0, color=c,
                  stroke_width=4, max_tip_length_to_length_ratio=0.15)
            for d, c in v_data
        ])
        self.play(LaggedStart(*[GrowArrow(a) for a in arrows], lag_ratio=0.25, run_time=1.5))
        self.wait(0.4)

        # ------------------------------------------------------------------
        # 3. Apply matrix transformation A = [[2,0],[0,3]]
        #    — Most vectors change direction; the axis-aligned ones don't.
        # NARRATION: "Watch what happens when a matrix acts on these vectors."
        # ------------------------------------------------------------------
        A = np.array([[2, 0], [0, 3]])

        def transform_arrow(arrow, matrix):
            start = np.array(arrow.get_start())
            end   = np.array(arrow.get_end()[:2])
            new_end = matrix @ end
            return Arrow(ORIGIN, np.append(new_end, 0), buff=0,
                         color=VEC_TRANS_COLOR, stroke_width=4,
                         max_tip_length_to_length_ratio=0.15)

        transformed = VGroup(*[transform_arrow(a, A) for a in arrows])

        self.play(
            Transform(arrows[0], transformed[0]),
            Transform(arrows[1], transformed[1]),
            Transform(arrows[2], transformed[2]),
            Transform(arrows[3], transformed[3]),
            run_time=1.8,
        )
        self.wait(0.3)

        # ------------------------------------------------------------------
        # 4. Highlight eigenvector (x-axis vector stays on its line)
        # VISUAL INTENT: The [1,0] eigenvector glows; a label asks "Why?"
        # ------------------------------------------------------------------
        eigen_arrow = Arrow(ORIGIN, np.array([2, 0, 0]), buff=0,
                            color=EIGENLINE_COLOR, stroke_width=5,
                            max_tip_length_to_length_ratio=0.15)
        self.play(Create(eigen_arrow), run_time=0.8)

        why_label = Text("Why does this vector keep its direction?",
                         font_size=28, color=RESULT_COLOR,
                         font="Sans-Serif").to_edge(DOWN, buff=0.5)
        self.play(Write(why_label), run_time=1.2)
        self.wait(0.5)

        # ------------------------------------------------------------------
        # 5. Title card — fade in over the grid
        # ------------------------------------------------------------------
        title = Text(
            "Eigenvalues & Eigenvectors:",
            font_size=42, color=RESULT_COLOR, weight=BOLD,
        )
        subtitle1 = Text(
            "The Geometry of Matrix Transformations",
            font_size=34, color=EIGEN_COLOR,
        )
        subtitle2 = Text(
            "Linear Algebra & Calculus (M3) — Internal Assessment",
            font_size=22, color=GRID_COLOR,
        )
        student_name = Text("Student Name: ______________________",
                            font_size=20, color=MATRIX_COLOR)
        student_id   = Text("Student ID:   ________________________",
                            font_size=20, color=MATRIX_COLOR)

        title_group = VGroup(title, subtitle1, subtitle2,
                             student_name, student_id)\
            .arrange(DOWN, buff=0.3)\
            .move_to(ORIGIN)

        # Dim the grid a bit so the text reads cleanly
        self.play(
            grid.animate.set_opacity(0.3),
            FadeOut(why_label),
            run_time=0.5,
        )
        self.play(FadeIn(title_group, shift=UP * 0.3), run_time=1.5)
        self.wait(2)

        # Fade everything out to transition into Scene 1
        self.play(FadeOut(VGroup(title_group, arrows, eigen_arrow, grid)),
                  run_time=1.0)
