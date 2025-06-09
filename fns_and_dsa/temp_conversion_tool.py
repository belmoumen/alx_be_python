FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
	fahrenheit = float(fahrenheit)
	return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
def convert_to_fahrenheit(celsius):
	celsius = float(celsius)
	return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def is_float(value):
	try:
		float(value)
		return True
	except ValueError:
		return False
while True:
	user_temp = user_temp = input("Enter the temperature to convert: ")
	if is_float(user_temp):
		temperature = float(user_temp)
		break
	else:
		print("Invalid temperature. Please enter a numeric value")

user_unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

match user_unit:
	case "C":
		converted = convert_to_fahrenheit(user_temp)
		print(f"{user_temp}°C is {converted}°F")
	case "F":
		converted = convert_to_celsius(user_temp)
		print(f"{user_temp}°F is {converted}°C")
	case _:
		print("Invalid unit. Please enter C or F.")

