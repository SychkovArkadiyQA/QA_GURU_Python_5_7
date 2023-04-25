import csv
import os
import csv

def test_cvs():
# TODO оформить в тест, добавить ассерты и использовать универсальный путь

PROJECT_ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(PROJECT_ROOT_PATH, 'resources', 'eggs.csv')

with open(csv_path, 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(['Anna', 'Pavel', 'Peter'])
    csvwriter.writerow(['Alex', 'Serj', 'Yana'])

with open(csv_path) as csvfile:
    csvreader = csv.reader(csvfile)
    name = []
    for row in csvreader:
        name.append(row)
        print(row)
    assert name[0] == ['Anna', 'Pavel', 'Peter']
    assert name[1] == ['Alex', 'Serj', 'Yana']


