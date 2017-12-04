file_name = 'day-4-input.txt'
with open(file_name) as f:
    content = f.readlines()
content = [x.strip() for x in content]
nope_1 = nope_2 = 0
for c in content:
    words = c.split(" ",)
    dupes_1 = [x for n, x in enumerate(words) if x in words[:n]]
    if dupes_1:
        nope_1 += 1
    size = len(words)
    new_words = []
    for w in words:
        new_words.append(''.join(sorted(w)))
    dupes_2 = [x for n, x in enumerate(new_words) if x in new_words[:n]]
    if dupes_2:
        nope_2 += 1
print 'valid passphrases using policy 1: {}'.format(len(content) - nope_1)
print 'valid passphrases using policy 2 : {}'.format(len(content) - nope_2)
