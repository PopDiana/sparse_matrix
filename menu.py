from sparsematrix import *

lines = int(input("Enter the number of lines for the sparse matrix : "))
columns = int(input("Enter the number of columns for the sparse matrix : "))
elements = int(input("Enter the number of elements for the sparse matrix : "))
A = SparseMatrix(lines, columns, elements, "A")  # Create the first matrix named "A"

print("\n1.Display matrix")
print("2.Display dimensions of the current matrix.")
print("3.Add matrices")
print("4.Subtract matrices")
print("5.Multiply matrices")
print("6.Create unit matrix")
print("7.Create zero matrix")
print("8.Transpose the current matrix")
print("9.Search for a value in the current matrix")
print("10.Access element in the matrix by indices")
print("Press '0' to exit the menu\n")

ch = int(input("Choose : "))

while ch != 0:

    if ch == 1:
        A.display_matrix()  # Print the matrix A

    if ch == 2:
        print("The matrix {0} has {1} lines and {2} columns.\n".format(A.matrix_name, A.no_of_lines, A.no_of_columns))
        # print A's dimensions

    if ch == 3:
        print("The second matrix should have {0} lines and {1} columns\n".format(A.no_of_lines, A.no_of_columns))
        lines = int(input("Enter the number of lines for the second matrix : "))
        columns = int(input("Enter the number of columns for the second matrix : "))
        elements = int(input("Enter the number of elements for the second matrix : "))
        B = SparseMatrix(lines, columns, elements, "B")  # Create the second matrix named "B"

        print("\nFirst matrix : ")
        A.display_matrix()
        print("Second matrix : ")
        B.display_matrix()

        if B.no_of_lines != A.no_of_lines or B.no_of_columns != A.no_of_columns:
            # Dimensions are incompatible for addition
            print("Could not add the two matrices.\n")
        else:  # Add the matrices and prints the result
            C = A.add_matrices(B)
            print("Result of addition : ")
            C.display_matrix()

    if ch == 4:
        print("The second matrix should have {0} lines and {1} columns.\n".format(A.no_of_lines, A.no_of_columns))
        lines = int(input("Enter the number of lines for the second matrix : "))
        columns = int(input("Enter the number of columns for the second matrix : "))
        elements = int(input("Enter the number of elements for the second matrix : "))
        B = SparseMatrix(lines, columns, elements, "B")  # Create the second matrix named "B"

        print("\nFirst matrix : ")
        A.display_matrix()
        print("Second matrix : ")
        B.display_matrix()

        if B.no_of_lines != A.no_of_lines or B.no_of_columns != A.no_of_columns:
            # Dimensions are incompatible for subtraction
            print("Could not subtract the two matrices.\n")
        else:  # Subtract the matrices and print the result
            C = A.subtract_matrices(B)
            print("Result of subtraction : ")
            C.display_matrix()

    if ch == 5:
        print("The second matrix should have {0} lines.\n".format(A.no_of_columns))
        lines = int(input("Enter the number of lines for the second matrix : "))
        columns = int(input("Enter the number of columns for the second matrix : "))
        elements = int(input("Enter the number of elements for the second matrix: "))
        B = SparseMatrix(lines, columns, elements, "B")  # Creates the second matrix named "B"

        # Print both matrices
        print("First matrix : ")
        A.display_matrix()
        print("Second matrix : ")
        B.display_matrix()

        if B.no_of_lines != A.no_of_columns:  # Dimensions are incompatible for multiplication
            print("Could not multiply the two matrices.\n")
        else:  # MultiplY the matrices and print the result
            C = A.multiply_matrices(B)
            print("Result of multiplication : ")
            C.display_matrix()

    if ch == 6:  # Create and print an unit matrix of given dimension
        I_dimension = int(input("Enter the dimension of the unit matrix : "))
        # Firstly, a zero matrix will be created then the matrix will be transformed into an unit matrix
        # by adding elements with the value '1' to the main diagonal
        I = SparseMatrix(I_dimension, I_dimension, 0, "I" + str(I_dimension))
        I.make_unit_matrix()
        I.display_matrix()

    if ch == 7:  # Create and print a zero matrix
        O_dimension = int(input("Enter the dimension of the zero matrix : "))
        O = SparseMatrix(O_dimension, O_dimension, 0, "O" + str(O_dimension))
        O.display_matrix()

    if ch == 8:  # Create and print the transposed of the matrix A
        Tr = A.transposed_matrix()
        Tr.display_matrix()

    if ch == 9:
        # Search for a value in the matrix A and print the indices of all its occurrences
        value = float(input("Enter the value you wish to search in the current matrix : "))
        if value == 0:
            value = float(input("Please enter a non-zero value : "))
        A.find_position(value)

    if ch == 10:
        # Search for a non-zero element in the matrix A, specified by its indices
        line = int(input("Enter the line of the element you wish to search in the current matrix : "))
        column = int(input("Enter the column of the element you wish to search in the current matrix : "))

        while line > A.no_of_lines:
            print("Invalid value.")
            line = int(input("Enter the line of the element you wish to search in the current matrix : "))
        while column > A.no_of_columns:
            print("Invalid value.")
            column = int(input("Enter the column of the element you wish to search in the current matrix : "))

        value = A.find_value(line, column)
        if value == 0:
            print("Could not find a non-zero value at line {0} and column {1} in the current matrix.\n".format(line, column))
        else:
            print("The value found at line {0} and column {1} in the matrix is {2}.\n".format(line, column, value))

    print("\n1.Display matrix")
    print("2.Display dimensions of the current matrix.")
    print("3.Add matrices")
    print("4.Subtract matrices")
    print("5.Multiply matrices")
    print("6.Create unit matrix")
    print("7.Create zero matrix")
    print("8.Transpose the current matrix")
    print("9.Search for a value in the current matrix")
    print("10.Access element in the matrix by indices")
    print("Press '0' to exit the menu\n")

    ch = int(input("Choose : "))
