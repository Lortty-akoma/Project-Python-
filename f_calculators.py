import math
#The output below should inform the user on what he wants to do
print("investment - to calculate the amount of interest you will earn on your investment")
print("bond - to calculate the amount you will have to pay on a home loan")

#Get the user to choose from the options given to proceed to the next stage
f_calculator = input("Enter either 'investment' or 'bond' from the menu above to proceed : ")
print(f_calculator)

#This validates any format the user used to make the entry
user_input = f_calculator.lower()
print(user_input)

#Check if user entered the appropriate option and print appropriate error
if (len(user_input) == 0) or (user_input != "bond") and (user_input != "investment") :
    print("Please enter a valid entry to proceed")
else:
    print("success")

#if the user chooses investment, below is the entry required of the user. 
# #The user also enters either simple or compound interest to determine how the interest will be calculated.
if f_calculator == "investment" :
    amount = int(input("Enter the deposit amount: "))
    rate = int(input("What is the interest rate? Please enter only the number: "))/100
    years = int(input("How many years are you investing?:  "))
    interest = input("Please enter your preference; 'simple' or 'compound': ")
#The formula for calculating simple interest as shown if the user opts for that and the total amount is displayed using the print function
    if interest == "simple":
        totalAmount = amount * (1 + rate * years)
        print(totalAmount)

#otherwise, the compound interest as shown below is used and the total amount is displayed using the print function.
    elif interest == "compound":
        totalAmount = amount * math.pow((1+rate), years)
        print(totalAmount)

#if the user opts for bond, the following entries below is require of the user
elif f_calculator == "bond":
    p_value = int(input("Enter the present of the house:  "))
    interest = (int(input("What is the interest rate? Please enter only the number:  "))/100)/12
    months = int(input("How many months to repay?: "))

#the formula for calculating bond is shown below and the final amount is displayed using the print function
Repayment = (interest * p_value) / (1 - (1 + interest)**(- months))
print(Repayment)






