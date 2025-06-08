from datetime import datetime, timedelta

def display_current_datetime():
	# the current date and time
	current_date = datetime.now()
	#convert to the format yyyy-mm-dd hh:mm:ss
	formatted_now = current_date.strftime("%Y-%m-%d %H:%M:%S")
	print("Current Date and Time: ", formatted_now)
	return current_date
def calculate_future_date(start_date):
	user_input = int(input("Enter the number of days to add to the current date: "))
	future_date = start_date + timedelta(days=user_input)
	print("Future date: ", future_date.strftime("%Y-%m-%d"))
if __name__ == "__main__":
	current_date = display_current_datetime()
	calculate_future_date(current_date)


