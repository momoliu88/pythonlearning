import textwrap

sample_text = '''
To help people plan together, get together, and eat together, Google has launched a Ramadan hub (google.com/ramadan) with customized, location-based content. Find a local countdown to sunset (when you can enjoy a meal!), watch a popular YouTube video on DIY Ramadan decorations, get instant access to your grocery lists in the supermarket, and easily schedule all your gatherings on Calendar. In just three days, more than 1M users visited the site--check it out for yourself at google.com/ramadan.
'''
print 'No dedent:\n'
print textwrap.fill(sample_text, width=50)

print 'Dedented'
print textwrap.dedent(sample_text)

dedented_text = textwrap.dedent(sample_text).strip()
for width in [45, 70]:
  print '%d Colums:\n' % width
  print textwrap.fill(dedented_text, width=width)
  print

print textwrap.fill(dedented_text,
		    initial_indent = '',
		    subsequent_indent = ' '*2,
		    width=50)
