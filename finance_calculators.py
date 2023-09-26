import math

#Creating a program that allows a user to access two different financial calculations.
print("Choose either 'investment' or 'bond' from the menu below to proceed: ")
print("\n investment \n to calculate the amount of interest you'll earn on your investment")
print("\n bond \n to calculate the amount you'll have to pay on a home loan")

#Creating a choice option where the user will choose between investment and bond.
choice = input("Choose 'i' for investment and 'b' for bond: \n")

if choice == "i":
    amount = int(input("Enter the deposit amount: \n"))
    interest_rate = int(input("Enter the interest rate without the precentage: \n"))
    num_years = int(input("Enter the number of years you plan on investing for: \n"))
    interest = input("Choose if you'd like 'simple' or 'compund' interest: ")

#Now we will calculate the simple interest and the compound interest using the relevant forumulae.
    if interest == "simple":
        P = int(amount)
        r = int(interest_rate)
        t = (num_years)
        simple_interest = P(1+r*t)
        print(f"Your interest is {simple_interest}")

    else:
        P = int(amount)
        r = int(interest_rate)
        t = (num_years)
        compound_interest = P*math.pow((1+r),t)
        print(f"Your compound interest is {compound_interest}")

else:
    present_value = int(input("Enter the present value of the house: \n"))
    interest_rate2 = int(input("Enter the interest rate: \n"))
    num_years2 = int(input("Enter the number of months over which the bond will be repaid: \n"))

    #Redefining the variables in order to use them in the formula to calculate the bond repayment.
    P2 = present_value
    i = interest_rate2
    n = num_years2

    monthly_payment = (i*P2)/(1-(1+i)^(-n))
    print(f"The amount you'll be paying every month for the bond is {monthly_payment}")