month = 0
totalPaid = 0

monthlyInterestRate = annualInterestRate / 12.0
while month <12:
    minPayment = monthlyPaymentRate * balance   #Computing monthly payment
    unpayBal = balance - minPayment
    totalPaid += minPayment
    balance = unpayBal + (monthlyInterestRate * unpayBal)
    month += 1
    print('Month: ' + str(month))
    print('Minimum monthly payment: ' + str(round(minPay,2)))
    print('Remaining balance: ' + str(round(balance,2)))
print('Total paid: ' + str(round(totalPaid,2)))
print('Remaining balance: ' + str(round(balance,2)))
