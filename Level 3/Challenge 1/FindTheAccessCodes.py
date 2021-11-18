import Tools
import random


def solution1(l):
    class Node:
        def __init__(self, val):
            self.val = val
            self.children = []

    tree = {}

    for num in l:
        temp_node = Node(num)
        for key in tree.keys():
            if num % key == 0:
                for node in tree[key]:
                    node.children.append(temp_node)

        if num not in tree.keys():
            tree[num] = [temp_node]
        else:
            tree[num].append(temp_node)

    lucky_tuples = 0
    for key in tree.keys():
        for base_node in tree[key]:
            for child in base_node.children:
                lucky_tuples += len(child.children)


    return lucky_tuples



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