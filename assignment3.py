# NHIF premium rates(Kshs)
grossincome = int(input("Enter Your income"))
if grossincome > 0 and grossincome <= 5999:
    print("Your monthly Contribution is Kshs.150.00")
elif grossincome >= 6000 and grossincome <= 7999:
    print("Your monthly Contribution is Kshs.300.00")
elif grossincome >= 8000 and grossincome <= 11999:
    print("Your monthly Contribution is Kshs.400.00")
elif grossincome >= 12000 and grossincome <= 14999:
    print("Your monthly Contribution is Kshs.500.00")
elif grossincome >= 15000 and grossincome <= 19999:
    print("Your monthly Contribution is Kshs.600.00")
elif grossincome >= 20000 and grossincome <= 24999:
    print("Your monthly Contribution is Kshs.750.00")
elif grossincome >= 25000 and grossincome <= 29999:
    print("Your monthly Contribution is Kshs.850.00")
elif grossincome >= 30000 and grossincome <= 49999:
    print("Your monthly Contribution is Kshs.1000.00")
elif grossincome >= 50000 and grossincome <= 99999:
    print("Your monthly Contribution is Kshs.1500.00")
else:
    print("Your monthly Contribution is Kshs.2000.00")