import re
comp = re.compile('\w')
str = comp.findall('enot')
print(str)