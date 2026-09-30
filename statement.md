# Project Statement: Student Study Planner

## The problem

Students often have to revise several subjects and topics at the same time. Without a simple way to track that work, it can be hard to see what has been covered or how much time has gone into studying.

## The proposed solution

Student Study Planner is a lightweight command-line program. It lets a student list study topics, record a completed session, rate their focus, and review a short progress summary. It runs in a terminal and uses Python's built-in data structures.

## Intended users

- Students who want a straightforward way to keep track of revision.
- People who prefer a small terminal tool to a larger web or desktop app.
- Beginners learning about Python dictionaries, lists, loops, and input validation.

## Project scope

### Included

- Add study tasks with a subject, topic, and priority.
- Assign each task a unique, increasing string ID.
- List unfinished tasks before recording a study session.
- Record session duration in minutes and focus on a scale from 1 to 5.
- Mark a task complete after its session is recorded.
- Calculate total time studied, average focus, and task completion.
- Display a 20-character progress bar in the terminal.
- Validate user input and explain when an entry needs to be corrected.
- Keep data in memory while the program is running.

### Not included

- Saving tasks or sessions to a database or file. Data is cleared when the program closes.
- Operating-system notifications.
- Accounts or support for multiple users.

## How the program is organized

Tasks are stored in a dictionary, using their IDs as keys. Each task records its subject, topic, priority, and completion status. Study sessions are stored in a list of dictionaries with the related task ID, duration, and focus rating.

The program presents a repeating menu. When a user adds a task or records a session, it checks the input before updating the in-memory data. The progress option totals the session minutes and focus ratings, counts completed tasks, and uses those counts to draw the progress bar.

## Basic validation rules

- Subject and topic cannot be blank.
- Priority must be High, Medium, or Low.
- Task IDs must refer to an unfinished task when a session is recorded.
- Session duration must be a positive whole number of minutes.
- Focus rating must be a whole number from 1 to 5.

## Possible future improvements

Later versions could save data between runs or include a study timer. Those additions are outside the current project scope.
