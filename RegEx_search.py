import re

text = '''DE: Lorem ipsum dolor Adela.1984@tuempresa.com
Para: incididunt ut labore et 21.07.87Melania@gmail.com
CC: exercitation ullamco id.3335.JoseCarlos@yahoo.com commodo consequat. 1Victor659633698@outlook.com in reprehenderit a.ruiz.carrillo@yahoo.comcillum dolore eu fugiat nulla adela.r.c@outlook.com sint occaecat cupidatat non a.r.carrillo@gmail.com qui officia deserunt mollit anim id est laborum.'''

print ('########### RE.SEARCH ###########\n')

searchResult = (re.search(r'[\w.+-]+@[\w-]+\.[\w.-]+', text))
print (type(searchResult))
print (searchResult)

print ('\n########### RE.MATCH ###########\n')

text2 = '''Adela.1984@tuempresa.com DE: Lorem ipsum dolor'''
text3 = '''DE: Lorem ipsum dolor Adela.1984@tuempresa.com'''

matchResult = (re.match(r'[\w.+-]+@[\w-]+\.[\w.-]+', text2))
print (type(matchResult))
print (matchResult,'\n')
matchResult = (re.match(r'[\w.+-]+@[\w-]+\.[\w.-]+', text3))
print (type(matchResult))
print (matchResult)

print ('\n########### RE.FINDALL ###########\n')

findallResult = (re.findall(r'[\w.+-]+@[\w-]+\.[\w.-]+', text))
print ('; '.join(findallResult))