import pytest
from main import MedianCoffeeReport, read_csv_files

def test_median_coffee_report():
    data = [
        {'student': 'Алексей Смирнов', 'coffee_spent': '450'},
        {'student': 'Алексей Смирнов', 'coffee_spent': '500'},
        {'student': 'Алексей Смирнов', 'coffee_spent': '550'},
        {'student': 'Дарья Петрова', 'coffee_spent': '200'},
        {'student': 'Дарья Петрова', 'coffee_spent': '250'},
        {'student': 'Дарья Петрова', 'coffee_spent': '300'},
    ]

    report = MedianCoffeeReport()
    results = report.generate(data)

    # Expected: Алексей 500, Дарья 250
    expected = [
        ('Алексей Смирнов', 500.0),
        ('Дарья Петрова', 250.0),
    ]

    assert results == expected

def test_median_coffee_report_single_entry():
    data = [
        {'student': 'Алексей Смирнов', 'coffee_spent': '450'},
    ]

    report = MedianCoffeeReport()
    results = report.generate(data)

    expected = [
        ('Алексей Смирнов', 450.0),
    ]

    assert results == expected

def test_median_coffee_report_empty():
    data = []

    report = MedianCoffeeReport()
    results = report.generate(data)

    assert results == []

def test_read_csv_files(tmp_path):
    # Create temporary CSV files
    file1 = tmp_path / "test1.csv"
    file1.write_text("student,coffee_spent\nАлексей,100\nДарья,200\n", encoding='utf-8')
    file2 = tmp_path / "test2.csv"
    file2.write_text("student,coffee_spent\nАлексей,300\n", encoding='utf-8')

    data = read_csv_files([str(file1), str(file2)])
    expected = [
        {'student': 'Алексей', 'coffee_spent': '100'},
        {'student': 'Дарья', 'coffee_spent': '200'},
        {'student': 'Алексей', 'coffee_spent': '300'},
    ]
    assert data == expected