# -*- coding: utf-8 -*-

import re
import os

base_dir = './content'

sum = {}

sdirs = ['Python', 'Linux', 'WebSecurity', 'Kali2', 'Vuln', 'PHP', 'Docker', 'HTTP', 'Git', 'Image', 'JS', 'Note',  'AWS', 'Python3', 'Simiki']

pattern = re.compile(r'title: "(.*?)"')

for root, dirs, files in os.walk(base_dir):
	if not dirs:
		sum[root.split('/')[-1]] = {}
		for file in files:
			if file.endswith('.md'):
				with open(root + os.sep + file) as f:
					content = f.read()
					match = pattern.search(content)
					try:
						sum[root.split('/')[-1]][file] = match.group(1)
					except:
						print file
#print sum	

txt = []
txt.append('# Summary\n\n')	
txt.append('* [Wiki](README.md)\n')

for d in sdirs:
	txt.append('* {}\n'.format(d))
	dict_ = sorted(sum[d].iteritems(), key=lambda d:d[1])
	for k, v in dict_:
		txt.append('    * [{t}]({p}/{f})\n'.format(t=v, p=d,f=k))

#print txt	
with open('SUMMARY.md', 'w') as f:
	f.write(''.join(txt))