Task = input("Enter your task: ")
Priority = input("Priority (high/medium/low): ").lower()
Time_bound = input("Is it time-bound? (yes or no): ").lower()

match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a HIGH priority task."
    case "medium":
        reminder = f"Reminder: '{task}' is a MEDIUM priority task."
    case "low":
        reminder = f"Reminder: '{task}' is a LOW priority task."
    case _:
        reminder = f"Reminder: '{task}' has an UNKNOWN priority level."

if time_bound == "yes":
    reminder += " This task requires immediate attention today!"

print(reminder)
