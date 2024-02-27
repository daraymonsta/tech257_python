
double_quotes_str = "Look! Double quotes!"
single_quotes_str = 'Look! Single quotes!'
print(double_quotes_str)
print(single_quotes_str)

# bad_str = 'I said 'Wow!''

escape_str = 'I said \'Wow!\''
print(escape_str)
double_quotes_in_single_quotes_str = 'I said "Wow!"'
print(double_quotes_in_single_quotes_str)
single_quotes_in_double_quotes_str = "I said 'Wow!'"
print(single_quotes_in_double_quotes_str)

extra_spaces_str = "   Bob                   "
print(len(extra_spaces_str))
print(len(extra_spaces_str.strip()))

example_str = "here's some text with lots of text"
print(example_str)
# count how many times substring occurs in a string
print(example_str.count("text"))

# all lowercase
print(example_str.lower())

# all uppercase
print(example_str.upper())

# capitalise first letter
print(example_str.capitalize())

# replace something in sting
print(example_str.replace(" with", ","))
