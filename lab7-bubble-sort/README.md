# Bubble Sort Visualization

A Python project that visualizes the **Bubble Sort** algorithm.  
This repository follows the same project structure as the earlier `lab1-hello-world` template, while adapting it for a new sorting and visualization lab.

## Project Goal

Create a new project named **`lab7-bubble-sort`** and build a working Bubble Sort visualization in `main.py`.

This setup follows the instructions shown in class:

1. Pull the latest content from `lab1-hello-world`
2. Create a new `lab7-bubble-sort` project
3. Copy the `.github` folder into the new project
4. Copy `.gitignore`
5. Copy `REPORT.md`
6. Open the new folder in VS Code
7. Create `main.py`
8. Use Copilot with the project instructions and journal logger agent

## Features

- Random dataset generation
- Step-by-step Bubble Sort visualization
- Graphical interface using **Tkinter**
- Adjustable number of bars
- Adjustable animation speed
- Shuffle / regenerate data buttons
- Console fallback for environments without GUI support
- Matplotlib animation mode (`--matplotlib`)
- Self-test mode to verify sorting logic

## Files

- `main.py` - Main Python application
- `README.md` - Project overview and instructions
- `REPORT.md` - Reflection and project report
- `JOURNAL.md` - Development journal
- `.github/copilot-instructions.md` - AI / Copilot project instructions
- `.github/agents/journal-logger.agent.md` - Journal logging rules

## How to Run

### Normal GUI mode

```bash
python main.py
```

### Console mode

```bash
python main.py --console
```

### Matplotlib mode

```bash
python main.py --matplotlib
```

### Self-test mode

```bash
python main.py --test
```

## How the Visualization Works

Bubble Sort repeatedly compares adjacent values and swaps them when they are in the wrong order.  
The program shows this process visually by highlighting the bars currently being compared.

## Notes

- Tkinter is included with most standard Python installations.
- Install Matplotlib for animation mode:

```bash
pip install matplotlib
```

- If the graphical mode cannot start, the program automatically switches to console mode.
- This project is intentionally beginner-friendly and keeps the code readable.

## Students Comments - Please add your name and a comment here

- Nidhish Srinivasan Krishnassamy: Built a Bubble Sort visualizer project using Python and AI-assisted development tools.
