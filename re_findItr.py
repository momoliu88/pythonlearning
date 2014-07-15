import re
text = 'abaaaabaaa'
pattern = 'ab'
for match in re.finditer(pattern, text):
    print 'Found: %s at %d:%d' % (match.string, match.start(), match.end())


def test_patterns(text, patterns):
    for pattern, description in patterns:
        print 'Pattern %r (%s)\n' % (pattern, description)
        print ' %r' % text
        for match in re.finditer(pattern, text):
            s = match.start()
            e = match.end()
            substr = text[s:e]
            n_backslashes = text[:s].count('\\')
            prefix = '.' * (s + n_backslashes)
            print ' %s%r' % (prefix, substr)
        print
test_patterns('abaaaaaaabbbbbbbba',[('ab', 'a followed by b')])
test_patterns('abaaaaaaabbbbbbbba', [
    ('ab*', 'a followed by zero or more b'),
    ('ab+', 'a followed by one or more b'),
    ('ab?', 'a followed by zero or one b'),
    ('ab{2}', 'a followed by two b'),
    ('ab{2,3}', 'a followed by two to three b')
    ])
#? disable greedy matching.
test_patterns('abaaaaaaabbbbbbbba', [
    ('ab*?', 'a followed by zero or more b'),
    ('ab+?', 'a followed by one or more b'),
    ('ab??', 'a followed by zero or one b'),
    ('ab{2}?', 'a followed by two b'),
    ('ab{2,3}?', 'a followed by two to three b')
    ])
#character set
test_patterns('abaaaaaaabbbbbbbba', [
    ('a[ab]*?', 'a followed by zero or more a or b, not greedy'),
    ('a[ab]+', 'a followed by one or more a or b'),
    ('a[ab]?', 'a followed by zero or one a or b'),
    ])
