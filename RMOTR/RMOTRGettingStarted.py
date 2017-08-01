# In Python 3, print() prints out text to the console with a newline at the end. No newline can be specified.

# print("No newline please.", end='')
# print("Thanks.")

your_name = "Nikolas"
course = "Intro to Python"

# Use .format() to dyamically add strings to another string. The variables are used in the order they are used as arguments in format().
greeting_message = "Welcome, {}, to the {} course!".format(your_name, course)
print(greeting_message)

# We can specify which variables to use by refering to the order in which they are placed as arguments. This allows us to use the same variable again.
format_test_message = "Welcome, {0}, to the {1} course. Oh, your name is {0}?".format(your_name, course)
print(format_test_message)

# We can do what we did above without refering to their placement, but this will eventually cause us to add a variable as an arguement to format() more than once.
format_test_message2 = "Welcome, {}, to the {} course. Oh, your name is {}?".format(your_name, course, your_name)
print(format_test_message2)

# Use triple quotation marks to denote multi-line strings. When printed, the format is kept.

multi_line = """Hi.
This is still part of the same string.
So is this."""
print(multi_line)

# \ can be used to break up a long line of code into multiple physical lines if needed. This does not affect the formatting.

long_string = "This string is really long \
so I had to break it up into \
multiple physical lines. \
Oh well."
print(long_string)
# r or R at the beginning of a string will specify a raw string. In a raw string, no special processing such as escape sequences are handled.

raw_string = r"There is no special processing \n \n \n"
print(raw_string)

# len() returns the number of characters that compose a string.

print(len("This has 23 characters."))

# input() accepts user input. Be aware that input is recieved as a string so it must be surrounded with quotation marks.
# user_input = input()
# print(user_input)

# int() and float() convert a string into an int and float, respectively. str() converts an int or float to a string.

# e notation is used to denote powers of 10. For example, 3e4 would be 30000.0. e notation results in a float.

print(3e4) # 30000.0
print(2e2)  # 200.0
print(4e-3) # 0.004