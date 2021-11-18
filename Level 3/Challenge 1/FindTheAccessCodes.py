import Tools
import random


def solution1(l):
    class Node:
        def __init__(self, val):
            self.val = val
            self.children = []

        def print_vals(self):
            print([child.val for child in self.children])

    tree = {}

    for num in l:
        temp_node = Node(num)
        for key in tree.keys():
            if num % key == 0:
                for node in tree[key]:
                    node.children.append(temp_node)

        if num not in tree.keys():
            tree[num] = [temp_node]

    

    return 0

def generate_test_case(nums, low=1, high=999999):
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