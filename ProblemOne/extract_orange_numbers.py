import re 

# Extracting HTML data where the numbers are enclosed in <span> tags with a class of "orange".
with open('orange_numbers.html', 'r', encoding="utf-8") as file:
    data = file.read()
    
# Regular expression to find the numbers in the orange spans.
pattern = r'<span class="orange">(\d+)</span>'

# Find all matches of the pattern in the data.
matches = re.findall(pattern, data)

# Convert the matches to integers list use map.
numbers = list(map(int, matches))

# Print the extracted numbers.
print(numbers)