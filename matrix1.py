import sys
import numpy as np


def get_matrix(rows, cols, matrix_name="Matrix"):
    print(f"Enter elements for {matrix_name} ({rows}x{cols}):")
    matrix = []
    for i in range(rows):
        while True:
            try:
                row = input(f"Row {i + 1}: ").strip().split()
                row = [complex(x.replace('i', 'j')) for x in row]
                if len(row) != cols:
                    raise ValueError("Incorrect number of elements.")
                matrix.append(row)
                break
            except ValueError as e:
                print(f"Error: {e} Try again.")
    return np.array(matrix)

def print_matrix(matrix):
    rows, cols = matrix.shape
    for i in range(rows):
        print(" ".join(f"{matrix[i,j]:8.2f}" if matrix[i,j].imag == 0 else f"{matrix[i,j]:8.2f}" for j in range(cols)))

def main():
    current_matrix = None

    while True:
        print("\nMatrix Calculator")
        print("1. Enter new matrix")
        print("2. Add another matrix")
        print("3. Subtract another matrix")
        print("4. Multiply by another matrix")
        print("5. Multiply by a number")
        print("6. Transpose matrix")
        print("7. Determinant of matrix")
        print("8. Inverse of matrix")
        print("9. Rank of matrix")
        print("10. Show current matrix")
        print("11. Exit")

        choice = input("Choose an option (1-11): ")

        if choice == "1":
            rows = get_positive_int("Enter number of rows: ")
            cols = get_positive_int("Enter number of columns: ")
            current_matrix = get_matrix(rows, cols)

        elif choice == "2":
            if current_matrix is None:
                print("No matrix loaded. Enter a matrix first.")
                continue
            rows, cols = current_matrix.shape
            m2 = get_matrix(rows, cols, "Matrix to add")
            current_matrix = current_matrix + m2
            print("Result of addition:")
            print_matrix(current_matrix)

        elif choice == "3":
            if current_matrix is None:
                print("No matrix loaded. Enter a matrix first.")
                continue
            rows, cols = current_matrix.shape
            m2 = get_matrix(rows, cols, "Matrix to subtract")
            current_matrix = current_matrix - m2
            print("Result of subtraction:")
            print_matrix(current_matrix)

        elif choice == "4":
            if current_matrix is None:
                print("No matrix loaded. Enter a matrix first.")
                continue
            cols1 = current_matrix.shape[1]
            rows2 = get_positive_int("Enter number of rows for Matrix 2: ")
            cols2 = get_positive_int("Enter number of columns for Matrix 2: ")
            if cols1 != rows2:
                print("Error: Number of columns of Matrix 1 must equal number of rows of Matrix 2.")
                continue
            m2 = get_matrix(rows2, cols2, "Matrix to multiply")
            current_matrix = np.dot(current_matrix, m2)
            print("Result of multiplication:")
            print_matrix(current_matrix)

        elif choice == "5":
            if current_matrix is None:
                print("No matrix loaded. Enter a matrix first.")
                continue
            try:
                num = complex(input("Enter number to multiply: ").replace('i', 'j'))
                current_matrix = current_matrix * num
                print("Result of scalar multiplication:")
                print_matrix(current_matrix)
            except ValueError:
                print("Invalid number.")

        elif choice == "6":
            if current_matrix is None:
                print("No matrix loaded. Enter a matrix first.")
                continue
            current_matrix = current_matrix.T
            print("Transposed matrix:")
            print_matrix(current_matrix)

        elif choice == "7":
            if current_matrix is None:
                print("No matrix loaded. Enter a matrix first.")
                continue
            if current_matrix.shape[0] != current_matrix.shape[1]:
                print("Determinant is only defined for square matrices.")
                continue
            det = np.linalg.det(current_matrix)
            print(f"Determinant: {det:.2f}")

        elif choice == "8":
            if current_matrix is None:
                print("No matrix loaded. Enter a matrix first.")
                continue
            if current_matrix.shape[0] != current_matrix.shape[1]:
                print("Inverse is only defined for square matrices.")
                continue
            try:
                inv = np.linalg.inv(current_matrix)
                current_matrix = inv
                print("Inverse matrix:")
                print_matrix(current_matrix)
            except np.linalg.LinAlgError:
                print("Matrix is singular and cannot be inverted.")

        elif choice == "9":
            if current_matrix is None:
                print("No matrix loaded. Enter a matrix first.")
                continue
            rank = np.linalg.matrix_rank(current_matrix)
            print(f"Rank of the matrix: {rank}")

        elif choice == "10":
            if current_matrix is None:
                print("No matrix loaded.")
            else:
                print("Current matrix:")
                print_matrix(current_matrix)

        elif choice == "11":
            print("Goodbye!")
            sys.exit()

        else:
            print("Invalid choice. Please select 1-11.")

def get_positive_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Number must be positive.")
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

if __name__ == "__main__":
    main()

