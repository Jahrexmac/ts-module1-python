try:
	text = input()
	print(text.lower())
except EOFError:
	print("No input received.")
