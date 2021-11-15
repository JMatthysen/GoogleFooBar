import Tools




def solution1(s):

    salute_count = 0
    lower_count  = 0
    for char in s:
        if char == '-': continue
        elif char == '>': lower_count += 1
        elif char == '<': salute_count += lower_count * 2
    return salute_count


def solution2(s):
    hyphen  = '-'
    greater = '>'
    lesser  = '<'
    salute_count = 0
    lower_count  = 0
    for char in s:
        if char is hyphen: continue
        elif char is greater:
            lower_count += 1
        elif char is lesser:
            salute_count += lower_count * 2

    return salute_count


def solution3(s):
    greater = '>'
    lesser  = '<'
    salute_count = 0
    lower_count  = 0
    for char in s:
        if   char is greater: lower_count += 1
        elif char is lesser: salute_count += lower_count * 2

    return salute_count

def solution4(s):
    greater = '>'
    lesser  = '<'

    def convert_it(char):
        if char is greater:return 1
        elif char is lesser: return -1
        return 0

    salute_count = 0
    lower_count  = 0
    for val in map(convert_it, s):
        if   val == 1: lower_count += 1
        elif val == -1: salute_count += lower_count * 2

    return salute_count

def solution5(s):
    greater = '>'
    lesser  = '<'
    salute_count = 0
    lower_count  = 0
    for char in s:
        if   char is greater: lower_count = lower_count + 1
        elif char is lesser: salute_count = salute_count + lower_count * 2

    return salute_count


def test_solution():
    test_cases = [[">----<", 2],
                  ["<<>><", 4],
                  ["--->-><-><-->-", 10],
                  ["-", 0],
                  ['>>>>>>>>>', 0],
                  ['<<<<<<<<<', 0],
                  ]

    Tools.run_tests(solution1, test_cases, False, 10000)
    Tools.run_tests(solution2, test_cases, False, 10000)
    Tools.run_tests(solution3, test_cases, False, 10000)
    Tools.run_tests(solution4, test_cases, False, 10000)
    Tools.run_tests(solution5, test_cases, False, 10000)


test_solution()