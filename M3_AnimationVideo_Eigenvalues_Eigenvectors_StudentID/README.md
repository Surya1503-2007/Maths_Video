# Eigenvalues & Eigenvectors — M3 Mathematical Animation

## Project Title
**Eigenvalues & Eigenvectors — M3 Mathematical Animation**

## Description
A complete 3Blue1Brown-inspired mathematical animation built with **Manim Community Edition** (Python) that teaches eigenvalues and eigenvectors through geometric intuition. The video emphasises that eigenvectors are *invariant directions* under a matrix transformation — the matrix only stretches, shrinks, or reverses them without rotating them. The algebra (characteristic equation, eigenvector solve) emerges naturally from the geometry.

---

## Features

```
✓ 1080p (1920×1080) mathematical animation
✓ Eigenvector geometric intuition via live coordinate-plane transformations
✓ Matrix transformation visualization (animated grid stretching)
✓ Characteristic equation step-by-step derivation
✓ Fully worked numerical example for A = [[4,1],[2,3]]
✓ Eigenvector verification for both eigenvalues
✓ 6-scene storyboard structure + opening title card
✓ Narration-ready source code (NARRATION: / VISUAL INTENT: / CAPTION: comments)
✓ Semantic color coding throughout
✓ Modular, reproducible, GitHub-ready codebase
```

---

## Project Structure

```
M3_AnimationVideo_Eigenvalues_Eigenvectors_StudentID/
│
├── Video.mp4                        ← final rendered video (after rendering)
│
├── Code/
│   ├── main.py                      ← entry point; FullVideo class + math checks
│   ├── scenes/
│   │   ├── __init__.py
│   │   ├── opening.py               ← Opening title card (0:00–0:10)
│   │   ├── scene1_hook.py           ← Hook / Context (0:10–0:50)
│   │   ├── scene2_concept.py        ← Concept Introduction (0:50–1:40)
│   │   ├── scene3_intuition.py      ← Visual Intuition (1:40–2:35)
│   │   ├── scene4_worked_example.py ← Worked Example (2:35–4:10)
│   │   ├── scene5_interpretation.py ← Interpretation (4:10–4:40)
│   │   └── scene6_summary.py        ← Summary & Credits (4:40–5:00+)
│   │
│   ├── assets/                      ← (empty; add custom fonts/images here)
│   └── requirements.txt
│
├── Storyboard.md                    ← scene-by-scene storyboard document
└── README.md                        ← this file
```

---

## Installation

### Prerequisites

- Python 3.9 or higher
- `ffmpeg` (required by Manim for video encoding)

**Install ffmpeg:**

| OS      | Command |
|---------|---------|
| macOS   | `brew install ffmpeg` |
| Ubuntu/Debian | `sudo apt install ffmpeg` |
| Windows | Download from https://ffmpeg.org/download.html and add to PATH |

### Python Environment Setup

```bash
# Navigate to the project root
cd M3_AnimationVideo_Eigenvalues_Eigenvectors_StudentID

# Create a virtual environment
python -m venv .venv

# Activate it
# macOS / Linux:
source .venv/bin/activate
# Windows (PowerShell):
.venv\Scripts\Activate.ps1
# Windows (CMD):
.venv\Scripts\activate.bat

# Install dependencies
pip install -r Code/requirements.txt
```

### Manim Version

This project requires **Manim Community Edition ≥ 0.18.0**.

```bash
# Verify after install:
manim --version
```

---

## Student Configuration

Open `Code/main.py` and edit the two lines near the top:

```python
STUDENT_NAME = "______________________"   # ← your full name here
STUDENT_ID   = "________________________"  # ← your student ID here
```

---

## Rendering

All render commands should be run from the `Code/` directory:

```bash
cd Code
```

### Render Individual Scenes (for preview / debugging)

```bash
manim -pqh main.py OpeningScene
manim -pqh main.py Scene1Hook
manim -pqh main.py Scene2Concept
manim -pqh main.py Scene3Intuition
manim -pqh main.py Scene4WorkedExample
manim -pqh main.py Scene5Interpretation
manim -pqh main.py Scene6Summary
```

### Render the Full Video (all scenes, single MP4)

```bash
manim -pqh main.py FullVideo
```

### Flag Reference

| Flag | Meaning |
|------|---------|
| `-p` | Preview (open the video after rendering) |
| `-q h` / `-qh` | Quality: 1080p H.264 (1920×1080) |
| `-q m` | Quality: 720p (faster, for iteration) |
| `--save_sections` | Save each section as a separate MP4 |
| `--format gif` | Render as GIF instead of MP4 |

---

## Output

Manim writes all rendered files to:

```
Code/media/videos/main/1080p60/
```

The combined full video will be named:

```
Code/media/videos/main/1080p60/FullVideo.mp4
```

Copy it to the project root as `Video.mp4` to match the submission layout:

```bash
# macOS / Linux:
cp Code/media/videos/main/1080p60/FullVideo.mp4 Video.mp4
# Windows:
copy Code\media\videos\main\1080p60\FullVideo.mp4 Video.mp4
```

---

## Mathematical Verification

Run the built-in verification script to confirm all equations are correct:

```bash
python Code/main.py
```

Expected output confirms:
- Characteristic polynomial: λ² − 7λ + 10 = 0
- Eigenvalues: λ₁ = 5, λ₂ = 2
- Eigenvectors: v₁ = [1, 1], v₂ = [1, -2]
- Av₁ = 5v₁ ✓
- Av₂ = 2v₂ ✓

---

## Color Reference

| Element | Color | Hex |
|---------|-------|-----|
| Background | Dark charcoal | `#111318` |
| Grid / axes | Muted slate | `#4A5568` |
| Original vector | Electric blue | `#38BDF8` |
| Transformed vector | Amber / gold | `#FBBF24` |
| Eigenvector | Bright cyan | `#38BDF8` |
| Eigenvalue | Amber / gold | `#FBBF24` |
| Comparison vector | Coral red | `#F87171` |
| Eigenline | Emerald green | `#34D399` |
| Key result | White | `#FFFFFF` |
| Matrix entries | Light grey | `#E2E8F0` |

---

## References

1. Gilbert Strang — *Introduction to Linear Algebra*
2. 3Blue1Brown — *Essence of Linear Algebra* (YouTube)
3. MIT OpenCourseWare — *Linear Algebra (18.06)*
4. Standard M3 Linear Algebra Course Material

---

## AI Tool Disclosure

AI-assisted development was used for code generation, debugging, mathematical visualization planning, and animation workflow assistance using Antigravity IDE / AI tools. All mathematical content was reviewed and verified before rendering.
