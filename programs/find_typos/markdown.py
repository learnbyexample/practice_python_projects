import re
from string import punctuation

def spell_check(words, text):
    for w in text.split():
        w = w.strip(punctuation + '—')
        if w and w.lower() not in words:
            yield w

def process_md(words, md_file):
    links = re.compile(r'\[([^]]+)\]\([^)]+\)')
    inline_code = re.compile(r'`[^`]+`')
    hist = {}
    code_block = False
    with open(md_file) as f:
        for line in f:
            if line.startswith('```'):
                code_block = not code_block
            elif not code_block:
                line = links.sub(r'\1', line)
                line = inline_code.sub('', line)
                for w in spell_check(words, line):
                    hist[w] = hist.get(w, 0) + 1
    return hist

if __name__ == '__main__':
    word_file = 'word_files/words.txt'
    with open(word_file) as f:
        words = {line.rstrip().lower() for line in f}

    hist = process_md(words, 'md_files/sample.md')    
    for k in sorted(hist, key=lambda k: (k.lower(), -hist[k])):
        print(f'{k}: {hist[k]}')
