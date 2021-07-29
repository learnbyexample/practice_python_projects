import re

ip_files = ('top_comments_2019.txt', 'top_comments_2021.txt')
op_files = ('authors_2019.txt', 'authors_2021.txt')

patterns = (r'.*\s(?:[–-]|by)\s+(.+)',
            r'.*\s\\[–-]\s+(.+)',
            r'.*\s\*by\s+(.+)',
            r'.*[,-]\s+(.+)')

for ip_file, op_file in zip(ip_files, op_files):
    with open(ip_file) as ipf, open(op_file, 'w') as opf:
        for line in ipf:
            if re.fullmatch(r'\s+', line):
                continue
            for pat in patterns:
                if m := re.search(pat, line, flags=re.I):
                    opf.write(m[1].strip('*\t ') + '\n')
                    break
