first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)
# To insert a variable’s value into a string, place the letter f immediately
# before the opening quotation mark . Put braces around the name or names
# of any variable you want to use inside the string. Python will replace each
# variable with its value when the string is displayed.
# These strings are called f-strings.
# The f is for format, because Python
# formats the string by replacing the name of any variable in braces with its
# value.
print(f"Hello, {full_name.title()}!") # use f-strings to compose complete messages using the information associated with a variable
