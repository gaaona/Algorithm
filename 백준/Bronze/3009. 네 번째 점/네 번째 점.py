import sys

matrix = [list(map(int, line.split())) for line in sys.stdin.readlines()]

def find_missing_coordinate(matrix):
    x_coords = [point[0] for point in matrix]
    y_coords = [point[1] for point in matrix]
    
    missing_x = 0
    missing_y = 0
    for x in x_coords:
        missing_x ^= x
    for y in y_coords:
        missing_y ^= y
    
    return missing_x, missing_y

x, y = find_missing_coordinate(matrix)
print(f'{x} {y}')
