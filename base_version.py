


# This function gets a string a list of integers and returns the corresponding DNA sequence
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














input_file_name = "input1.txt"
seq1, seq2 = input_file_reader(input_file_name)














