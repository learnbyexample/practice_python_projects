from string import punctuation

def spell_check(text):
    op = []
    for w in text.split():
        w = w.strip(punctuation)
        if w and w.lower() not in words:
            op.append(w)
    return op

word_file = 'word_files/words.txt'
with open(word_file) as f:
    words = {line.rstrip().lower() for line in f}
