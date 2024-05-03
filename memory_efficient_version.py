





GAP_COST = 30
ALFA_DICTIONARY = {"AA": 0, "AC": 110, "AG": 48, "AT": 94,
                   "CA": 110, "CC": 0, "CG": 118, "CT": 48,
                   "GA": 48, "GC": 118, "GG": 0, "GT": 110,
                   "TA": 94, "TC": 48, "TG": 110, "TT": 0}


# This function gets a string and a list of integers and returns the corresponding DNA sequence
def sequence_generator(input_base_string, input_list_of_integers):
    current_string = input_base_string
    i = 0
    while i < len(input_list_of_integers):
        current_index = input_list_of_integers[i]
        temp_char_list = []
        for char in current_string:
            temp_char_list.append(char)
        temp_string = ""
        j = 0
        while j <= current_index:
            temp_string += temp_char_list[j]
            j += 1
        temp_string += current_string
        j = current_index + 1
        while j < len(temp_char_list):
            temp_string += temp_char_list[j]
            j += 1
        current_string = temp_string
        i += 1
    return current_string


# This function reads the input text file and returns two sequences
def input_file_reader(input_file_name):
    input_file = open(input_file_name, "rt")
    lines = []
    while True:
        line = input_file.readline()
        if line == "":
            break
        lines.append(line.rstrip("\n"))

    input_file.close()
    first_seq_numbers_list = []
    second_seq_numbers_list = []
    first_seq = lines[0]
    second_seq = ""
    i = 1
    while i < len(lines):
        if lines[i].isnumeric():
            first_seq_numbers_list.append(int(lines[i]))
        else:
            second_seq = lines[i]
            break
        i += 1

    i += 1
    while i < len(lines):
        second_seq_numbers_list.append(int(lines[i]))
        i += 1

    first_seq = sequence_generator(first_seq, first_seq_numbers_list)
    second_seq = sequence_generator(second_seq, second_seq_numbers_list)
    return first_seq, second_seq


# This function initializes the cost matrix
def cost_matrix_initializer(first_dimension, second_dimension):
    output_matrix = []
    i = 0
    first_row = []
    while i <= first_dimension:
        first_row.append(i * GAP_COST)
        i += 1
    output_matrix.append(first_row)
    j = 1
    while j <= second_dimension:
        temp_list = [j * GAP_COST]
        i = 1
        while i <= first_dimension:
            temp_list.append(-1)
            i += 1
        output_matrix.append(temp_list)
        j += 1
    return output_matrix


# This function prints the input matrix
def matrix_printer(input_matrix):
    i = len(input_matrix) - 1
    while i >= 0:
        print(input_matrix[i])
        i = i - 1


# This function prints the input matrix
def new_matrix_printer(input_matrix):
    i = 0
    while i < len(input_matrix):
        print(input_matrix[i])
        i += 1


# This function calculates the optimal cost using dynamic programming
def optimal_cost_calculator(input_cost_matrix, input_seq_one, input_seq_two):
    input_seq_one_list = []
    input_seq_two_list = []
    for letter in input_seq_one:
        input_seq_one_list.append(letter)
    for letter in input_seq_two:
        input_seq_two_list.append(letter)
    i = 1
    while i <= len(input_seq_one):
        j = 1
        while j <= len(input_seq_two):
            input_cost_matrix[j][i] = min(input_cost_matrix[j - 1][i] + GAP_COST, input_cost_matrix[j][i - 1] + GAP_COST, input_cost_matrix[j - 1][i - 1] + ALFA_DICTIONARY[input_seq_one_list[i - 1] + input_seq_two_list[j - 1]])
            j += 1
        i += 1
    return input_cost_matrix, input_seq_one_list, input_seq_two_list


# This function reverses the input string
def reverse_string(input_string):
    return input_string[::-1]


# This function gets the cost matrix and input sequences and returns the two aligned sequences
def aligned_seqs_generator_memory_efficient_version(input_seq_one, input_seq_two, input_cost_matrix, input_seq_one_list, input_seq_two_list):
    current_row = len(input_seq_two)
    current_column = len(input_seq_one)
    output_seq_one = ""
    output_seq_two = ""
    while True:
        if current_row == 0 and current_column == 0:
            break
        print(input_seq_one_list[current_column - 1] + input_seq_two_list[current_row - 1])
        if input_cost_matrix[current_row][current_column] == input_cost_matrix[current_row - 1][current_column - 1] + ALFA_DICTIONARY[input_seq_one_list[current_column - 1] + input_seq_two_list[current_row - 1]]:
            print("it is here")
            output_seq_one = output_seq_one + input_seq_one_list[current_column - 1]
            output_seq_two = output_seq_two + input_seq_two_list[current_row - 1]
            current_column = current_column - 1
            current_row = current_row - 1
        else:
            if input_cost_matrix[current_row][current_column] == input_cost_matrix[current_row - 1][current_column] + GAP_COST:
                output_seq_one = output_seq_one + "_"
                output_seq_two = output_seq_two + input_seq_two_list[current_row - 1]
                current_row = current_row - 1
            else:
                if input_cost_matrix[current_row][current_column] == input_cost_matrix[current_row][current_column - 1] + GAP_COST:
                    output_seq_one = output_seq_one + input_seq_one_list[current_column - 1]
                    output_seq_two = output_seq_two + "_"
                    current_column = current_column - 1
        print("=============")
        print("current output seq one: " + str(output_seq_one))
        print("current output seq two: " + str(output_seq_two))
        print("=============")

    return reverse_string(output_seq_one), reverse_string(output_seq_two)


# main part of the code starts here
input_file_name = "input1.txt"
seq_one, seq_two = input_file_reader(input_file_name)
# cost_matrix = cost_matrix_initializer(len(seq_one), len(seq_two))
# cost_matrix, seq_one_chars_list, seq_two_chars_list = optimal_cost_calculator(cost_matrix, seq_one, seq_two)
# splitting the first sequence into two parts
seq_one_chars_list = []
for letter in seq_one:
    seq_one_chars_list.append(letter)
if len(seq_one) % 2 == 0:
    middle = len(seq_one) / 2
else:
    middle = int(len(seq_one) / 2)
seq_one_first_half = []
seq_one_second_half = []
i = 0
while i < middle:
    seq_one_first_half.append(seq_one_chars_list[i])
    i += 1

i = middle
while i < len(seq_one):
    seq_one_second_half.append(seq_one_chars_list[i])
    i += 1
seq_one_first_half_string = ""
seq_one_second_half_string = ""
i = 0
while i < len(seq_one_first_half):
    seq_one_first_half_string = seq_one_first_half_string + seq_one_first_half[i]
    i += 1
i = 0
while i < len(seq_one_second_half):
    seq_one_second_half_string = seq_one_second_half_string + seq_one_second_half[i]
    i += 1

first_half_cost_matrix = cost_matrix_initializer(len(seq_one_first_half_string), len(seq_two))
first_half_cost_matrix, seq_one_first_half_string_chars_list, seq_two_chars_list = optimal_cost_calculator(first_half_cost_matrix, seq_one_first_half_string, seq_two)
seq_one_reverse_second_half_string = reverse_string(seq_one_second_half_string)
seq_two_reverse_string = reverse_string(seq_two)
second_half_cost_matrix = cost_matrix_initializer(len(seq_one_reverse_second_half_string), len(seq_two_reverse_string))
second_half_cost_matrix, seq_one_reverse_second_half_string_chars_list, seq_two_reverse_string_chars_list = optimal_cost_calculator(second_half_cost_matrix, seq_one_reverse_second_half_string, seq_two_reverse_string)

first_half_cost_matrix_last_column = []
second_half_cost_matrix_last_column = []
i = 0
while i <= len(seq_two):
    first_half_cost_matrix_last_column.append(first_half_cost_matrix[i][len(seq_one_first_half_string)])
    i += 1
i = 0
while i <= len(seq_two_reverse_string):
    second_half_cost_matrix_last_column.append(second_half_cost_matrix[i][len(seq_one_second_half_string)])
    i += 1
last_column_summation = []
i = 0
while i < len(first_half_cost_matrix_last_column):
    last_column_summation.append(first_half_cost_matrix_last_column[i] + second_half_cost_matrix_last_column[i])
    i += 1
minimum_value = last_column_summation[0]
minimum_value_index = 0
i = 1
while i < len(last_column_summation):
    if minimum_value >= last_column_summation[i]:
        minimum_value = last_column_summation[i]
        minimum_value_index = i
    i += 1

aligned_seq_one_first_half, aligned_seq_two = aligned_seqs_generator_memory_efficient_version(seq_one_first_half_string, seq_two, first_half_cost_matrix, seq_one_first_half_string_chars_list, seq_two_chars_list)
aligned_seq_one_second_half, aligned_seq_two_reverse = aligned_seqs_generator_memory_efficient_version(seq_one_second_half_string, seq_two_reverse_string, second_half_cost_matrix, seq_one_reverse_second_half_string_chars_list, seq_two_reverse_string_chars_list)

















































