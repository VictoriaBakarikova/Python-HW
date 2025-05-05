def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    new_matrix = [[0] * rows for _ in range(cols)]

    for x in range(rows):
        for y in range(cols):
            new_matrix[y][x] = matrix[x][y]
    return new_matrix


input_matrix = []

while True:
    input_row = input(
        "Input numbers for matrix, input empty string for end of matrix: "
    )
    if input_row == "":
        break
    input_matrix.append([int(number) for number in input_row.split()])


for row in transpose_matrix(input_matrix):
    print(row)
