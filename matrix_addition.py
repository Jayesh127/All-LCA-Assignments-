"""
Matrix Addition Program
------------------------
Creates two matrices (as 2D arrays/lists) and performs their addition.
"""


def create_matrix(rows, cols, label):
    """Take user input and create a matrix of given dimensions."""
    print(f"\nEnter elements for {label} ({rows}x{cols}):")
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            value = float(input(f"Enter element [{i}][{j}]: "))
            row.append(value)
        matrix.append(row)
    return matrix


def add_matrices(matrix_a, matrix_b, rows, cols):
    """Add two matrices of the same dimensions."""
    result = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(matrix_a[i][j] + matrix_b[i][j])
        result.append(row)
    return result


def print_matrix(matrix, label):
    """Print a matrix in readable format."""
    print(f"\n{label}:")
    for row in matrix:
        print(" ".join(f"{val:.2f}" for val in row))


def main():
    print("=== Matrix Addition Program ===")

    # Take matrix dimensions from the user
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    # Create matrix A and matrix B
    matrix_a = create_matrix(rows, cols, "Matrix A")
    matrix_b = create_matrix(rows, cols, "Matrix B")

    # Perform addition
    result = add_matrices(matrix_a, matrix_b, rows, cols)

    # Display results
    print_matrix(matrix_a, "Matrix A")
    print_matrix(matrix_b, "Matrix B")
    print_matrix(result, "Result (A + B)")


if __name__ == "__main__":
    main()
