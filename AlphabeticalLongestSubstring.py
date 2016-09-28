initial = final = s[0]

#Python has the advantage to compare the characters without comparing their ASCII values, ex: 'a' > 'b' would return False

for i in range(1, len(s)):
    if s[i] >= initial[-1]:
        initial += s[i]
        if len(initial) > len(final):
            final = initial
    else:
        initial = s[i]

print('Longest substring in alphabetical order is:', final)
