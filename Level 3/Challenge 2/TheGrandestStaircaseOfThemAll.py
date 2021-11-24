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




def test_solution():
    test_cases = [[200, 487067745],
                  [3, 1],
                  [4, 1],
                  [5, 2]

                  ]
    solution2(3)
    print()
    solution2(4)
    #Tools.run_tests(solution1, test_cases, True, 1)
    #Tools.run_tests(solution2, test_cases, False, 10000)
    #Tools.run_tests(solution3, test_cases, False, 10000)
    #Tools.run_tests(solution4, test_cases, False, 10000)
    #Tools.run_tests(solution5, test_cases, False, 10000)


test_solution()