class SparseMatrix(object):

    def __init__(self, lines, columns, elements, name):

        self.no_of_lines = lines
        self.no_of_columns = columns
        self.no_of_elements = elements
        self.matrix_name = name

        # elements_list - the list of elements of the matrix in the form [i ,j, k] where
        #  i - the element's line
        #  j - the element's column
        #  k - the element's value, k != 0
        self.elements_list = []

        # Reads the non-zero elements of the matrix and appends them to its list
        i = 1
        while i <= self.no_of_elements:
            line = int(input("Enter the line of the element: "))
            while line <= 0 or line > self.no_of_lines:
                print("Invalid value.")
                line = int(input("Enter the line of the element: "))

            column = int(input("Enter the column of the element: "))
            while column <= 0 or column > self.no_of_columns:
                print("Invalid value.")
                column = int(input("Enter the column of the element: "))

            value = float(input("Enter the value of the element: "))
            while value == 0:
                print("Invalid value.")
                value = float(input("Enter the value of the element: "))

            self.elements_list.append([line, column, value])
            i += 1

    def __del__(self):
        print("\nMatrix {0} was deleted.\n".format(self.matrix_name))

    def find_value(self, element_line, element_column):
        # Returns the value found in the matrix at the line and column given as parameters
        for element in self.elements_list:
            if element[0] == element_line and element[1] == element_column:
                return element[2]
        return 0

    def display_matrix(self):
        # Prints the sparse matrix and its name
        print("Matrix {0}\n".format(self.matrix_name))
        for i in range(1, self.no_of_lines + 1):
            for j in range(1, self.no_of_columns + 1):
                value = self.find_value(i, j)
                print(float(value), end = " ")  # Prints the value found at line 'i' and column 'j' in the matrix
            print('\n')
        print('\n')

    def find_position(self, value):
        # Searches for a given, non-zero value in the list
        # and returns all its occurrences in the matrix (by indices)
        found = 0
        for element in self.elements_list:
            if element[2] == value:
                print("The value was found at line {0} and column {1}.\n".format(element[0], element[1]))
                found = 1
        if found == 0:
            print("Could not find the value {0} in the matrix {1}.\n".format(value, self.matrix_name))

    def add_matrices(self, second_matrix):
        # Adds the matrix with a matrix given as parameter
        result_name = self.matrix_name + " + " + second_matrix.matrix_name

        result = SparseMatrix(self.no_of_lines, self.no_of_columns, 0, result_name)

        for i in range(1, self.no_of_lines + 1):
            for j in range(1, self.no_of_columns + 1):
                x = float(self.find_value(i, j))
                y = float(second_matrix.find_value(i, j))
                # Finds the values at line 'i' and column 'j' in the matrices
                if x + y != 0:
                    # Verifies if the result of the addition is a non-zero value, adds the element to the list if true
                    add = [i, j, x + y]
                    result.elements_list.append(add)
        return result

    def subtract_matrices(self, second_matrix):
        # Subtracts the matrix with a matrix given as parameter
        result_name = self.matrix_name + " - " + second_matrix.matrix_name

        result = SparseMatrix(self.no_of_lines, self.no_of_columns, 0, result_name)

        for i in range(1, self.no_of_lines + 1):
            for j in range(1, self.no_of_columns + 1):
                x = float(self.find_value(i, j))
                y = float(second_matrix.find_value(i, j))
                # Finds the values at line 'i' and column 'j' in the matrices
                if x - y != 0:
                    # Verifies if the result of the subtraction is a non-zero value,
                    # adds the element to the list if true
                    subtract = [i, j, x - y]
                    result.elements_list.append(subtract)
        return result

    def multiply_matrices(self, second_matrix):
        # Multiplies the matrix with a matrix given as parameter
        result_name = self.matrix_name + " * " + second_matrix.matrix_name

        result = SparseMatrix(self.no_of_lines, second_matrix.no_of_columns, 0, result_name)
        for i in range(1, self.no_of_lines + 1):
            for j in range(1, second_matrix.no_of_columns + 1):
                s = 0.0
                for k in range(1, self.no_of_columns + 1):
                    # The same as the normal multiplication of matrices, with the exception that
                    # the corresponding elements to be multiplied must exist in the matrices' lists
                    # (both non-zero values).
                    for x in self.elements_list:
                        for y in second_matrix.elements_list:
                            if x[0] == i and x[1] == k and y[0] == k and y[1] == j:
                                s = s + x[2] * y[2]
                if s != 0:  # Only non-zero results will be added to the list
                    new_element = [i, j, s]
                    result.elements_list.append(new_element)
        return result

    def transposed_matrix(self):
        # Creates the transposed of the sparse matrix
        transposed_name = "Transposed " + self.matrix_name

        transposed = SparseMatrix(self.no_of_columns, self.no_of_lines, 0, transposed_name)
        for i in range(1, self.no_of_lines + 1):
            for j in range(1, self.no_of_columns + 1):
                for element in self.elements_list:
                    # Adds the element to the list with switched indices
                    new_element = [element[1], element[0], element[2]]
                    transposed.elements_list.append(new_element)
        return transposed

    def make_unit_matrix(self):
        # Transforms a matrix (supposed to be a zero matrix)
        # into an unit one by adding elements with the value "1"
        # to the main diagonal
        for i in range(1, self.no_of_lines + 1):
            self.elements_list.append([i, i, 1])
