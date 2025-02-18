# TASK: Write a function that validates an email format.

# Define a function that takes a string parameter
def email_validator(email):
# Check if '@' is in the email
# Extract the last four characters of the email
# Check if it ends with '.com' or '.net'
    if "@" in email and (email[-4:] == ".com"  or email[-4:] == ".net" or email[-3:] == ".ca"):
        # Return True if valid, False otherwise
        return True
    else:
        return False



# Prompt the user for an email input and call the function
email = input("Please enter your email:\n")
vaild = email_validator(email)

if vaild is True:
    print("Your email is valid")
else:
    print("Your email is not valid")
# Display whether the email is valid
