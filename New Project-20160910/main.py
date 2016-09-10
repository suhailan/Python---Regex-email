import re

line = "huangrh(at)cse.dot.tamu.dot.edu";
local = re.search( r'(.+)\(at\)(.+)', line, re.M|re.I)
domain = re.search( r'\(at\)(.+)', line, re.M|re.I)
if local and domain:
   email = local.group(1)+"@"+domain.group(1)
   print email
else:
  print "Nothing found!!"

line = "huangrh at cse dot tamu dot edu";
local = re.search( r'(.+) at (.+)', line, re.M|re.I)
domain = re.search( r' at (.+)', line, re.M|re.I)
if local and domain:
    email = local.group(1)+"@"
    domainName = domain.group().split();
    for index in range(1,len(domainName)-1):
       email = email+domainName[index]+"."
    email = email+domainName[len(domainName)-1]
    print email
else:
  print "Nothing found!!"