task = input("Enter your task: ").lower()
priority = input("Priority (high/medium/low): ").lower()
time = input("Is it time-bound? (yes/no): ").lower()

match priority:
	case "high":
		if time == "yes":
			print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
		else:
			print(f"Reminder: '{task}' is a high priority task, Consider completing it when you have free time.")
	case "medium":
		if time == "yes":
			print(f"Reminder: '{task}' is a medium priority task that requires immediate attention today!")
		else:
			print(f"Reminder: '{task}' is a medium priority task, Consider completing it when you have free time.")
	case "low":
		if time == "yes":
			print(f"Reminder: '{task}' is a low priority task that requires immediate attention today!")
		else:
			print(f"Reminder: '{task}' is a low priority task, Consider completing it when you have free time.")
	case _:
		print("You have to choose between high, medium, or low.")
