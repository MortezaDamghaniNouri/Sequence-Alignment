


def letters_of_string(input_string):
    output_list = []
    for letter in input_string:
        output_list.append(letter)
    return output_list


def are_the_same(first_input_string, second_input_string):
    if len(first_input_string) != len(second_input_string):
        print("They are not the same and the length of them is different")
        print("The length of the first string: " + str(len(first_input_string)))
        print("The length of the second string: " + str(len(second_input_string)))
        return 0
    first_input_letters = letters_of_string(first_input_string)
    second_input_letters = letters_of_string(second_input_string)
    i = 0
    while i < len(first_input_letters):
        if first_input_letters[i] != second_input_letters[i]:
            print("They are not the same and the letters of them are not the same: ")
            print("The " + str(i) + "th letter of the first string: " + first_input_letters[i])
            print("The " + str(i) + "th letter of the second string: " + second_input_letters[i])
            return 0
        i += 1
    print("THE STRINGS ARE THE SAME")
    return 1


# main part of the code starts here
first_string = "_AC_AC_ACT__G__ACTA__C_TGACTG_GTGAC___TACTGACTGGACTGACTACTGACTGGTGACTACTG_ACTG_G"
second_string = "_A_CA_CACT__G__A_C_TAC_TGACTG_GTGA__C_TACTGACTGGACTGACTACTGACTGGTGACTACTG_ACTG_G"
are_the_same(first_string, second_string)





















































