import numpy as np

def load_data(file_name):
    return np.genfromtxt(file_name, delimiter=" ", dtype=np.int)

def adjacency_matrix(data, dim):
    rows, cols = data.T
    m = np.zeros((dim + 1, dim + 1))
    m[rows, cols] = 1
    m[cols, rows] = 1
    return m

def max_index(data_sets):
    return max([np.max(data.flatten()) for data in data_sets])

class Board:
    def __init__(self, taxi, bus, metro, boat):
        self.taxi = taxi
        self.bus = bus
        self.metro = metro
        self.boat = boat

folder = "board/"
files = ["taxi.txt", "bus.txt", "metro.txt", "boat.txt"]

data = [load_data(folder + file) for file in files] * 2
max_dim = max_index(data)
matrices = [adjacency_matrix(d, max_dim) for d in data]

board = Board(*matrices)
print(board)
