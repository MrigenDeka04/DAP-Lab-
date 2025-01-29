def count_letters(s):
    upper_case = 0
    lower_case = 0
    
    for char in s:
        if char.isupper():
            upper_case += 1
        elif char.islower():
            lower_case += 1
            
    return upper_case, lower_case

# Example usage:
string = "Hi Jimmy"
upper, lower = count_letters(string)
print(f"Upper case letters: {upper}")
print(f"Lower case letters: {lower}")
