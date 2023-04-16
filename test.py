with open('data.csv', 'r') as data:
    letters = {}
    for row in data:
        col = row.split('\t')
        if col[0] in letters:
            letters[col[0]] = [
                max(letters[col[0]][0], int(col[1])),
                min(letters[col[0]][1], int(col[1]))
            ]
        else:
            letters[col[0]] = [int(col[1]), int(col[1])]

letters = sorted(letters.items(), key=lambda x: x[0])

# Transform letters into a tuple
letters = [(letter, max, min) for letter, (max, min) in letters]

print(letters)