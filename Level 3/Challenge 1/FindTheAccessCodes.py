import Tools
import random


def solution1(l):
    unique_numbers = {}

    trees = {}
    for num in l:
        if num not in trees.keys():
            trees[num] = []

        for key in trees:
            if num % key == 0:
                trees[key].append(num)
    print(trees)

    return 0

def generate_test_case(nums, low=1, high=999999):
    nums = []
    return [random.randint(low, high) for i in range(nums)]



def test_solution():
    test_cases = [[[1, 1, 1], 1],
                  [[1, 2, 3, 4, 5, 6], 3],
                  [generate_test_case(10, 1, 20), None]

                  ]

    Tools.run_tests(solution1, test_cases, True, 1)
    #Tools.run_tests(solution2, test_cases, False, 10000)
    #Tools.run_tests(solution3, test_cases, False, 10000)
    #Tools.run_tests(solution4, test_cases, False, 10000)
    #Tools.run_tests(solution5, test_cases, False, 10000)


test_solution()