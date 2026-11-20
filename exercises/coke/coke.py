amount_due = 50

while amount_due > 0:
	try:
		coin = int(input("Insert Coin: "))
	except ValueError:
		coin = 0
	except EOFError:
		print("Input ended before payment was completed.")
		break

	if coin in (25, 10, 5):
		amount_due -= coin

	print(f"Amount Due: {max(amount_due, 0)}")

if amount_due <= 0:
	print(f"Change Owed: {-amount_due}")
