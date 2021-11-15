import Tools


def solution1(dollars):
    class Accounting:
        def __init__(self, pay_generously: bool):
            self.balance = dollars
            self.balance_remaining = True
            self.pay_roll = []
            self.num_employees = 0

            self.hand_out_checks(pay_generously)


        def hand_out_checks(self, pay_generously):

            self.pay_employee(1)  # The first always gets 1

            if pay_generously:
                # pay_roll[i] = 2 x pay_roll[i - 1]
                while self.balance_remaining:
                    self.pay_employee(2 * self.pay_roll[-1])
                #print("\nMost Generous\n", self.pay_roll)
                #print("Remainder : ", self.balance)


            else:
                # pay_roll[i] = pay_roll[i - 1] + pay_roll[i - 2]
                self.pay_employee(1)
                while self.balance_remaining:
                    self.pay_employee(self.pay_roll[-1] + self.pay_roll[-2])
                #print("\nLeast Generous\n", self.pay_roll)
                #print("Remainder : ", self.balance)

        def pay_employee(self, amount):
            if amount > self.balance:
                self.balance_remaining = False
                return

            self.balance       -= amount
            self.num_employees += 1
            self.pay_roll.append(amount)

            return

    generous = Accounting(pay_generously=True)
    stingy   = Accounting(pay_generously=False)

    return stingy.num_employees - generous.num_employees



def solution2(dollars):

    ######  Generous
    balance = dollars
    last_employee = 1
    balance  -= last_employee
    num_employees_generous = 1
    while True:
        last_employee = last_employee * 2
        if last_employee > balance: break
        balance       -= last_employee
        num_employees_generous += 1

    ######  Stingy
    balance = dollars
    last_two = [1, 1]
    balance  -= 2
    num_employees_stingy = 2
    while True:
        pay = sum(last_two)
        if pay > balance: break
        last_two = [last_two[1], pay]

        balance       -= pay
        num_employees_stingy += 1

    return num_employees_stingy - num_employees_generous



def solution3(dollars):

    ######  Generous
    one_back = 1
    balance = dollars - 1
    num_employees_generous = 1
    while True:
        one_back = one_back * 2
        if one_back > balance: break
        balance -= one_back
        num_employees_generous += 1

    ######  Stingy
    one_back, two_back = 1, 1
    balance = dollars - 2
    num_employees_stingy = 2
    while True:
        current = one_back + two_back
        if current > balance: break
        two_back  = one_back
        one_back  = current
        balance       -= current
        num_employees_stingy += 1

    return num_employees_stingy - num_employees_generous


def test_solution():
    test_cases = [[143, 3], [10, 1]]

    #Tools.run_tests(solution1, test_cases, False, 10000)
    Tools.run_tests(solution2, test_cases, False, 10000)
    Tools.run_tests(solution3, test_cases, False, 10000)



test_solution()