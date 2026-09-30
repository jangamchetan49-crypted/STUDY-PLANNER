# Student Study Planner

Student Study Planner is a small command-line app for keeping track of study topics. Add a task for each topic, record how long you studied it, and give the session a focus rating. The progress screen adds up your study time and shows how many tasks you have finished.

## What it can do

- Create tasks with a subject, topic, and High, Medium, or Low priority.
- Give each task a simple, automatically assigned ID.
- Record a study session in whole minutes and rate focus from 1 to 5.
- Mark a task complete after a session has been recorded for it.
- Show total study time, average focus, and task completion in a 20-character progress bar.
- Check input before saving it so blank fields and invalid values are not accepted.

## Requirements

You need Python 3. No additional packages are required.

To check that Python is available, run:

```bash
python --version
```

## Run the app

Open a terminal in this folder and run:

```bash
python main.py
```

You can also run `python study_planner.py`; it starts the same app for compatibility with the original filename. Tasks and sessions stay in memory and are cleared when you close the program.

## Project files

- `main.py` contains the application.
- `study_planner.py` is a small launcher for the original filename.
- `statement.md` describes the project goals and requirements.
- `README.md` explains how to use the project.

The code uses dictionaries, lists, loops, and built-in input checks to keep the program easy to follow. It does not use external libraries, a database, or file-based storage.

## Current limits

Each task can be completed with one recorded session. The app does not save information between runs, send notifications, or manage multiple users.
