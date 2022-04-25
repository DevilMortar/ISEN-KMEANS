import csv
import drawLib


def loadCSV(file):
    r = []
    with open('file/' + file, newline='') as f:
        content = csv.reader(f, delimiter=',')
        for row in content:
            r.append(row)
    return r



