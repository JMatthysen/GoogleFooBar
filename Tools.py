import cProfile
import io
import pstats


def profile(func):
    def wrapper(*args, **kwargs):
        pr = cProfile.Profile()
        pr.enable()
        retval = func(*args, **kwargs)
        pr.disable()
        s = io.StringIO()
        sortby = 'cumulative'  # 'cumulative'
        ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
        ps.print_stats()
        print(s.getvalue())
        return retval

    return wrapper



@profile
def run_tests(solution, test_cases, print_results=True, repetitions_for_profiling=1):
    for repetition in range(repetitions_for_profiling):
        for i, case in enumerate(test_cases):
            sol = solution(case[0])

            if print_results:
                print(f"\nTest {i}")
                print(f"______________")
                print(f"Test Case   : {case[0]}")
                print(f"Expected    : {case[1]}")
                print(f"Solution    : {sol}")
                print(f"Test Passed : {sol == case[1]}\n")