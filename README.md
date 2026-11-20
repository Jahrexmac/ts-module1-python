# ts-module1-python

I'm Anthony Rorobi, a Python learner practicing command-line programs, input handling, CSV files, and basic statistics.

## Programs

- `bank.py` assigns a dollar amount based on a greeting.
- `coke.py` simulates a 50-cent drink machine and accepts 25-, 10-, and 5-cent coins.
- `fuel.py` converts a fraction to a fuel percentage and displays `E`, `F`, or the percentage.
- `indoor.py` prints entered text in lowercase.
- `lines.py` counts nonblank, non-comment lines in a Python file.
- `scores.py` reads `scores.csv` and prints the mean, median, highest scorer, and lowest scorer.
- `tip.py` calculates a tip from a meal cost and tip percentage.
- `gradebook.py` reads student scores from a CSV, prints class statistics, assigns letter grades, and writes a sorted `report.txt` beside the script.

## Running the Programs

Run these commands from the repository root with Python 3 installed. The interactive programs prompt for their input:

```powershell
python exercises/bank/bank.py
python exercises/coke/coke.py
python exercises/fuel/fuel.py
python exercises/indoor/indoor.py
python exercises/tip/tip.py
```

Pass the Python file to count as a command-line argument:

```powershell
python exercises/lines/lines.py exercises/indoor/indoor.py
```

The scores program reads `exercises/scores/scores.csv` from beside its script:

```powershell
python exercises/scores/scores.py
```

Pass a CSV filename to the gradebook. It writes `gradebook/report.txt`:

```powershell
python gradebook/gradebook.py gradebook/students.csv
```