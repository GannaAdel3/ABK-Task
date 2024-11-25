TotalAmountBeingRented = 4000000
AnnualInterestRate = 0.15
NumberOfPeriodsPerYear = 12
TotalDuration = 3

r = AnnualInterestRate / NumberOfPeriodsPerYear
n = NumberOfPeriodsPerYear * TotalDuration

numerator = (TotalAmountBeingRented * r) * ((1 + r) ** n)
denominator = ((1 + r) ** n) - 1

PMT = numerator / denominator

for i in range(n):
    cost = TotalAmountBeingRented
    Interest = cost * r
    PrincipalRepayment = PMT - Interest
    if PrincipalRepayment > cost :
        RemainingPrincipal = 0
    else:
        RemainingPrincipal = cost - PrincipalRepayment
    TotalAmountBeingRented = RemainingPrincipal
    print(f"{cost:.2f} | {PMT:.2f} | {PrincipalRepayment:.2f} | {RemainingPrincipal:.2f}")



# TotalAmountBeingRented = 100000
# AnnualInterestRate = 0.15
# NumberOfPeriodsPerYear = 12
# TotalDuration = 3
# ChangeMonth = 12
# NewAnnualInterestRate = 0.10
#
#
# def calculate_PMT(TotalAmountBeingRented, AnnualInterestRate, NumberOfPeriodsPerYear, TotalDuration):
#     r = AnnualInterestRate / NumberOfPeriodsPerYear
#     n = NumberOfPeriodsPerYear * TotalDuration
#     numerator = (TotalAmountBeingRented * r) * ((1 + r) ** n)
#     denominator = ((1 + r) ** n) - 1
#     PMT = numerator / denominator
#     return PMT, r
#
#
# PMT, r = calculate_PMT(TotalAmountBeingRented, AnnualInterestRate, NumberOfPeriodsPerYear, TotalDuration)
# n = NumberOfPeriodsPerYear * TotalDuration
#
# for i in range(n):
#     if i == ChangeMonth:
#         remaining_duration = (n - i) / NumberOfPeriodsPerYear
#         PMT, r = calculate_PMT(TotalAmountBeingRented, NewAnnualInterestRate, NumberOfPeriodsPerYear,
#                                remaining_duration)
#
#     cost = TotalAmountBeingRented
#     Interest = cost * r
#     PrincipalRepayment = PMT - Interest
#     if PrincipalRepayment > cost:
#         RemainingPrincipal = 0
#     else:
#         RemainingPrincipal = cost - PrincipalRepayment
#     TotalAmountBeingRented = RemainingPrincipal
#     print(f"{cost:.2f} | {PMT:.2f} | {PrincipalRepayment:.2f} | {RemainingPrincipal:.2f}")
