
import socket

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("address", help="enter the website address",)
args = parser.parse_args()
web_addr = args.address
#print(web_addr)

domain= socket.gethostbyname('google.com')
file = open('report.txt','w')
file.writelines([web_addr])
file.write("\n")
file.write(domain)
file.close()
