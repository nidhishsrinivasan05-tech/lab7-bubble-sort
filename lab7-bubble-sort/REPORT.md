# Project Report: AI-Assisted Development

## 1. Initial Approach
This project started from the `lab1-hello-world` template and was adapted into a new project called `lab7-bubble-sort`. The goal was to create a beginner-friendly Bubble Sort visualization in Python while keeping the repository structure consistent with the course workflow.

### Assumptions
- The project should contain a `main.py` file.
- The repository should reuse the `.github` setup, `.gitignore`, and documentation structure from the original template.
- The final application should clearly demonstrate Bubble Sort step by step.

## 2. Prompting & AI Interaction

### Successes
Clear prompts worked well when they specified:
- the project name
- the expected repository structure
- the need for a Python visualization
- the requirement to keep the code readable for a student lab

### Failures
Possible AI failures included:
- suggesting code that was too advanced for a beginner lab
- creating a sorting script without any real visualization
- ignoring the project template and documentation files

### Analysis
These failures usually happen when the prompt is too vague or when the AI optimizes for a “cool” solution instead of a course-appropriate one. The solution was to be more explicit about the lab context, required files, and level of complexity.

## 3. Key Learnings

### Technical Skills
- Implementing Bubble Sort
- Using Tkinter for simple algorithm visualization
- Structuring a Python project for submission
- Adding fallback behavior for different runtime environments

### AI Workflow
In future projects, the best workflow is:
1. define the required repo structure first
2. reuse the template files
3. ask for one feature at a time
4. run and test before finalizing
