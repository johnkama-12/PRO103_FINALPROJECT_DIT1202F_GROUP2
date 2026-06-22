# PROG103 Final Project - Student Academic Portal Management System

## Project Overview
This is a GUI-based Python application created for the PROG103 Principle of Structured Programming final project. The system is an Education System / Student Academic Portal that allows students to register, log in, enter their own subjects, and view academic information such as dashboard statistics, courses, assignments, grades, calendar events, messages, and settings.

## Important Feature Added
- New students can enter their own subjects during signup.
- The subjects entered during signup are used throughout their session.
- Demo accounts still show the original default courses and data.

## SDG Alignment
This project supports SDG 4: Quality Education by helping students organize academic activities and access learning information more easily.

## Requirements
Install Python 3.10 or above, then install dependencies:

```bash
pip install -r requirements.txt
```

## How to Run
```bash
python source_code/now.py
```

## Demo Accounts
| Student | ID | Password |
|---|---|---|
| Chris Effionga | 905006475 | chris123 |
| Mohamed Tucker | 905007895 | Moh123 |
| Caro | 905006789 | Caro123 |

## Optional Email Sending
The final package does not store the Gmail App Password directly inside the source code. To enable email sending, set this environment variable before running:

Windows PowerShell:
```powershell
$env:EMAIL_APP_PASSWORD="your-new-gmail-app-password"
python source_code/now.py
```

Command Prompt:
```bat
set EMAIL_APP_PASSWORD=your-new-gmail-app-password
python source_code\now.py
```

If the variable is not set, the account still registers successfully, but email sending is skipped and the credentials are shown in a message box.

## GitHub Submission Commands
```bash
git init
git status
git add .
git commit -m "Initial commit: Student Academic Portal"
git branch -M main
git remote add origin <your-repository-url>
git push -u origin main
```

## Package Contents
- `source_code/now.py` - main Python application
- `students.json` - initial student data file
- `requirements.txt` - Python dependencies
- `docs/Full_Project_Documentation.docx` - full report
- `docs/Full_Project_Documentation.pdf` - rendered report copy
- `screenshots/` - system screenshot images
- `diagrams/` - flowchart and context diagram
- `LICENSE` - MIT License
