import re

mod = re.compile(r'(\d+)/(\d+)/(\d+)')

text = 'yesterday was 07/08/2018. tomorrow is 09/08/2018.'

y = mod.match('07/08/2017')
print(y.group(0))
x = mod.findall(text)
# print(x)

# print(re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text))

