import csv

def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)
    # print(header)
    data = []
    data = [{key: value for key, value in zip(header, row)} for row in reader]
    return data