
GAP_COST = 30
ALFA_DICTIONARY = {"AA": 0, "AC": 110, "AG": 48, "AT": 94,
                   "CA": 110, "CC": 0, "CG": 118, "CT": 48,
                   "GA": 48, "GC": 118, "GG": 0, "GT": 110,
                   "TA": 94, "TC": 48, "TG": 110, "TT": 0}

def alignment_cost_calculator(first_string, second_string):
    total_cost = 0
    first_string_chars = []
    second_string_chars = []
    for letter in first_string:
        first_string_chars.append(letter)
    for letter in second_string:
        second_string_chars.append(letter)

    if len(first_string_chars) != len(second_string_chars):
        print("The length of the two strings does not equal")
    else:
        i = 0
        while i < len(first_string_chars):
            if first_string_chars[i] == "_" or second_string_chars[i] == "_":
                total_cost += GAP_COST
            else:
                total_cost += ALFA_DICTIONARY[first_string_chars[i] + second_string_chars[i]]
            i += 1
        print("The total cost is: " + str(total_cost))


# main part of the code
first_seq = "_A_CA_CACT__G__A_C_TAC_TGACTG_GTGA__C_TACTGACTGGACTGACTACTGACTGGTGACTAC_TGACTG_G"
second_seq = "TATTATTA_TACGCTATTATACGCGAC_GCG_GACGCGTA_T_AC_G__CT_ATTA_T_AC_G_CGAC_GCG_GAC_GCG"
alignment_cost_calculator(first_seq, second_seq)



























