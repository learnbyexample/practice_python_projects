import glob
import re
from string import punctuation

def reference_words(word_files):
    words = set()
    for word_file in word_files:
        with open(word_file) as f:
            words.update(line.rsplit(':', 1)[0].rstrip().lower() for line in f)
    return words

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
    word_files = glob.glob('word_files/**/*.txt', recursive=True)
    words = reference_words(word_files)

    with open('typos.log', 'w') as opf:
        for md in glob.glob('md_files/**/*.md', recursive=True):
            hist = process_md(words, md)    
            if hist:
                opf.write(f'{md}\n')
                for k in sorted(hist, key=lambda k: (k.lower(), -hist[k])):
                    opf.write(f'{k}: {hist[k]}\n')
                opf.write(f'{"-" * 50}\n\n')
