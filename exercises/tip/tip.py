def dollars_to_float(dollars):
	return float(dollars.replace("$", ""))


def percent_to_float(percent):
	return float(percent.replace("%", "")) / 100

def main():
	while True:
		try:
			meal_cost = dollars_to_float(input("How much was the meal? "))
			tip_percent = percent_to_float(input("What percentage would you like to tip? "))
		except ValueError:
			print("Please enter a valid meal cost and tip percentage.")
			continue
		except EOFError:
			print()
			return

		tip = meal_cost * tip_percent
		print(f"${tip:.2f}")
		return


if __name__ == "__main__":
	main()
