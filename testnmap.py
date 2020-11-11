###Download chrome driver for the desired OS on which the testing is to be done
###keep it in any specific direcory like (/Users/vishalkumar/downloads/chromedriver)
###Implementing Artificial intelligence using Pyautogui
###use "pip install pyautogui"
###use "pip install pyobjc-core"
### use "pip install pyobjc"
### allow all the system preference

#=========================================#
###First Build version for "macos mojave" 
###Author   : Vishal kumar
###Copyright: vishal kumar
###help     : vishalkumar770@rocketmail.com
#=========================================#

#IMPORTING THE REQUIRED LIBRARIES

import time
# import pyautogui
import random
import threading
import os
import subprocess 
import sys
from fpdf import FPDF
##nmap -T4 -A -v 192.168.43.122

#nmap_text = subprocess.getstatusoutput("nmap -T4 -A -v 192.168.43.150")


##############################################
##ip=192.168.43.150
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("address", help="enter the website address",)
args = parser.parse_args()
web_addr = args.address

nmap_text = subprocess.getstatusoutput("nmap -T4 -A -v "+web_addr)




file1 = open("output.txt","w") ## resets the main file each time
file1.writelines(nmap_text[1])
file1.close()




###nmap features

#######



###########text processing#########
###################################

def textprocess(KeyWord):
    import re
    log = []
    linenum=0
    pattern = re.compile(KeyWord,re.IGNORECASE)

    with open('output.txt','rt') as filework:
        for line in filework:
            linenum += 1
            if pattern.search(line) != None:
                log.append((linenum, line.rstrip('\n')))

    file2=open("text1.txt",'w')
    for logno in log:
    #file2.write("Line " + str(logno[0]) + ": " + logno[1])
        file2.write(logno[1])
        file2.write("\n")
    # print(logno[1])

def textprocess1(KeyWord):
    import re
    log = []
    linenum=0
    pattern = re.compile(KeyWord,re.IGNORECASE)

    with open('output.txt','rt') as filework:
        for line in filework:
            linenum += 1
            if pattern.search(line) != None:
                log.append((linenum, line.rstrip('\n')))

    file2=open("text2.txt",'w')
    for logno in log:
    #file2.write("Line " + str(logno[0]) + ": " + logno[1])
        file2.write(logno[1])
        file2.write("\n")
    # print(logno[1])
def textprocess2(KeyWord):
    import re
    log = []
    linenum=0
    pattern = re.compile(KeyWord,re.IGNORECASE)

    with open('output.txt','rt') as filework:
        for line in filework:
            linenum += 1
            if pattern.search(line) != None:
                log.append((linenum, line.rstrip('\n')))

    file2=open("text3.txt",'w')
    for logno in log:
    #file2.write("Line " + str(logno[0]) + ": " + logno[1])
        file2.write(logno[1])
        file2.write("\n")
    # print(logno[1])
def textprocess3(KeyWord):
    import re
    log = []
    linenum=0
    pattern = re.compile(KeyWord,re.IGNORECASE)

    with open('output.txt','rt') as filework:
        for line in filework:
            linenum += 1
            if pattern.search(line) != None:
                log.append((linenum, line.rstrip('\n')))

    file2=open("text4.txt",'w')
    for logno in log:
    #file2.write("Line " + str(logno[0]) + ": " + logno[1])
        file2.write(logno[1])
        file2.write("\n")
    #print(logno[1])
def textprocess4(KeyWord):
    import re
    log = []
    linenum=0
    pattern = re.compile(KeyWord,re.IGNORECASE)

    with open('output.txt','rt') as filework:
        for line in filework:
            linenum += 1
            if pattern.search(line) != None:
                log.append((linenum, line.rstrip('\n')))

    file2=open("text5.txt",'w')
    for logno in log:
    #file2.write("Line " + str(logno[0]) + ": " + logno[1])
        file2.write(logno[1])
        file2.write("\n")
    #print(logno[1])

textprocess("Starting Nmap")
textprocess1("open")
textprocess2("Nmap done")
textprocess3("(RSA)")
textprocess4("(ECDSA)")


class PDF(FPDF):
    def header(self):
        # Logo
        self.image('a.jpeg', 1, 1, 25)
        # Arial bold 15
        self.set_font('Arial', 'B', 15)
        # Move to the right
        self.cell(80)
        # Title
        self.cell(30, 10, 'Vulnerability Scanned Report', 0, 0, 'C')
        # Line break
        self.ln(20)

    # Page footer
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')

# Instantiation of inherited class
pdf = PDF()
pdf.alias_nb_pages()
pdf.add_page()
pdf.set_font('Times', '', 12)
# for i in range(1, 41):
#     pdf.cell(0, 10, 'Printing line number ' + str(i), 0, 1)
# pdf.output('tuto2.pdf', 'F')

file12 = open('text1.txt','r')
lines = file12.readlines()
num_lines = sum(1 for line in open('text1.txt'))
# new_text = "hello this is new line"
pdf.cell(0,10,"Initialization",0,1)
for i in range(0,num_lines):
    pdf.cell(0, 10, str(lines[i]), 1, 1)

pdf.cell(0,10,'\n',0,1)
pdf.cell(0,10,'\n',0,1)
pdf.cell(0,10,"Discovered Port that are open",0,1)

file123 = open('text2.txt','r')
lines = file123.readlines()
num_lines = sum(1 for line in open('text2.txt'))
for i in range(0,num_lines):
    pdf.cell(0,10,str(lines[i]),1,1)


pdf.cell(0,10,'\n',0,1)
pdf.cell(0,10,"Finished at",0,1)

file123 = open('text3.txt','r')
lines = file123.readlines()
num_lines = sum(1 for line in open('text3.txt'))
for i in range(0,num_lines):
    pdf.cell(0,10,str(lines[i]),1,1)

pdf.cell(0,10,'\n',0,1)
pdf.cell(0,10,'\n',0,1)


file123 = open('text4.txt','r')
lines = file123.readlines()
num_lines = sum(1 for line in open('text4.txt'))
for i in range(0,num_lines):
    pdf.cell(0,10,str(lines[i]),1,1)

pdf.cell(0,10,'\n',0,1)
pdf.cell(0,10,'\n',0,1)


file123 = open('text5.txt','r')
lines = file123.readlines()
num_lines = sum(1 for line in open('text5.txt'))
for i in range(0,num_lines):
    pdf.cell(0,10,str(lines[i]),1,1)





pdf.output('tuto.pdf','F')
file12.close()


