import re

mystr="This is Python!456845689"

#x=re.findall('\w',mystr)
#x=re.findall('\W',mystr)
#x=re.findall('\d',mystr)
#x=re.findall('\D',mystr)
#x=re.findall('\s',mystr)
#x=re.findall('\S',mystr)
#x=re.findall(r'\bThis',mystr)
x=re.findall('\B89',mystr)
print(x)