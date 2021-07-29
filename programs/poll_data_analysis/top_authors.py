from rapidfuzz import fuzz

ip_files = ('authors_2019.txt', 'authors_2021.txt')
op_files = ('top_authors_2019.csv', 'top_authors_2021.csv')

for ip_file, op_file in zip(ip_files, op_files):
    authors = {}
    with open(ip_file) as ipf, open(op_file, 'w') as opf:
        for line in ipf:
            name = line.rstrip('\n')
            authors[name] = authors.get(name, 0) + 1

        fuzzed = {}
        for k1 in sorted(authors, key=lambda k: -authors[k]):
            s1 = k1.lower().replace('.', '')
            for k2 in fuzzed:
                s2 = k2.lower().replace('.', '')
                if round(fuzz.ratio(s1, s2)) >= 90:
                    fuzzed[k2] += authors[k1]
                    break
            else:
                fuzzed[k1] = authors[k1]

        opf.write(f'Author,votes\n')
        for name in sorted(fuzzed, key=lambda k: -fuzzed[k]):
            votes = fuzzed[name]
            if votes >= 5:
                opf.write(f'{name},{votes}\n')
