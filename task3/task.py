import csv
from math import log2

def get_file_data(path):
    with open(path, newline="") as csvfile:
        filedata = [[int(s) for s in line] for line in csv.reader(csvfile, delimiter=",", quotechar="|")]
    return filedata

def get_entropy(data):
    n = len(data)
    m = len(data[0])
    entr = 0
    for i in range(n):
        for j in range(m):
            if data[i][j]:
                entr -= data[i][j] * log2(data[i][j] / (n - 1)) / (n - 1)
    return entr

print(get_entropy(get_file_data("task3.csv")))

