# Build a command-line Banking Application with the following functionality:

# 1. Application starts with a prompt to the user with the following options:
#   Press 1: create account
#   Press 2: transaction


# 2. Create account: This should prompt you to enter an email/or unique identity, and then a password.
# You must check your data structure to make sure the account is unique before creating the new account.
# [Hint: Ensure that you data structure caters for each users account balance, you might want to initialize this to 0.0]


# 3. Transaction: Authenticate the user by prompting for a password,
# if the password is correct,
# user is authenticated and show the following options:
#   Press 1: check balance
#   Press 2: deposit
#   Press 3: withdraw
#   Press 4: transfer
# if the password is incorrect, tell the user that they are not authorized and go back to the create account option


# 4. check balance: query your data structure to check the balance of the authenticated user


# 5. deposit: prompt the user to enter an amount, then add the amount to the users balance


# 6. withdraw: prompt the user to enter an amount, if the user does not have money in their account,
# tell them to deposit and move to the deposit prompt.
# If they user has money, print out the amount withdrawn and the available balance,


# 7. transfer: prompt the user to enter an email of the person they want to transfer to,
# prompt for the amount, deduct the amount from the authenticated users balance,
# add the amount to the beneficiaries account,

