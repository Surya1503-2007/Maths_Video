# Storyboard — Eigenvalues & Eigenvectors: M3 Mathematical Animation

> A scene-by-scene reference document. Each scene can be understood independently before running the code.

---

## Opening Frame — 0:00–0:10

| Field | Content |
|-------|---------|
| **Scene Number** | 0 (Opening) |
| **Scene Title** | "Eigenvalues & Eigenvectors: The Geometry of Matrix Transformations" |
| **Duration** | 0:00 – 0:10 |
| **Visual Description** | Dark charcoal canvas. A coordinate grid (#4A5568) fades in. Four vectors in electric blue and coral red emerge from the origin. A matrix A = [[2,0],[0,3]] fires: most vectors change direction (now amber/gold). One vector on the x-axis stays on its line. It is highlighted in emerald green. Title text fades over a dimmed grid. |
| **Mathematical Content** | A = [[2,0],[0,3]] (teaser). Text: "Why does this vector keep its direction?" |
| **Animation / Transition** | FadeIn grid → GrowArrow × 4 → Transform to Av → emerald highlight → FadeIn title card |
| **On-Screen Text** | "Eigenvalues & Eigenvectors: The Geometry of Matrix Transformations" / "Linear Algebra & Calculus (M3) — Internal Assessment" / Student Name / Student ID |
| **Narration** | (Silent — let visuals create the hook) |
| **Learning Objective** | Establish visual curiosity: why does one vector survive the transformation? |
| **Color Coding** | Grid: #4A5568 · Original vectors: #38BDF8 · Transformed: #FBBF24 · Special eigenvector: #34D399 |
| **Camera Movement** | Static, centered on origin |

---

## Scene 1 — Hook / Context — 0:10–0:50

| Field | Content |
|-------|---------|
| **Scene Number** | 1 |
| **Scene Title** | "What Makes One Vector Special?" |
| **Duration** | 0:10 – 0:50 (≈ 40 s) |
| **Visual Description** | Fresh coordinate grid. Four vectors fan out: v₁ (blue), v₂ v₃ v₄ (coral). Matrix A = [[2,0],[0,3]] transforms them — coral vectors rotate to amber. An emerald eigenline appears on the x-axis. The eigenvector animates to twice its length, still on the same line. λ=2 appears. Black screen shows "What if a matrix transforms a vector without changing direction?" → "→ Eigenvectors / → Eigenvalues". Bullet list of matrix capabilities. |
| **Mathematical Content** | Av ≠ λv for general vectors. Av = λv for the special vector. λ = 2 shown. |
| **Animation / Transition** | GrowArrow × 4 → Transform → eigenline Create → eigenvector Transform → FadeOut grid → Write question → FadeIn answers → BulletedList |
| **On-Screen Text** | "Direction changes for most vectors" / "Direction preserved! — Av = λv" / "λ = 2" / The five-item bullet list |
| **Narration** | "Watch what happens when a matrix acts on these vectors. Most spin around — their direction completely changes. But look at this one. It stays on the same line. What is so special about it?" |
| **Learning Objective** | Geometric introduction: eigenvectors are directions that survive transformation. |
| **Color Coding** | Comparison vectors: #F87171 · Eigenvector: #38BDF8 · Eigenline: #34D399 · λ label: #FBBF24 |
| **Camera Movement** | Static, light zoom on eigenvector highlight |

---

## Scene 2 — Concept Introduction — 0:50–1:40

| Field | Content |
|-------|---------|
| **Scene Number** | 2 |
| **Scene Title** | "The Mathematical Definition" |
| **Duration** | 0:50 – 1:40 (≈ 50 s) |
| **Visual Description** | Dark canvas. Build Av = λv piece by piece: "Av" (blue) → "Av = λv" (multi-colour) → boxed result + component labels. Learning objective text. Mini coordinate grid. λ=3: arrow [1,0] → [3,0] (stretches). λ=-2: arrow [1.5,0] → [-3,0] (reverses). |
| **Mathematical Content** | Av = λv. A = matrix, v = eigenvector, λ = eigenvalue. Av = 3v (triple stretch). Av = -2v (reverse and double). |
| **Animation / Transition** | TransformMatchingTex: "Av" → "Av = λv" → boxed. FadeIn components. Write objective. FadeIn mini grid. Transform arrows. |
| **On-Screen Text** | "Av" → "Av = λv" (boxed). "A = square matrix", "v = eigenvector", "λ = eigenvalue", "Av = transformed vector", "λv = scaled original". Learning objective sentence. "Av = 3v" / "Av = -2v". |
| **Narration** | "The defining equation is A times v equals lambda times v. A is the matrix, v is the eigenvector, lambda is the eigenvalue. The left side transforms the vector; the right side just scales it. When lambda is 3, the vector triples. When lambda is negative 2, it reverses and doubles." |
| **Learning Objective** | Formally establish Av = λv and its geometric meaning. |
| **Color Coding** | A: #E2E8F0 · v: #38BDF8 · λ: #FBBF24 · Av: #FBBF24 · box: #34D399 |
| **Camera Movement** | Static; mild scale-in on the boxed equation |

---

## Scene 3 — Visual Intuition — 1:40–2:35

| Field | Content |
|-------|---------|
| **Scene Number** | 3 |
| **Scene Title** | "Eigenvectors Are Invariant Directions" |
| **Duration** | 1:40 – 2:35 (≈ 55 s) |
| **Visual Description** | Full coordinate grid. Matrix A = [[2,0],[0,3]] labeled top-right. General vector [1,1] → [2,3] animates (direction change, blue→amber). x-axis eigenline (emerald). v₁=[1,0] → [2,0] (λ=2 boxed). y-axis eigenline (emerald). v₂=[0,1] → [0,3] (λ=3 boxed). Full grid transformation animates (stretches 2×H, 3×V). Eigenlines stay fixed. Key callout. Three eigenvalue sign demos in a horizontal strip. |
| **Mathematical Content** | A = [[2,0],[0,3]]. Av = [2,3] ≠ 2[1,1]. Av₁ = [2,0] = 2v₁ → λ₁=2. Av₂ = [0,3] = 3v₂ → λ₂=3. λ>0 / λ<0 / λ=0 demos. |
| **Animation / Transition** | FadeIn grid → Write mat_label → GrowArrow v_gen → Transform v_gen → FadeOut → Create eigenline → GrowArrow v₁ → Transform v₁ → Write λ₁ box → repeat for v₂ → grid.animate.apply_matrix → Write callout → FadeOut → three-panel sign demo |
| **On-Screen Text** | "A = [[2,0],[0,3]]". "Direction changes — not an eigenvector". "Av₁ = [2,0] = 2v₁" / "λ₁=2" (boxed). "Av₂ = [0,3] = 3v₂" / "λ₂=3" (boxed). "Applying A: horizontal ×2, vertical ×3". "Eigenvectors are directions that survive the transformation unchanged — except for scaling." λ>0 / λ<0 / λ=0 panels. |
| **Narration** | "Take the diagonal matrix [[2,0],[0,3]]. The vector [1,1] maps to [2,3] — direction changed. But [1,0] maps to [2,0] — same line, just doubled. Lambda equals 2. And [0,1] maps to [0,3] — same line, just tripled. Lambda equals 3." |
| **Learning Objective** | Build deep geometric intuition: eigenlines = invariant directions; eigenvalue = stretching factor. |
| **Color Coding** | General vector: #38BDF8→#FBBF24 · Eigenvectors: #38BDF8 · Eigenlines: #34D399 · λ boxes: #FBBF24 |
| **Camera Movement** | Slight pull-back as grid stretches |

---

## Scene 4 — Worked Example — 2:35–4:10

| Field | Content |
|-------|---------|
| **Scene Number** | 4 |
| **Scene Title** | "How Do We Find Eigenvalues and Eigenvectors?" |
| **Duration** | 2:35 – 4:10 (≈ 95 s) |
| **Visual Description** | Dark canvas with step headers. Five algebraic sub-steps are displayed sequentially: (0) state A and Av=λv; (1) rearrange to det(A-λI)=0; (2) construct A-λI; (3) solve characteristic polynomial; (4) find eigenvectors for each eigenvalue; (5) verify. TransformMatchingTex used for equation morphs. Amber highlights on eigenvalues; green checkmarks on verification. |
| **Mathematical Content** | A = [[4,1],[2,3]]. Av=λv → (A-λI)v=0 → det(A-λI)=0. det = (4-λ)(3-λ)-2 = λ²-7λ+10. λ₁=5, λ₂=2. For λ=5: (A-5I)v=0 → [-1,1;2,-2][x,y]=0 → y=x → v₁=[1,1]. For λ=2: (A-2I)v=0 → [2,1;2,1][x,y]=0 → y=-2x → v₂=[1,-2]. Verification: Av₁=[5,5]=5v₁ ✓. Av₂=[2,-4]=2v₂ ✓. |
| **Animation / Transition** | TransformMatchingTex: Av=λv → Av-λv=0 → (A-λI)v=0. Write equations step by step. FadeOut each step before next. Final verification in green. |
| **On-Screen Text** | Each step header. All equations as listed above. "✓" in green for both eigenvectors. |
| **Narration** | "Start from Av=λv. Rearrange to (A-λI)v=0. For a non-trivial solution the matrix must be singular, so det(A-λI)=0. Expanding gives λ²-7λ+10=0. Factoring: (λ-5)(λ-2)=0. Eigenvalues are 5 and 2. Substituting back finds the eigenvectors [1,1] and [1,-2]." |
| **Learning Objective** | Master the full algorithm: characteristic equation → eigenvalues → eigenvectors → verification. |
| **Color Coding** | Step headers: #38BDF8 · Eigenvalue results: #FBBF24 · Verification: #34D399 · Matrices/equations: #FFFFFF |
| **Camera Movement** | Static; natural page-turn feel via FadeOut/In between steps |

---

## Scene 5 — Interpretation — 4:10–4:40

| Field | Content |
|-------|---------|
| **Scene Number** | 5 |
| **Scene Title** | "What Did We Actually Discover?" |
| **Duration** | 4:10 – 4:40 (≈ 30 s) |
| **Visual Description** | Coordinate grid centered near origin. Two emerald eigenlines drawn for directions [1,1] and [1,-2]. v₁=[1,1] in cyan → Av₁=[5,5] in amber (×5). v₂=[1,-2] in cyan → Av₂=[2,-4] in amber (×2). Non-eigenvector [1,0] → [4,2] (coral, direction changes). Then a black canvas with the main insight quote and the Av=λv↔"stays on its own line" connection. |
| **Mathematical Content** | A=[4,1;2,3]. v₁=[1,1]→Av₁=[5,5]=5v₁. v₂=[1,-2]→Av₂=[2,-4]=2v₂. [1,0]→[4,2] (non-eigen). Insight: Av=λv ↔ vector stays on its own line. |
| **Animation / Transition** | FadeIn grid → Create eigenlines → GrowArrow v₁ → Transform v₁ → GrowArrow v₂ → Transform v₂ → GrowArrow v_non → Transform v_non → FadeOut grid → Write insight → Write Av=λv connection |
| **On-Screen Text** | "×5 along the same direction" / "×2 along the same direction" / "Direction changed — not an eigenvector". Insight quote. Av=λv ↔ "vector stays on its own line". |
| **Narration** | "The vector [1,1] was stretched to [5,5] — five times as long, same direction. [1,-2] stretched to [2,-4] — twice as long, same direction. But [1,0] rotated away entirely. The eigenvector directions are the natural backbone of this transformation." |
| **Learning Objective** | Consolidate algebra and geometry: eigenvectors = preserved directions; eigenvalues = scaling amounts. |
| **Color Coding** | Eigenlines: #34D399 · Original eigenvectors: #38BDF8 · Transformed: #FBBF24 · Non-eigenvector: #F87171 |
| **Camera Movement** | Static grid; zoom out slightly for the insight text |

---

## Scene 6 — Summary & Credits — 4:40–5:00+

| Field | Content |
|-------|---------|
| **Scene Number** | 6 |
| **Scene Title** | "The Big Picture" |
| **Duration** | 4:40 – 5:00 (summary) + ~10 s credits |
| **Visual Description** | Dark canvas. Three boxed key results appear sequentially on the left. On the right, a vertical visual chain: Matrix A → Transformation → Invariant Directions → Eigenvectors → Eigenvalues = Scaling Factors, connected by arrows. Final quote appears on empty canvas. Credits roll. |
| **Mathematical Content** | ①Av=λv  ② det(A-λI)=0  ③ (A-λI)v=0. Visual chain (conceptual, not numeric). Final quote. References list. |
| **Animation / Transition** | FadeIn takeaways with lag → FadeIn chain items with lag → GrowArrow chain connectors → FadeOut all → Write final quote → FadeIn credits |
| **On-Screen Text** | Three boxed equations + one-line descriptions. Chain labels. "Eigenvalues tell us how much. Eigenvectors tell us in which special directions." References. Music/AI credit. |
| **Narration** | "Av equals lambda v. Solve det(A-λI)=0 for eigenvalues. Solve (A-λI)v=0 for eigenvectors. Eigenvalues tell us how much. Eigenvectors tell us which direction." |
| **Learning Objective** | Provide a memorable summary to consolidate all concepts. |
| **Color Coding** | Def: #FFFFFF · Eigenvalues box: #FBBF24 · Eigenvectors box: #38BDF8 · Chain items: semantic colors · Credits: #64748B |
| **Camera Movement** | Static throughout |

---

## Color Palette Quick Reference

| Semantic Role | Hex | Manim Constant |
|---------------|-----|----------------|
| Background | `#111318` | `BG_COLOR` |
| Grid / axes | `#4A5568` / `#64748B` | `GRID_COLOR` / `AXIS_COLOR` |
| Original vector | `#38BDF8` | `VEC_ORIG_COLOR` |
| Transformed vector | `#FBBF24` | `VEC_TRANS_COLOR` |
| Eigenvector | `#38BDF8` | `EIGEN_COLOR` |
| Eigenvalue | `#FBBF24` | `EIGENVAL_COLOR` |
| Comparison vector | `#F87171` | `VEC2_COLOR` |
| Invariant eigenline | `#34D399` | `EIGENLINE_COLOR` |
| Key result / white | `#FFFFFF` | `RESULT_COLOR` |
| Matrix entries | `#E2E8F0` | `MATRIX_COLOR` |
| Accent / highlight | `#A78BFA` | `HIGHLIGHT_COLOR` |

---

## Final Quality Checklist

### Mathematical
- [x] Av = λv correctly explained  
- [x] A − λI correctly constructed  
- [x] Determinant equation (4−λ)(3−λ)−2=0 correct  
- [x] Eigenvalues λ₁=5, λ₂=2 correct  
- [x] Eigenvectors v₁=[1,1], v₂=[1,−2] correct  
- [x] Verification Av₁=5v₁ and Av₂=2v₂ shown  
- [x] Positive / negative / zero eigenvalue intuition correct  
- [x] Geometric interpretation matches algebra  

### Visual
- [x] Dark 16:9 canvas (#111318)  
- [x] Consistent semantic colors  
- [x] Coordinate grids visible and readable  
- [x] Vector transformations smooth  
- [x] Eigenlines drawn in emerald green  
- [x] No excessive visual clutter  
- [x] Equations readable at 1080p  

### Video
- [x] 1920×1080 (via `-qh` flag)  
- [x] 16:9 landscape  
- [x] MP4 output  
- [x] Target ≈ 5 minutes  
- [x] Strictly under 7 minutes  
- [x] Opening frame present  
- [x] All 6 scenes present  
- [x] Closing credits present  

### Repository
- [x] `Code/main.py`  
- [x] `Code/scenes/` (7 files)  
- [x] `Code/requirements.txt`  
- [x] `README.md`  
- [x] `Storyboard.md`  
- [x] Reproducible rendering instructions  
