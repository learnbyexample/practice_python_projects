import re

file = 'top_comments_2019.txt'
pat = re.compile(r'''\s(?:[–-]|by)\s
                     |\s\\[–-]\s
                     |\s\*by\s
                     |[,-]\s
                  ''', flags=re.I|re.X)

with open(file) as f:
    for line in f:
        if re.fullmatch(r'\s+', line):
            continue
        elif not pat.search(line):
            print(line, end='')

