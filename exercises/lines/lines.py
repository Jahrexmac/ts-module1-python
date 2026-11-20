import sys


def main():
	if len(sys.argv) < 2:
		sys.exit("Too few command-line arguments")
	if len(sys.argv) > 2:
		sys.exit("Too many command-line arguments")

	filename = sys.argv[1]
	if not filename.endswith(".py"):
		sys.exit("Not a Python file")

	try:
		with open(filename, encoding="utf-8") as source:
			line_count = sum(
				1
				for line in source
				if line.strip() and not line.lstrip().startswith("#")
			)
	except FileNotFoundError:
		sys.exit("File does not exist")

	print(line_count)


if __name__ == "__main__":
	main()
