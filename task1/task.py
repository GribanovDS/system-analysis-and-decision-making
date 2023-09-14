import csv
import sys

def read_csv_cell(file_path, row_index, column_index):
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        data = list(reader)

        if row_index <= len(data) and column_index <= len(data[row_index-1]):
            cell_value = data[row_index-1][column_index-1]
            return cell_value
        else:
            return None

if __name__ == "__main__":
    file_path = sys.argv[1]
    row_index = int(sys.argv[2])
    column_index = int(sys.argv[3])

    cell_value = read_csv_cell(file_path, row_index, column_index)
    if cell_value is not None:
        print("The value in cell ({}, {}) is: {}".format(row_index, column_index, cell_value))
    else:
        print("Invalid row or column index.")