import csv
import sys

def read_adjacency_matrix(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        adjacency_matrix = list(reader)
        
        for node, neighbors in enumerate(adjacency_matrix):
            node_neighbors = [str(index+1) for index, adjacent in enumerate(neighbors) if adjacent == '1']
            node_neighbors_str = ', '.join(node_neighbors)
            print("Node {}: {}".format(node+1, node_neighbors_str))

if __name__ == "__main__":
    file_path = sys.argv[1]
    read_adjacency_matrix(file_path)