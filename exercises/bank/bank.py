def value(greeting):
	greeting = greeting.lstrip().lower()
	if greeting.startswith("hello"):
		return 0
	if greeting.startswith("h"):
		return 20
	return 100


def main():
	greeting = input("Greeting: ")
	print(f"${value(greeting)}")


if __name__ == "__main__":
	main()
