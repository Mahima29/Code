import re
import os


# Opening the file in which we'll need to find the numbers
cwd = os.getcwd()  # Get the current working directory (cwd)
# print()
sample_file = open(cwd+"\\python3_coursera\\week2\\data.txt")

# Obtaining strings representing the numbers in that file
text = sample_file.read()  # With read, we read the entire text and not line by line
number_regex = '[0-9]+'
# Match any combination of one or more digits
numbers = re.findall(number_regex, text)

# Casting them to integers and getting the total sum
total = sum(int(num) for num in numbers)

print(total)

# Closing the file to avoid memory problems
sample_file.close()
