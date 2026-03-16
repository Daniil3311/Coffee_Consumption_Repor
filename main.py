import argparse
import csv
import sys
from statistics import median
from tabulate import tabulate

class Report:
    def __init__(self, name):
        self.name = name

    def generate(self, data):
        raise NotImplementedError

class MedianCoffeeReport(Report):
    def __init__(self):
        super().__init__("median-coffee")

    def generate(self, data):
        student_spends = {}
        for row in data:
            student = row['student']
            spend = float(row['coffee_spent'])
            if student not in student_spends:
                student_spends[student] = []
            student_spends[student].append(spend)

        results = []
        for student, spends in student_spends.items():
            med = median(spends)
            results.append((student, med))

        results.sort(key=lambda x: x[1], reverse=True)
        return results

def read_csv_files(file_paths):
    data = []
    for file_path in file_paths:
        with open(file_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            data.extend(list(reader))
    return data

def main():
    parser = argparse.ArgumentParser(description="Generate coffee consumption reports.")
    parser.add_argument('--files', nargs='+', required=True, help='Paths to CSV files')
    parser.add_argument('--report', required=True, help='Report type')

    args = parser.parse_args()

    reports = {
        'median-coffee': MedianCoffeeReport(),
    }

    if args.report not in reports:
        print(f"Unknown report type: {args.report}", file=sys.stderr)
        sys.exit(1)

    data = read_csv_files(args.files)
    report = reports[args.report]
    results = report.generate(data)

    headers = ['Student', 'Median Coffee Spent']
    print(tabulate(results, headers=headers, tablefmt='grid'))

if __name__ == '__main__':
    main()