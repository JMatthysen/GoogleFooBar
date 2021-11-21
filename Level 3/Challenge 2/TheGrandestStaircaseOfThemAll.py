import Tools

def solution1(n):
    class Bar:
        def __init__(self, val):
            self.val = val

        def _split(self, ):

    count = 0
    brick_pool = n
    still_looking = True
    while still_looking:
        brick_pool = n
        bars = []
        first_bar = brick_pool - 1



def test_solution():
    test_cases = [[200, 487067745],
                  [3, 1],
                  [4, 1],
                  [5, 2]

                  ]

    Tools.run_tests(solution1, test_cases, True, 1)
    #Tools.run_tests(solution2, test_cases, False, 10000)
    #Tools.run_tests(solution3, test_cases, False, 10000)
    #Tools.run_tests(solution4, test_cases, False, 10000)
    #Tools.run_tests(solution5, test_cases, False, 10000)


test_solution()