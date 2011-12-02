#!/usr/bin/env python
#
# File: en2pt.py
# Description: translate a word from english to portuguese
# Usage: 
#       $ ./en2pt.py word
#
# TODO: treat bold tag
# TODO: treat bullets


import re
import sys
import urllib2
import HTMLParser

#searching
url = 'http://michaelis.uol.com.br/moderno/ingles/index.php?lingua=ingles-portugues&palavra='
word = sys.argv[1]
html = urllib2.urlopen('%s%s' % (url, word)).read()

#parsing
pars = HTMLParser.HTMLParser()
pattern = r"<span class='descricao'>(.*)</span>"
d = re.search(pattern, html).groups()[0]
d = pars.unescape(d)
d = re.split('<B> *\d+</B>', d)[1:]
meanings = [line.strip() for line in d]

#printing
for i, meaning in enumerate(meanings):
    print "%s - %s" % (i+1, meaning)
