"""A small command-line planner for tracking study tasks and sessions."""

tasks = {}
sessions = []
next_task_id = 1

print("Student Study Planner")
print("Add your study topics, record sessions, and review your progress.")

running = True
while running:
    print("\nMain menu")
    print("1. Add a study task")
    print("2. Record a study session")
    print("3. View progress")
    print("4. Exit")

    choice = input("Choose an option (1-4): ").strip()

    if choice == "1":
        subject = input("Subject: ").strip()
        topic = input("Topic or chapter: ").strip()
        priority = input("Priority (High, Medium, or Low): ").strip().capitalize()

        if not subject or not topic:
            print("Please enter both a subject and a topic.")
        elif priority not in ("High", "Medium", "Low"):
            print("Priority must be High, Medium, or Low.")
        else:
            task_id = str(next_task_id)
            tasks[task_id] = {
                "subject": subject,
                "topic": topic,
                "priority": priority,
                "is_completed": False,
            }
            next_task_id += 1
            print(f"Added task {task_id}: {subject} — {topic} ({priority} priority).")

    elif choice == "2":
        open_task_ids = []
        for task_id, task in tasks.items():
            if not task["is_completed"]:
                open_task_ids.append(task_id)

        if not open_task_ids:
            print("There are no unfinished tasks. Add a task before recording a session.")
            continue

        print("\nUnfinished study tasks")
        for task_id in open_task_ids:
            task = tasks[task_id]
            print(
                f"[{task_id}] {task['subject']} — {task['topic']} "
                f"(Priority: {task['priority']})"
            )

        task_id = input("Enter the task ID you studied: ").strip()
        if task_id not in open_task_ids:
            print("That ID is not an unfinished task. Please choose one from the list.")
            continue

        minutes_text = input("How many minutes did you study? ").strip()
        focus_text = input("How focused were you (1-5)? ").strip()

        if not minutes_text.isdigit() or not focus_text.isdigit():
            print("Enter whole numbers for both minutes and focus rating.")
            continue

        minutes = int(minutes_text)
        focus = int(focus_text)
        if minutes <= 0:
            print("Study time must be greater than zero minutes.")
        elif focus < 1 or focus > 5:
            print("Focus rating must be between 1 and 5.")
        else:
            sessions.append({"task_id": task_id, "minutes": minutes, "focus": focus})
            tasks[task_id]["is_completed"] = True
            print(f"Recorded {minutes} minutes for task {task_id}. Nice work!")

    elif choice == "3":
        total_minutes = 0
        total_focus = 0
        for session in sessions:
            total_minutes += session["minutes"]
            total_focus += session["focus"]

        total_tasks = len(tasks)
        completed_tasks = 0
        for task in tasks.values():
            if task["is_completed"]:
                completed_tasks += 1

        if sessions:
            average_focus = total_focus / len(sessions)
        else:
            average_focus = 0

        if total_tasks:
            completion_percent = completed_tasks / total_tasks * 100
        else:
            completion_percent = 0

        bar_width = 20
        filled_blocks = round(completion_percent / 100 * bar_width)
        progress_bar = "#" * filled_blocks + "-" * (bar_width - filled_blocks)
        hours, minutes = divmod(total_minutes, 60)

        print("\nStudy progress")
        print("=" * 34)
        print(f"Time studied:       {hours} hr {minutes} min")
        if sessions:
            print(f"Average focus:      {average_focus:.1f} / 5")
        else:
            print("Average focus:      No sessions recorded")
        print(f"Tasks completed:    {completed_tasks} / {total_tasks}")
        print(f"Completion:         [{progress_bar}] {completion_percent:.1f}%")
        print("=" * 34)

    elif choice == "4":
        print("Good luck with your studies. See you next time!")
        running = False

    else:
        print("Please choose a number from 1 to 4.")
