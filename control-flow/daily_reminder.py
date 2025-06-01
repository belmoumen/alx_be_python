task = str(input("Enter your task: "))
priority = str(input("Priority (high/medium/low): "))
time = str(input("Is it time-bound? (yes/no): "))

match time.lower():
	case "yes":
		if priority.lower() == "high":
			print(f"Reminder: \'{task}\' is a high priority task that requires immediate attention today ")
		elif priority.lower() == "medium":
			print(f"Reminder: \'{task}\' is a medium priority task that requires immediate attention today")
		elif priority.lower() == "low":
			print(f"Reminder: \'{task}\' is a low priority task that requires immediate attention today")
		else:
			print("You have to chose between high,medium or low")
	case "no":
		if priority.lower() == "high":
			print(f"Reminder: \'{task}\' is a high priority task. Consider completing it when you have free time.")
		elif priority.lower() == "medium":
			print(f"Reminder: \'{task}\' is a medium priority task. Condider completing it when you have free time")
		elif priority.lower() == "low":
			print(f"Reminder: \'{task}\' is a low priority task. Consider completing it when you have free time")
		else:
			print("you have to chose between high, medium or low")
	case _:
		if priority.lower() == "high":
			print("invalid response, it should be 'yes or no'")
		elif priority.lower() == "medium":
			print("invalid response, it should be 'yes or no'")
		elif priority.lower() == "low":
			print("invalid reponse, it should be 'yes or no'")
