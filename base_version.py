



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
    return input_cost_matrix


# main part of the code starts here
input_file_name = "input5.txt"
seq_one, seq_two = input_file_reader(input_file_name)
cost_matrix = cost_matrix_initializer(len(seq_one), len(seq_two))
cost_matrix = optimal_cost_calculator(cost_matrix, seq_one, seq_two)
print("The minimum cost is: " + str(cost_matrix[len(seq_two)][len(seq_one)]))
print("the len of seq one: " + str(len(seq_one)))
print("the len of seq two: " + str(len(seq_two)))
exit()
aligned_seq_one, aligned_seq_two = aligned_seqs_generator(seq_one, seq_two, cost_matrix)












