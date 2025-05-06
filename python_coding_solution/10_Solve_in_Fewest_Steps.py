#  Given a string consisting of letters and digits, write a Python program to separate and sort letters 
# and digits individually and then concatenate them, letters first and digits after, with each group 
# sorted individually.

def separate_and_sort(s):
    # Separate letters and digits using list comprehensions
    letters = ''.join(sorted([c for c in s if c.isalpha()]))
    digits = ''.join(sorted([c for c in s if c.isdigit()]))
    
    # Concatenate letters and digits
    return letters + digits

# Example Input
input_string = "B4A1D3"

# Call the function and display the output
output_string = separate_and_sort(input_string)
print(output_string)
