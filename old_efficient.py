import sys
import time
import psutil


GAP_COST = 30
ALFA_DICTIONARY = {"AA": 0, "AC": 110, "AG": 48, "AT": 94,
                   "CA": 110, "CC": 0, "CG": 118, "CT": 48,
                   "GA": 48, "GC": 118, "GG": 0, "GT": 110,
                   "TA": 94, "TC": 48, "TG": 110, "TT": 0}


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


def matrix_printer(input_matrix):
    i = len(input_matrix) - 1
    while i >= 0:
        print(input_matrix[i])
        i = i - 1


def process_memory():
    process = psutil.Process()
    memory_info = process.memory_info()
    memory_consumed = int(memory_info.rss / 1024)
    return memory_consumed


def new_matrix_printer(input_matrix):
    i = 0
    while i < len(input_matrix):
        print(input_matrix[i])
        i += 1


def optimal_cost_calculator(input_cost_matrix, input_seq_one, input_seq_two, return_chars_lists):
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
    if return_chars_lists:
        return input_cost_matrix, input_seq_one_list, input_seq_two_list
    else:
        return input_cost_matrix


def reverse_string(input_string):
    return input_string[::-1]


def aligned_seqs_generator_memory_efficient_version(input_seq_one, input_seq_two, input_cost_matrix, input_seq_one_list, input_seq_two_list, input_index):
    current_row = input_index
    current_column = len(input_seq_one)
    output_seq_one = ""
    output_seq_two = ""
    while True:
        if current_row == 0 and current_column == 0:
            break
        if input_cost_matrix[current_row][current_column] == input_cost_matrix[current_row - 1][current_column - 1] + ALFA_DICTIONARY[input_seq_one_list[current_column - 1] + input_seq_two_list[current_row - 1]]:
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

    return reverse_string(output_seq_one), reverse_string(output_seq_two)


def aligned_seqs_generator_memory_efficient_version_reverse(input_seq_one, input_seq_two, input_cost_matrix, input_seq_one_list, input_seq_two_list, input_index):
    current_row = input_index
    current_column = len(input_seq_one)
    output_seq_one = ""
    output_seq_two = ""
    while True:
        if current_row == 0 and current_column == 0:
            break
        if input_cost_matrix[current_row][current_column] == input_cost_matrix[current_row - 1][current_column - 1] + ALFA_DICTIONARY[input_seq_one_list[current_column - 1] + input_seq_two_list[current_row - 1]]:
            output_seq_one = output_seq_one + input_seq_one_list[current_column - 1]
            output_seq_two = output_seq_two + input_seq_two_list[current_row - 1]
            current_column = current_column - 1
            current_row = current_row - 1
        else:
            if input_cost_matrix[current_row][current_column] == input_cost_matrix[current_row][current_column - 1] + GAP_COST:
                output_seq_one = output_seq_one + input_seq_one_list[current_column - 1]
                output_seq_two = output_seq_two + "_"
                current_column = current_column - 1

            else:
                if input_cost_matrix[current_row][current_column] == input_cost_matrix[current_row - 1][current_column] + GAP_COST:
                    output_seq_one = output_seq_one + "_"
                    output_seq_two = output_seq_two + input_seq_two_list[current_row - 1]
                    current_row = current_row - 1

    return reverse_string(output_seq_one), reverse_string(output_seq_two)


def output_file_generator(output_file_path_argument, input_aligned_seq_one, input_aligned_seq_two, input_consumed_memory, input_time_taken, input_cost):
    output_file = open(output_file_path_argument, "wt")
    output_file.write(str(input_cost) + "\n")
    output_file.write(str(input_aligned_seq_one) + "\n")
    output_file.write(str(input_aligned_seq_two) + "\n")
    output_file.write(str(round(input_time_taken, 5)) + "\n")
    output_file.write(str(input_consumed_memory))
    output_file.close()


def seq_alignment_efficient_version(input_file_path_argument, output_file_path_argument):
    input_file_name = input_file_path_argument
    seq_one, seq_two = input_file_reader(input_file_name)
    # splitting the first sequence into two parts
    start_time = time.time()
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

    i = int(middle)
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
    first_half_cost_matrix = optimal_cost_calculator(first_half_cost_matrix, seq_one_first_half_string, seq_two, False)
    seq_one_reverse_second_half_string = reverse_string(seq_one_second_half_string)
    seq_two_reverse_string = reverse_string(seq_two)
    first_half_cost_matrix_last_column = []
    i = 0
    while i <= len(seq_two):
        first_half_cost_matrix_last_column.append(first_half_cost_matrix[i][len(seq_one_first_half_string)])
        i += 1
    first_half_cost_matrix = cost_matrix_initializer(len(seq_one_reverse_second_half_string), len(seq_two_reverse_string))
    first_half_cost_matrix = optimal_cost_calculator(first_half_cost_matrix, seq_one_reverse_second_half_string, seq_two_reverse_string, False)
    second_half_cost_matrix_last_column = []
    i = 0
    while i <= len(seq_two_reverse_string):
        second_half_cost_matrix_last_column.append(first_half_cost_matrix[i][len(seq_one_second_half_string)])
        i += 1
    last_column_summation = []
    i = 0
    while i < len(first_half_cost_matrix_last_column):
        last_column_summation.append(first_half_cost_matrix_last_column[i] + second_half_cost_matrix_last_column[(len(first_half_cost_matrix_last_column) - 1) - i])
        i += 1
    minimum_value = last_column_summation[0]
    minimum_value_index = 0
    i = 1
    while i < len(last_column_summation):
        if minimum_value >= last_column_summation[i]:
            minimum_value = last_column_summation[i]
            minimum_value_index = i
        i += 1
    first_half_cost_matrix = cost_matrix_initializer(len(seq_one_first_half_string), len(seq_two))
    first_half_cost_matrix, seq_one_first_half_string_chars_list, seq_two_chars_list = optimal_cost_calculator(first_half_cost_matrix, seq_one_first_half_string, seq_two, True)
    aligned_seq_one_first_half, aligned_seq_two = aligned_seqs_generator_memory_efficient_version(seq_one_first_half_string, seq_two, first_half_cost_matrix, seq_one_first_half_string_chars_list, seq_two_chars_list, minimum_value_index)
    first_half_cost_matrix = cost_matrix_initializer(len(seq_one_reverse_second_half_string), len(seq_two_reverse_string))
    first_half_cost_matrix, seq_one_reverse_second_half_string_chars_list, seq_two_reverse_string_chars_list = optimal_cost_calculator(first_half_cost_matrix, seq_one_reverse_second_half_string, seq_two_reverse_string, True)
    aligned_seq_one_second_half, aligned_seq_two_reverse = aligned_seqs_generator_memory_efficient_version_reverse(seq_one_reverse_second_half_string, seq_two_reverse_string, first_half_cost_matrix, seq_one_reverse_second_half_string_chars_list, seq_two_reverse_string_chars_list, (len(first_half_cost_matrix_last_column) - 1) - minimum_value_index)
    aligned_seq_one_final = aligned_seq_one_first_half + reverse_string(aligned_seq_one_second_half)
    aligned_seq_two_final = aligned_seq_two + reverse_string(aligned_seq_two_reverse)
    end_time = time.time()
    time_taken = (end_time - start_time) * 1000
    consumed_memory = process_memory()
    output_file_generator(output_file_path_argument, aligned_seq_one_final, aligned_seq_two_final, consumed_memory, time_taken, minimum_value)


if __name__ == "__main__":
    if len(sys.argv) < 3 or len(sys.argv) > 3:
        print("Wrong input arguments format")
        sys.exit()
    else:
        input_file_path = sys.argv[1]
        output_file_path = sys.argv[2]
        seq_alignment_efficient_version(input_file_path, output_file_path)































