import os
a  = os.popen('nmap 1.1.1.1').readlines()
print(a)
