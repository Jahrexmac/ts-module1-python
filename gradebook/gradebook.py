import csv
import math
import statistics
import sys
from pathlib import Path


def letter(score):
	if score >= 90:
		return "A"
	if score >= 80:
		return "B"
	if score >= 70:
		return "C"
	if score >= 60:
		return "D"
	return "F"


def load_students(csv_path):
	students = []
	try:
		with csv_path.open(newline="", encoding="utf-8-sig") as file:
			reader = csv.DictReader(file)
			required_columns = {"name", "course", "score"}
			missing_columns = required_columns - set(reader.fieldnames or [])
			if missing_columns:
				sys.exit(
					"CSV is missing required columns: "
					+ ", ".join(sorted(missing_columns))
				)

			for row_number, row in enumerate(reader, start=2):
				score_text = (row.get("score") or "").strip()
				try:
					score = float(score_text)
					if not math.isfinite(score):
						raise ValueError
				except (TypeError, ValueError):
					print(
						f"Warning: skipping row {row_number}: "
						f"{score_text!r} is not a valid score.",
						file=sys.stderr,
					)
					continue

				students.append(
					{
						"name": (row.get("name") or "").strip(),
						"course": (row.get("course") or "").strip(),
						"score": score,
					}
				)
	except (csv.Error, OSError, UnicodeError) as error:
		sys.exit(f"Could not read {csv_path}: {error}")

	return students


def summarize(students):
	scores = [student["score"] for student in students]
	if not scores:
		return {
			"count": 0,
			"mean": None,
			"median": None,
			"highest": None,
			"lowest": None,
		}

	return {
		"count": len(students),
		"mean": statistics.mean(scores),
		"median": statistics.median(scores),
		"highest": max(students, key=lambda student: student["score"]),
		"lowest": min(students, key=lambda student: student["score"]),
	}


def format_summary(summary):
	if summary["count"] == 0:
		return [
			"Class count: 0",
			"Mean score: N/A",
			"Median score: N/A",
			"Highest: N/A",
			"Lowest: N/A",
		]

	return [
		f"Class count: {summary['count']}",
		f"Mean score: {summary['mean']:.2f}",
		f"Median score: {summary['median']:.2f}",
		f"Highest: {summary['highest']['name']} "
		f"({summary['highest']['score']:g})",
		f"Lowest: {summary['lowest']['name']} "
		f"({summary['lowest']['score']:g})",
	]


def write_report(students, summary_lines, report_path):
	sorted_students = sorted(
		students,
		key=lambda student: student["score"],
		reverse=True,
	)
	report_lines = summary_lines + ["", "Students (highest to lowest):"]
	report_lines.extend(
		f"{student['name']} {student['score']:g} "
		f"{letter(student['score'])}"
		for student in sorted_students
	)

	try:
		report_path.write_text("\n".join(report_lines) + "\n", encoding="utf-8")
	except OSError as error:
		sys.exit(f"Could not write {report_path}: {error}")


def main():
	if len(sys.argv) < 2:
		sys.exit("Too few command-line arguments. Usage: python gradebook.py <file.csv>")
	if len(sys.argv) > 2:
		sys.exit("Too many command-line arguments. Provide one CSV filename.")

	csv_path = Path(sys.argv[1])
	if csv_path.suffix.lower() != ".csv":
		sys.exit("Input file must have a .csv extension.")
	if not csv_path.is_file():
		sys.exit(f"File does not exist: {csv_path}")

	students = load_students(csv_path)
	summary_lines = format_summary(summarize(students))
	report_path = Path(__file__).with_name("report.txt")
	write_report(students, summary_lines, report_path)

	print("\n".join(summary_lines))
	print(f"Report written to {report_path}")


if __name__ == "__main__":
	main()
