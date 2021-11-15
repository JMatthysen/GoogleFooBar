import random
from Tools import profile


def solution(s):
    char_count = s.count(s[0])

    total_length          = len(s)
    possible_group_widths = [ total_length // mult for mult in get_multiples(char_count)]
    for i in range(len(possible_group_widths) - 1, 0, -1):
        width = possible_group_widths[i]

        num_correct   = 1
        split_strings = [s[index : index + width] for index in range(0, len(s), width)]

        for string in split_strings[1:]:
            if string != split_strings[0]: break
            num_correct += 1
        num_groups = total_length // possible_group_widths[i]
        if num_correct == num_groups: return num_groups

    return 1


def solution1(s):
    # def get_common_multiple(list of counts)

    char_counts = {}
    for char in s:
        if char not in char_counts.keys():
            char_counts[char] = 1
            continue
        char_counts[char] += 1

    total_length = len(s)
    possible_group_widths = [ total_length // mult for mult in get_multiples(char_counts[s[0]]) ]
    for i in range(len(possible_group_widths) - 1, -1, -1):
        groups = []
        width  = possible_group_widths[i]
        base_group = s[:width]
        #print(base_group)
        num_groups = total_length // possible_group_widths[i]
        #print(num_groups)
        split_strings = [s[index : index + width] for index in range(0, len(s), width)]
        #print(split_strings)

        num_correct = 0
        for string in split_strings:
            if string == base_group:
                num_correct += 1
            else:
                break
        if num_correct == num_groups:
            return num_groups

    return


def get_multiples(num):
    return [i for i in range(1, num + 1) if not num % i]


def generate_test_cases(num_cases=10):
    alphabet   = "abcdefghijklmnopqrstuvwxyz"
    test_cases = []

    for i in range(num_cases):
        total_length        = random.randint(1, 199)
        possible_num_groups = get_multiples(total_length)
        num_groups   = possible_num_groups[random.randint(0, len(possible_num_groups) - 1)]
        group_length = total_length // num_groups

        group = "".join([ alphabet[random.randint(0, len(alphabet) - 1)] for i in range(group_length)])

        test_cases.append(["".join(group for i in range(num_groups)), num_groups])



    return test_cases


@profile
def test_solution():
    google_test_cases    = [["abcabcabcabc", 4], ["abccbaabccba", 2]]
    generated_test_cases = generate_test_cases(1000)
    test_cases = google_test_cases + generated_test_cases

    for i, case in enumerate(test_cases):
        sol = solution(case[0])
        if sol != case[1]:
            print(f"\nTest {i}")
            print(f"______________")
            print(f"Test Case   : {case[0]}")
            print(f"string length {len(case[0])}")
            print(f"Expected    : {case[1]}")
            print(f"Solution    : {sol}")
            print(f"Test Passed : {sol == case[1]}\n")


test_solution()
