import csv


if __name__ == '__main__':
    path, x, y = input().split()
    with open(path, newline="") as csv_file:
        filedata = list(csv.reader(csv_file, delimiter=",", quotechar='|'))
    print(filedata[int(x)][int(y)])
