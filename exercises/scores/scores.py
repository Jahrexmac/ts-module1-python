import csv
from pathlib import Path
from statistics import mean, median


def main():
	scores_path = Path(__file__).with_name("scores.csv")
	with scores_path.open(newline="", encoding="utf-8") as file:
		rows = list(csv.DictReader(file))

	if not rows:
		raise SystemExit("scores.csv has no scores")

	scores = [int(row["score"]) for row in rows]
	top_student = max(rows, key=lambda row: int(row["score"]))
	bottom_student = min(rows, key=lambda row: int(row["score"]))

	print(f"Mean: {mean(scores)}")
	print(f"Median: {median(scores)}")
	print(f"Top student: {top_student['name']} ({top_student['score']})")
	print(f"Bottom student: {bottom_student['name']} ({bottom_student['score']})")


if __name__ == "__main__":
	main()
