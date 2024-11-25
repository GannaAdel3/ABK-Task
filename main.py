# TotalAmountBeingRented = 100000
# AnnualInterestRate = 0.15
# NumberOfPeriodsPerYear = 12
# TotalDuration = 3
#
# r = AnnualInterestRate / NumberOfPeriodsPerYear
# n = NumberOfPeriodsPerYear * TotalDuration
#
# numerator = (TotalAmountBeingRented * r) * ((1 + r) ** n)
# denominator = ((1 + r) ** n) - 1
#
# PMT = numerator / denominator
#
# for i in range(n):
#     cost = TotalAmountBeingRented
#     Interest = cost * r
#     PrincipalRepayment = PMT - Interest
#     RemainingPrincipal = cost - PrincipalRepayment
#     TotalAmountBeingRented = RemainingPrincipal
#     print(f"{cost:.2f} | {PMT:.2f} | {PrincipalRepayment:.2f} | {RemainingPrincipal:.2f}")

# Principal = 100000
# AnnualInterestRate = 0.15
# months = 36
# MonthlyRate = AnnualInterestRate/12
#
# PaymentUp= ((1+MonthlyRate)**months)*Principal*MonthlyRate
# PaymentDown= ((1+MonthlyRate)**months) - (1+MonthlyRate)
# Payment = PaymentUp/PaymentDown
# for i in range(months-1):
#     cost = Principal
#     Interest = cost * MonthlyRate
#     PrincipalRepayment = Payment - Interest
#     RemainingPrincipal = cost - PrincipalRepayment
#     Principal = RemainingPrincipal
#     print(f"{cost:.2f} | {Payment:.2f} | {PrincipalRepayment:.2f} | {RemainingPrincipal:.2f}")

# def goal_seek(func , goal , initial_guess , tolerance =1e-6 , max_iterations = 1000):
#     x = initial_guess
#     for i in range(max_iterations):
#         y = func(x)
#         error = goal - y
#         if abs(error)<tolerance:
#             return x
#         h = 1e-5
#         derivative = (func(x+h)-func(x))/h
#         if derivative == 0 :
#             raise ValueError("Derivative is zero")
#         x += error / derivative
#     raise ValueError("Max iterations")
# def function_example (x):
#     return x*2
# goal = 10
# initial_guess = 1.0
# try:
#     solution = goal_seek(function_example, goal, initial_guess)
#     print(solution)
# except ValueError as e:
#     print(e)
#

# def calculate_payment(principal, annual_rate, periods):
#     r = annual_rate / 12
#     n = periods
#     payment = (r * principal) / (1 - (1 + r) ** -n)
#     return payment
#
#
# def goal_seek_payment(principal, annual_rate, periods, target_amount, tolerance=1e-6, max_iterations=1000):
#
#     def total_payment(payment):
#         return payment * periods
#
#     def error_function(payment):
#         return total_payment(payment) - target_amount
#
#     payment_guess = principal * annual_rate / 12
#     for _ in range(max_iterations):
#         error = error_function(payment_guess)
#         if abs(error) < tolerance:
#             return payment_guess
#         h = 1e-5
#         derivative = (error_function(payment_guess + h) - error_function(payment_guess)) /h
#         if derivative == 0:
#             raise ValueError("Derivative is zero")
#         payment_guess -= error / derivative
#     raise ValueError("Maximum iterations")
#
#
# principal = 10000
# annual_rate = 0.05
# periods = 12
# target_amount = 12000
#
# try:
#     payment = goal_seek_payment(principal, annual_rate, periods, target_amount)
#     print(f"The payment amount per period to meet the target amount is ${payment:.2f}")
# except ValueError as e:
#     print(e)



# def calculate_payment(principal, annual_rate, periods):
#     r = annual_rate / 12
#     n = periods
#     payment = (r * principal) / (1 - (1 + r) ** -n)
#     return payment
#
# def goal_seek_payment(principal, annual_rate, periods, tolerance=1e-6, max_iterations=1000):
#     def error_function(payment):
#         remaining_balance = principal * (1 + annual_rate / 12) ** periods - \
#                             payment * (((1 + annual_rate / 12) ** periods - 1) / (annual_rate / 12))
#         return remaining_balance
#
#     payment_guess = principal * annual_rate / 12
#     for i in range(max_iterations):
#         error = error_function(payment_guess)
#         if abs(error) < tolerance:
#             return payment_guess
#         h = 1e-5
#         derivative = (error_function(payment_guess + h) - error_function(payment_guess)) / h
#         if derivative == 0:
#             raise ValueError("Derivative is zero")
#         payment_guess -= error / derivative
#
#     raise ValueError("Maximum iterations exceeded")
#
# principal = 10000
# annual_rate = 0.05
# periods = 12
#
# try:
#     payment = goal_seek_payment(principal, annual_rate, periods)
#     for i in range(periods):
#         cost = principal
#         RemainingPrincipal = cost - payment
#         principal = RemainingPrincipal
#         print(f"{cost:.2f}  | {RemainingPrincipal:.2f}")
# except ValueError as e:
#     print(e)
#

# def calculate_payment(principal, annual_rate, periods):
#     r = annual_rate / 12
#     n = periods
#     payment = (r * principal) / (1 - (1 + r) ** -n)
#     return payment
#
#
# def goal_seek_payment(principal, annual_rate, periods, tolerance=1e-6, max_iterations=1000):
#     def error_function(payment):
#         remaining_balance = principal * (1 + annual_rate / 12) ** periods - \
#                             payment * (((1 + annual_rate / 12) ** periods - 1) / (annual_rate / 12))
#         return remaining_balance
#
#     payment_guess = principal * annual_rate / 12
#     for i in range(max_iterations):
#         error = error_function(payment_guess)
#         if abs(error) < tolerance:
#             return payment_guess
#         h = 1e-5
#         derivative = (error_function(payment_guess + h) - error_function(payment_guess)) / h
#         if derivative == 0:
#             raise ValueError("Derivative is zero")
#         payment_guess -= error / derivative
#
#     raise ValueError("Maximum iterations exceeded")
#
#
# principal = 10000
# annual_rate = 0.05
# periods = 12
#
# try:
#     payment = goal_seek_payment(principal, annual_rate, periods)
#
#     balance = principal
#     r = annual_rate / 12
#
#     print(f"{'Cost':<10} {'Remaining Principal':<20}")
#     for i in range(periods):
#         interest = balance * r
#         principal_payment = payment - interest
#         remaining_principal = balance - principal_payment
#         balance = remaining_principal
#         print(f"{balance + principal_payment:.2f}  | {remaining_principal:.2f}")
#
#     if abs(balance) < 1e-2:
#         print(f"{balance + principal_payment:.2f}  | 0")
#     else:
#         print(f"{balance + principal_payment:.2f}  | {balance:.2f}")
#
# except ValueError as e:
#     print(e)
#
def calculate_payment(principal, annual_rate, periods):
    r = annual_rate / 12
    n = periods
    payment = (r * principal) / (1 - (1 + r) ** -n)
    return payment


def goal_seek_payment(principal, annual_rate, periods, tolerance=1e-6, max_iterations=1000):
    def error_function(payment):
        remaining_balance = principal * (1 + annual_rate / 12) ** periods - \
                            payment * (((1 + annual_rate / 12) ** periods - 1) / (annual_rate / 12))
        return remaining_balance

    payment_guess = principal * annual_rate / 12
    for i in range(max_iterations):
        error = error_function(payment_guess)
        if abs(error) < tolerance:
            return payment_guess
        h = 1e-5
        derivative = (error_function(payment_guess + h) - error_function(payment_guess)) / h
        if derivative == 0:
            raise ValueError("Derivative is zero")
        payment_guess -= error / derivative

    raise ValueError("Maximum iterations exceeded")


principal = 100000
annual_rate = 0.15
periods = 36

try:
    payment = goal_seek_payment(principal, annual_rate, periods)

    balance = principal
    r = annual_rate / 12

    print(f"{' Cost':<11} {'Principal Payment':<9} {'Remaining Principal':<20}")
    for i in range(periods):
        interest = balance * r
        principal_payment = payment - interest
        remaining_principal = balance - principal_payment
        balance = remaining_principal
        if abs(remaining_principal) < 1e-2 and abs(balance) < 1e-2:
            remaining_principal = 0
            balance = 0

        print(f" {balance:.2f}  |     {principal_payment:.2f}     |  {remaining_principal:.2f}")

except ValueError as e:
    print(e)








