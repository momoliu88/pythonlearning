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
#group and groups
text = 'This is some text -- with punctuation.'
pattern = r'\b(t\w+)\W+(\w+)'
regex = re.compile(pattern)
matched = regex.search(text)
print 'Groups,', matched.groups()
print 'Group 0,', matched.group(1)
print 'Group 1,', matched.group(2)
#group name
pattern = r'\b(?P<first_word>t\w+)\W+(?P<second_word>\w+)'
regex = re.compile(pattern)
matched = regex.search(text)
print 'Groups,', matched.groups()
print 'Groups dict,', matched.groupdict()
