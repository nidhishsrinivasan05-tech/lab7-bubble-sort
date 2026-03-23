# This Journal gets updated automatically by the Journal Logger Agent

## 2026-03-23 00:00
- Prompt Summary: Create the second project based on the lab1 template, OneDrive material, and classroom photo.
- Changes Made:
  - Created a new `lab7-bubble-sort` project structure.
  - Reused the `.github` instructions and journaling agent from `lab1-hello-world`.
  - Added a new `main.py` implementing Bubble Sort visualization.
  - Wrote a project-specific `README.md`.
  - Updated `REPORT.md` for the new project.
- Why:
  - The classroom photo shows the required setup for a new Bubble Sort project.
  - The original template indicates that `.github`, `.gitignore`, and report/journal files should be reused across new projects.
### **New Interaction**
- **Agent Version**: 2.2
- **Date**: 23-03-2026 16:17
- **User**: nidhish-srinivasan.krishnassamy@epita.fr
- **Prompt**: add matplotlib to this
- **CoPilot Mode**: Edit
- **CoPilot Model**: GPT-5.3-Codex
- **Socratic Mode**: ON
- **Changes Made**: Added Matplotlib animation mode in main.py, added requirements.txt with matplotlib dependency, and updated README with run/install instructions.
- **Context and Reasons for Changes**: The user requested Matplotlib support for this bubble sort project, so a dedicated --matplotlib runtime path was added while preserving Tkinter and console modes.
