import copy

import Tools


def solution1(n):
    class Bar:
        bar_id = 0

        def __init__(self, val):
            self.val = val
            self.id  = Bar.bar_id
            Bar.bar_id += 1

        def look_for_offspring(self,):
            child_size = 0
            last_child_size = child_size
            still_looking = True
            perm_count, child_perms = 0, 0
            while still_looking:
                if  self.val == 1:
                    return perm_count + child_perms
                elif self.val <= child_size:
                    break

                child_size = last_child_size + 1
                self.val  -= 1
                print( self.id, self.val, child_size, child_perms)
                child_bar   = Bar(child_size)
                child_perms += child_bar.look_for_offspring()
                perm_count += 1
                last_child_size = child_size
                print( child_perms)
            return perm_count + child_perms

    def find_sums(num):
        sum_list = []
        while True:
            pass


    sum_vars = []
    for i in range(10):
        pass

    base_bar = Bar(n)
    count    = base_bar.look_for_offspring()
    print("Final count ", count)


def solution2(n):
    def get_addend_pairs(num):
        numbers = [n for n in range(num, -1, -1)]




    for i in range(n, 0, -1):
        remainder = n - i
        remainder_addends = [j for j in range(remainder, -1, -1)]
        print(i, remainder, remainder_addends)

@Tools.profile
def solution3(n):
    def print_all_sum_rec(target, current_sum, start, output, result):
        if current_sum == target:
            output.append(copy.copy(result))

        for i in range(start, target):
            temp_sum = current_sum + i
            if temp_sum <= target:
                result.append(i)
                #print("sum", temp_sum, "s", i+1,
                #      "out", output, "res", result)
                print_all_sum_rec(target, temp_sum, i+1, output, result)
                result.pop()
            else:
                return

    def print_all_sum(target):
        output, result = [], []
        print_all_sum_rec(target, 0, 1, output, result)
        return output



    final_result = print_all_sum(n)
    #for addend_set in final_result:
    #    print(addend_set)

    return len(final_result)


def test_solution():
    test_cases = [[3, 1],
                  [4, 1],
                  [5, 2],
                  [6, 3],
                  [7, 4],
                  [8, 5],

                  [200, 487067745],
                  ]
    solution3(4)
    print()
    #solution3(8)
    Tools.run_tests(solution3, test_cases, True, 1)
    #Tools.run_tests(solution2, test_cases, False, 10000)
    #Tools.run_tests(solution3, test_cases, False, 10000)
    #Tools.run_tests(solution4, test_cases, False, 10000)
    #Tools.run_tests(solution5, test_cases, False, 10000)


test_solution()