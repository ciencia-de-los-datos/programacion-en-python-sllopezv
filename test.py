# From 'data.csv' (separated by tabs), generate a dictionary containing:
# Column 1 as key
# As value the sum of the values ​​in column 5 (which is a string that simulates a)

with open('data.csv', 'r') as data:
    letters = {}
    for row in data:
        col = row.split('\t')
        letter = col[0]
        for item in col[4].split(','):
            value = item.split(':')[1]
            if letter in letters:
                letters[letter] += int(value)
            else:
                letters[letter] = int(value)

print(dict(sorted(letters.items())))
