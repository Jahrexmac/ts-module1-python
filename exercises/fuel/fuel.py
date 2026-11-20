def convert(fraction):
	numerator, denominator = fraction.split("/")
	return round(int(numerator) / int(denominator) * 100)


def gauge(percentage):
	if percentage <= 1:
		return "E"
	if percentage >= 99:
		return "F"
	return f"{percentage}%"


def main():
	while True:
		try:
			percentage = convert(input("Fraction: "))
			break
		except (ValueError, ZeroDivisionError):
			print("Enter a valid fraction, such as 3/4.")
		except EOFError:
			print("No fraction entered.")
			return

	print(gauge(percentage))


if __name__ == "__main__":
	main()
