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
    memory_consumed = int(memory_info.rss/1024)
    return memory_consumed


def new_matrix_printer(input_matrix):
    i = 0
    while i < len(input_matrix):
        print(input_matrix[i])
        i += 1


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


def reverse_string(input_string):
    return input_string[::-1]


def aligned_seqs_generator(input_seq_one, input_seq_two, input_cost_matrix, input_seq_one_list, input_seq_two_list):
    current_row = len(input_seq_two)
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


def output_file_generator(output_file_path_argument, input_aligned_seq_one, input_aligned_seq_two, input_consumed_memory, input_time_taken, input_cost):
    output_file = open(output_file_path_argument, "wt")
    output_file.write(str(input_cost) + "\n")
    output_file.write(str(input_aligned_seq_one) + "\n")
    output_file.write(str(input_aligned_seq_two) + "\n")
    output_file.write(str(round(input_time_taken, 5)) + "\n")
    output_file.write(str(input_consumed_memory) + "\n")
    output_file.close()


def seq_alignment_base_version(input_file_path_argument, output_file_path_argument):
    input_file_name = input_file_path_argument
    seq_one, seq_two = input_file_reader(input_file_name)
    start_time = time.time()
    cost_matrix = cost_matrix_initializer(len(seq_one), len(seq_two))
    cost_matrix, seq_one_chars_list, seq_two_chars_list = optimal_cost_calculator(cost_matrix, seq_one, seq_two)
    print("The minimum cost is: " + str(cost_matrix[len(seq_two)][len(seq_one)]))
    print("the len of seq one: " + str(len(seq_one)))
    print("the len of seq two: " + str(len(seq_two)))
    print("seq one:")
    print(seq_one)
    print("seq two:")
    print(seq_two)
    print("=====================================")
    aligned_seq_one, aligned_seq_two = aligned_seqs_generator(seq_one, seq_two, cost_matrix, seq_one_chars_list, seq_two_chars_list)
    end_time = time.time()
    time_taken = (end_time - start_time) * 1000
    print("aligned seq one: ")
    print(aligned_seq_one)
    print("aligned seq two: ")
    print(aligned_seq_two)
    print("the len of aligned seq two: " + str(len(aligned_seq_two)))
    consumed_memory = process_memory()
    print("the consumed memory: " + str(process_memory()))
    print("the taken_time: " + str(time_taken) + " ms")
    output_file_generator(output_file_path_argument, aligned_seq_one, aligned_seq_two, consumed_memory, time_taken, cost_matrix[len(seq_two)][len(seq_one)])


if __name__ == "__main__":
    if len(sys.argv) < 3 or len(sys.argv) > 3:
        print("Wrong input arguments format")
        sys.exit()
    else:
        input_file_path = sys.argv[1]
        output_file_path = sys.argv[2]
        seq_alignment_base_version(input_file_path, output_file_path)













